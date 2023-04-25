print ("Mostra vértices adjacentes ao vértice 'A'\n")

grafo = {}

quantV = int(input("Insira a quantidade de vértices: "))

for i in range(quantV):
    vertices = input("Digite os vértices: ")
    grafo[vertices] = []

quantA = int(input("\nInsira a quantidade de arestas: "))

for j in range(quantA):
    a, b = input("Digite os vértices que formam a aresta {}: ".format(j+1)).split()
    grafo[a].append(b)
    grafo[b].append(a)

adjA = grafo['A'] #adjacente
print("\nVértices adjacentes ao vértice 'A': ", adjA)
