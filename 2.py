print("Substitui um dos nomes da tupla\n")

tupla = ()

for i in range(0,3):
    nome = input ("Digite um nome: ")
    tupla += (nome, )
    
nomeEscolhido = input("\nEscolha um dos nomes para substituir: ")

if nomeEscolhido in tupla:
    lista = list(tupla)

    novoNome = input("\nDigite o novo nome: ")

    print("\nTupla Original: ", tupla)

    indice = lista.index(nomeEscolhido) #Acha o índice do nome escolhido para substituir 

    lista[indice] = novoNome

    tupla = tuple(lista)

    print ("Tupla Editada: ", tupla)
else:
    print("\nO nome escolhido não está presente na tupla!")
    print("\nTupla: ", tupla)