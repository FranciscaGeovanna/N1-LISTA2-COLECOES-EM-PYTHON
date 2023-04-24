dicionario = {}

print("Verifica se existe a chave 'profissão' ")

quant = int(input("\nQuantas chaves e valores deseja informar? "))

for i in range(quant): 
    chave = input("Digite a {}° chave: ".format(i+1))
    valor = input("Digite o {}° valor: ".format(i+1))
    dicionario[chave] = valor
    
if "profissão" in dicionario:
    print("\nProfissão está presente no dicionário!")
else:
    print("\nProfissão não está no dicionário!")
