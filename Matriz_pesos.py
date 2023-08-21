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
            