tupla = ()

print('Verifica se o nome "Maria" está na lista ')

for i in range(0,3):
    nome = input("Digite um nome: ")
    tupla += (nome, )
    
if "Maria" in tupla or "maria" in tupla:
    print ("\nMaria está na tupla! ")
else: 
    print("\nMaria não está na tupla!")