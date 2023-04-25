print("Verifica se a aresta (A,C) está presente no grafo\n")

grafo = {}

quantV = int(input("Insira a quantidade de vértices: "))

for i in range(quantV):
    vertices = input("Digite os vértices: ")
    grafo[vertices] = []

quantA = int(input("\nInsira a quantidade de arestas: "))

for j in range(quantA):
    a, b = input("Digite os vértices que formam a {}° aresta: ".format(j+1)).split()
    grafo[a].append(b)
    grafo[b].append(a)

print("\nGrafo: ", grafo)

if 'A' in grafo and 'C' in grafo['A']:
    print("\nA aresta ('A','C') está presente no grafo!")
else:
    print("\nA aresta ('A,'C') não está presente no grafo!")