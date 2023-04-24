tupla = ()

print("Verifica quantas vezes o nome 'Maria' aparece na tupla\n")

for i in range(0,3):
    nome = input("Digite um nome: ")
    tupla += (nome, )
    
quant = tupla.count("Maria")

print(f"\nO nome 'Maria' aparece {quant} vezes na tupla")
