# Comparar entre 2 números

numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

numero1int = int(numero1)
numero2int = int(numero2)

if numero1int >= numero2int:
    print(f'Número {numero1int} é maior que o número {numero2int}')



else:
    print(f'O número {numero2int} é maior')