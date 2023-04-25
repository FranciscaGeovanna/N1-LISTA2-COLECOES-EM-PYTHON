print("Remove uma aresta do grafo\n")

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

print("\nGrafo: ", grafo)

a, b = input("\nQual aresta deseja remover do grafo? ").split()

if a in grafo and b in grafo:
    grafo[a].remove(b)
    grafo[b].remove(a)
    print("\nAresta removida!")
    print("\nGrafo com a aresta removida: ", grafo)
else:
    print("\nA aresta informada não exite no grafo!")
