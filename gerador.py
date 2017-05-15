import random

values = []

def mapas(num):
    number = int(num)
    matrix = [[0 for x in range(number)] for y in range(number)] 
    for i in range(number):
        for k in range(number):
            if(i==k):
                matrix[i][k]=0
            else:
                if(matrix[i][k] == 0):
                    dist = random.randint(1,number*100)
                while(check(dist) == True):
                    print (dist)
                    dist = random.randint(1,number*100)
                values.append(dist)
                matrix[i][k] = dist
                matrix[k][i] = dist

    create_file(number,matrix)

def check(n):
    print("CHECK: ",n)
    if(n in values):
        return True
    else:
        return False



def create_file(number,matrix):
    filename = "tarefa_" + str(number) + ".txt"
    f = open(filename,'w')
    for i in range(number):
        aux = ""
        for j in range(number):
            if (j == number-1):
                aux = aux + str(matrix[i][j]) + "\n"    
            else:  
                aux = aux + str(matrix[i][j]) + " "    

            
        f.write(aux)
        print("String: ",aux)
    f.close()


if __name__ == '__main__':
    x = input("Tamanho do mapa: ") 
    mapas(x)

