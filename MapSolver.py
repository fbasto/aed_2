from tsp_solver import *
import time

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
	def addVertex(self,key):
		self.numVertices = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex
	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None
	def __contains__(self,n):
		return n in self.vertList
	def addEdge(self,f,t,cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], cost)
	def getVertices(self):
		return self.vertList.keys()
	def getStarter(self):
		for i in list(self.vertList.values()):
			# print("boolstart=",i.getBoolStart())
			if(i.getBoolStart()):
				return i
	def __iter__(self):
		return iter(self.vertList.values())


class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}
		self.strConnections = set()
		self.boolstartin = False
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr] = weight
		nbr.connectedTo[self] = weight
		self.strConnections.add(nbr.getId())
		nbr.strConnections.add(self.id)
	def starter(self):
		self.boolstartin = True
	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
	def getConnections(self):
		return self.connectedTo.keys()
	def getStrConnections(self):
		return self.strConnections
	def getId(self):
		return self.id
	def getWeight(self,nbr):
		return self.connectedTo[nbr]
	def getBoolStart(self):
		return self.boolstartin;

def printMatrix(matrix):
	strg = "1"
	for i in range(1,len(matrix)):
		strg = strg + "\t" + str(i+1)
	print("\t",strg)
	for k in range(0,len(matrix)):
		strg = ""
		for l in range(0,len(matrix)):
			# print("num=",str(matrix[k][l]))
			strg = strg + "\t" + str(matrix[k][l])
		print(k+1,strg)

def calcDistance(path, matrix):
	dist = 0
	priorvertex = 0
	for i in range(1,len(path)):
		# print("traveling from",priorvertex+1,"to",i+1)
		dist = dist + int(matrix[int(path[priorvertex])-1][int(path[i])-1])
		# print("dist=",dist,"+",int(matrix[int(path[priorvertex])-1][int(path[i])-1]),"from path[",priorvertex,"][",i,"]")
		priorvertex = i
		# print("dist updated to:",dist)
	dist = dist + int(matrix[int(path[priorvertex])-1][int(path[0])-1])
	# print("final dist:",dist)
	return dist

def dfs_paths(graph, start):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        connections = (graph.getVertex(vertex)).getStrConnections()
        for next in connections - set(path):
            # print("Checking",connections,"-",set(path))
            if len(graph.getVertices()) == len(path)+1:
                yield path + [next]
                #print("len path =",len(path))
                #print("len graph =",len(graph))
                #print("path found=",path)
            else:
                stack.append((next, path + [next]))

def dfs_paths_optimized(graph,start):
	print("TODO")

if __name__ == "__main__":
	g = Graph()
	print("Para adicionar o nó inicial: \"startin <nome>\" ;\nPara adicionar ligação entre dois nós: \"<nó1> <nó2> <peso>\" .")
	while(True):
		userinput = input().split(' ')
		if(userinput[0]=='M'):
			#print("breaking because EOF")
			break
		if(userinput[0]=='startin'):
			#print("startin")
			g.addVertex(userinput[1])
			g.getVertex(userinput[1]).starter()
		else:
			node1 = userinput[0]
			node2 = userinput[1]
			weight = userinput[2]
			if(g.getVertex(node1) == None):
				g.addVertex(node1)
			if(g.getVertex(node2) == None):
				g.addVertex(node2)
			g.addEdge(node1,node2,weight)
	# print(g.getVertex('1').getWeight(g.getVertex('2')))
	matrix = [[0 for x in range(len(g.getVertices()))] for y in range(len(g.getVertices()))] 
	i=0
	while(True):
		userinput = input().split(' ')
		if(userinput[0]=='E'):
			#print("breaking because EOF")
			break
		else:
			for j in range(0,len(g.getVertices())):
				matrix[i][j] = userinput[j]
		i=i+1
	printMatrix(matrix)


	# debug
	# for i in g.getVertices():
	# 	print(g.getVertex(i))


	start=time.time()

	paths = list(dfs_paths(g,g.getStarter().getId()))
	bestPath = 0
	bestDist = 0
	for i in list(paths):
		# print(i)
		newDist = calcDistance(i,matrix)
		if bestDist == 0 or (bestPath[0] != 0 and newDist < bestDist):
			# print("bestDist=",bestDist," e bestPath=",bestPath)
			bestDist = newDist
			bestPath = i

	print("Encontrou o melhor caminho:",bestPath,"com distância de",bestDist)

	end = time.time()
	print("Operacao demorou: %.10f segundos"%(end-start))
