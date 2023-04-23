dic = {}

quant = int (input("Quantas chaves e valores deseja informar? "))

print("\n")

for i in range(quant):
    chave = input("Digite a {}° chave: ".format(i+1))
    valor = input("Digite o {}° valor: ".format(i+1))
    dic [chave] = valor

nasceu = input("\nEm qual cidade você nasceu? ")

dic ["Cidade em que nasceu"] = nasceu

print ("\nDicionário:", dic)