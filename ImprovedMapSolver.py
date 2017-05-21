from tsp_solver import *
import sys
import time

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
		self.symmetric = 1
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
	def setSymmetric(self,boolval):
		self.symmetric = boolval
	def addEdge(self,f,t,cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], cost, self.symmetric)
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
	def addNeighbor(self,nbr,weight=0,symmetric=1):
		self.connectedTo[nbr] = weight
		self.strConnections.add(nbr.getId())
		if(symmetric==1):
			nbr.connectedTo[self] = weight
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
	lenGraph = len(graph.getVertices())
	best = [0,0]
	stack = [(start, [start], 0)]
	newDist = 0
	while stack:
		(vertex, path, newDist) = stack.pop()
		# print("stack=",stack)
		# print("vertex=",(vertex, path))
		connections = (graph.getVertex(vertex)).getStrConnections()
		for next in connections - set(path):
			if (best[0] == 0 or newDist < best[0]):
				# print("path=",path)
				# print("Checking",connections,"-",set(path))
				if lenGraph == len(path)+1:
					# print("complete path found=",path+[next])
					finalDist = newDist+int(matrix[int(path[len(path)-1])-1][int(graph.getVertex(next).getId())-1])
					finalDist = finalDist+int(matrix[int(graph.getVertex(next).getId())-1][0])
					if best[0] == 0 or (best[0] != 0 and finalDist < best[0]):
						#print("bestDist=",best[0]," e bestPath=",best[1])
						best[1] = path+[next]
						best[0] = finalDist


					#print("len path =",len(path))
					#print("len graph =",len(graph))
					# print("path found=",path)
				else:
					# print("lenpath=", len(path),"->path[len(path)-1]=",path[len(path)-1],"com next=",graph.getVertex(next).getId())
					stack.append((next, path + [next], newDist + int(matrix[int(path[len(path)-1])-1][int(graph.getVertex(next).getId())-1])))
	print("Encontrou o melhor caminho:",best[1],"com distância de",best[0])

if __name__ == "__main__":
	g = Graph()
	print("Para adicionar o nó inicial: \"startin <nome>\" ;\nPara adicionar ligação entre dois nós: \"<nó1> <nó2> <peso>\" .")
	while(True):
		userinput = input().split(' ')
		if(userinput[0]=='M'): # IGUAIS
			g.setSymmetric(1)
			#print("breaking because EOF")
			break
		elif(userinput[0]=='m'): # DIFERENTES
			g.setSymmetric(0)
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
#OPÇAO 1
	# paths = list(dfs_paths(g,g.getStarter().getId()))
	# bestPath = 0
	# bestDist = 0
	# for i in list(paths):
	# 	# print(i)
	# 	newDist = calcDistance(i,matrix)
	# 	if bestDist == 0 or (bestPath[0] != 0 and newDist < bestDist):
	# 		# print("bestDist=",bestDist," e bestPath=",bestPath)
	# 		bestDist = newDist
	# 		bestPath = i
#OPÇAO 2
	dfs_paths(g,g.getStarter().getId())

	end = time.time()
	print("Operacao demorou: %.10f segundos"%(end-start))
