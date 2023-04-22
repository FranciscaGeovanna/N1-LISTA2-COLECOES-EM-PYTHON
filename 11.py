lista = []

print("Mostra os elementos que estão nos índices pares da lista")

for i in range(0,10):
    num = int (input("Digite um número: "))
    lista.append(num)
    
print("\nElementos que estão nos índices pares: ")
for j in range(len(lista)):
    if j % 2 == 0:
        print(lista[j])