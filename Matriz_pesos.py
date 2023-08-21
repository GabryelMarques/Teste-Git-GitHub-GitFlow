class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self,u,v,peso ):
        self.grafo[u-1][v-1] = peso 
        self.grafo[v-1][u-1] = peso 

    def mostra_matriz(self):
        print("A matriz de Distâncias é")
        for i in range(self.vertices):
            print(self.grafo[i])
            
v=int(input("Qual a quantidade de vertices?"))
g = Grafo(v)
op= 0
while(op!= -1):
    print("(1)-Add")
    print("(2)-Mostar")
    print("(-1)-Sair")
    op = int(input())
    
    if(op == 1):
        i=int(input("Vértice de partida"))
        j=int(input("Vértice de destino"))
        p=int(input("Peso da aresta"))
        g.adiciona_aresta(i,j,p)
    elif(op == 2):
        g.mostra_matriz()
    else:
        op =-1