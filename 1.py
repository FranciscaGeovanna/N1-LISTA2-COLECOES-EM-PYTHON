lista = []

for i in range(0, 5):
    num = int (input ("Digite o {}° número: ".format(i+1)))
    lista.append(num)

novoNum = int (input("Digite mais um número: "))
lista.append(novoNum)

print("\nLista completa: ", lista)