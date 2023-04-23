conjunto = set()

print("Verifica se o número '3' está presente no conjunto de 5 números\n")

for i in range(0,5):
    num = int(input("Digite o {}° número: ".format(i+1)))
    conjunto.add(num)

print("\nConjunto: ", conjunto)
    
if 3 in conjunto:
    print("\nO número '3' está presente no conjunto!")
else:
    print("\nO número '3' não está presente no conjunto!")