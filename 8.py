dicionario = {}

quant = int(input("Quantas chaves e valores deseja informar? "))

for i in range(0, quant):
    chave = input(f"Digite a {i+1}° chave: ")
    valor = input(f"Digite o {i+1}° valor: ")
    dicionario[chave] = valor

if "idade" in dicionario:
    print('\nO valor da chave "Idade" é: ', dicionario["idade"])
else:
    print("\nA chave 'Idade' não está presente no dicionário!")
