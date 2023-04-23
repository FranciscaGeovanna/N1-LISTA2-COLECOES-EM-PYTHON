lista = []

print("Multiplica cada número da lista por 2\n")

for i in range(0,10):
    num = int(input("Digite o {}° número: ".format(i+1)))
    lista.append(num)

lista2 = []

print("\nResultados das multiplicaçōes: ")
for num in lista:
    m = num*2
    lista2.append(m)
    print("{} X 2 = {}".format(num, m))