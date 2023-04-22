tupla = ()

print("Mostra o 1° elemento da tupla")

for i in range(0,5):
    num = int(input ("Digite um número: "))
    tupla += (num, )
    
print("\nPrimeiro número da sua tupla: ", tupla[0])