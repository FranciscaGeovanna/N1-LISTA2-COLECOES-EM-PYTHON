conjunto = set()

print ("Mostra quantos elementos há no conjunto \n")

for i in range(0,5):
    num = int (input("Digite um número: "))
    conjunto.add(num)

print ("\nSeu conjunto:", conjunto)
    
quantElementos = len(conjunto)

print("\nQuantidade de elementos deste conjunto: ", quantElementos)