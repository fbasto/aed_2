import random

values = []
#igual
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
                    # print (dist)
                    dist = random.randint(1,number*100)
                values.append(dist)
                matrix[i][k] = dist
                matrix[k][i] = dist
    # print("M:",matrix)
    filename = "tarefa_1" + str(number) + ".txt"
    create_file(number,matrix,filename)
#dif
def mapas2(num):
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
                    # print (dist)
                    dist = random.randint(1,number*100)
                values.append(dist)
                matrix[i][k] = dist
    # print("M:",matrix)
    filename = "tarefa_2_" + str(number) + ".txt"
    create_file(number,matrix,filename)

def check(n):
    # print("CHECK: ",n)
    if(n in values):
        return True
    else:
        return False



def create_file(number,matrix,filename):
    f = open(filename,'w')
    f.write("startin 1\n")
    iguais = False
    if (matrix[1][0]==matrix[0][1]):
        iguais = True
    for i in range(number):
        aux = ""
        for j in range(number):
            # if (j == number-1):
            #     aux = aux + str(matrix[i][j]) + "\n"
            # else:
            #     aux = aux + str(matrix[i][j]) + " "
            if (iguais):
                if(i<j):
                    # print("i=",i,"; j=",j,"; peso=",matrix[i][j])
                    aux = str(i+1) + " " + str(j+1) + " " + str(matrix[i][j]) + "\n"
                    # else:
                    #     aux = str(i) + str(j) + str(matrix[i][j]) + "\n"
                    # print("String: ",aux)
                    f.write(aux)
            elif(iguais == False):
                if(i!=j):
                    # print("i=",i,"; j=",j,"; peso=",matrix[i][j])
                    aux = str(i+1) + " " + str(j+1) + " " + str(matrix[i][j]) + "\n"
                    # else:
                    #     aux = str(i) + str(j) + str(matrix[i][j]) + "\n"
                    # print("String: ",aux)
                    f.write(aux)

    f.write("M\n")
    for i in range(number):
        aux = ""
        for j in range(number):
            if (j == number-1):
                aux = aux + str(matrix[i][j]) + "\n"
            else:
                aux = aux + str(matrix[i][j]) + " "
        f.write(aux)
    f.write("0")
    f.close()


if __name__ == '__main__':
    while(True):
         userop = eval(input("1) Criar novo mapa\n2) Sair\n"))
         if (userop == 1):
            userop2 = eval(input("1)Mapa com distancias entre duas cidades iguais(ambos os sentidos)\n2)Mapa com distancia diferentes entre cidades\n"))
            if(userop2 == 1):
                x = input("Tamanho do mapa: ")
                mapas(x)
            elif(userop2 == 2):
                x = input("Tamanho do mapa: ")
                mapas2(x)
         elif (userop == 2):
            break
