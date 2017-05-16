import tsp_solver

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
	def transformToMatrix(self):
		matrix = [[0 for x in range(len(self.getVertices()))] for y in range(len(self.getVertices()))] 
		# print(matrix)
		starter = g.getStarter()
		counter = 0
		for i in list(self.vertList.values()):
			print(starter)
			if i != starter:
				value = starter.getWeight(self.getVertex(i.getId()))
				matrix[0][counter] = value
				matrix[counter][0] = value
				print("inseriu",value)
			else:
				matrix[0][counter] = 0
			counter=counter+1
		row = 1
		counter = 1;
		for j in list(self.vertList.values()):
			for k in list(self.vertList.values()):
				print("cmpring =",j.getId(),k.getId())
				if j != starter and k != starter:
					if j != k:
						value = j.getWeight(self.getVertex(k.getId()))
						matrix[row][counter] = value
						matrix[counter][row] = value
						counter=counter+1
						print("inseriu",value)
					else:
						matrix[row][counter] = 0
					counter=counter+1
			row=row+1
			counter=1
		print(matrix)
		return matrix


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

g = Graph()
print("Para adicionar o nó inicial: \"startin <nome>\" ;\nPara adicionar ligação entre dois nós: \"<nó1> <nó2> <peso>\" .")
while(True):
	userinput = input().split(' ')
	print(userinput)

	if(userinput[0]=='0'):
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
print(g.getVertices())
# print(g.getVertex('1').getWeight(g.getVertex('2')))
matrix = g.transformToMatrix()

# TODO aqui encontrar caminho
print("a")