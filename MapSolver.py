from tsp_solver import *

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
		self.boolstartin = False
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr] = weight
	def starter(self):
		self.boolstartin = True
	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
	def getConnections(self):
		return self.connectedTo.keys()
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
		dist = dist + int(matrix[priorvertex][i-1])
		priorvertex = i-1
		print("dist updated to:",dist)
	dist = dist + int(matrix[priorvertex][0])
	print("final dist:",dist)
	return dist



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
path = solve_tsp(matrix)
distance = calcDistance(path, matrix)
print("Encontrou o melhor caminho:",path,"com distância de",distance)

