conjunto = set()

for i in range(0,5):
    num = int (input("Digite o {}° número: ".format(i+1)))
    conjunto.add(num)

    removNum = int (input("\nQual número deseja remover? "))
    if removNum in conjunto:
        conjunto.remove(removNum)
        print("\nConjunto: ", conjunto)
    else:
        print ("O número digitado não está no conjunto!")