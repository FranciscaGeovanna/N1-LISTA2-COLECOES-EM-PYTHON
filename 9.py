print("Remove os números pares de um conjunto")

conjunto = set()

print("\ninforme 10 números\n")
for i in range (0,10):
    num = int (input("Digite o {}° número: ".format(i+1)))
    conjunto.add(num)

print("\nConjunto sem os números pares: ")

copiar = conjunto.copy()

for num in conjunto:
    if num %2 == 0:
        copiar.remove(num)
  
print(copiar)
