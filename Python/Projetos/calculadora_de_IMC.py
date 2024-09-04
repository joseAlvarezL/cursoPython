# calculadora de IMC
nome = input('Digite seu nome: ')
peso = input('Digite seu peso: ')
altura = input('Digite sua altura: ')

nome1 = str(nome)
peso1 = int(peso)
altura1 = float(altura)
imc_calculo = float(peso1/altura1**2)

imc_corporal = 'Olá {name}, seu peso é {weight} KG, é sua estatura é {height}.\nO cálculo do seu IMC resultou em: {imc:.2f}'
imc_final = imc_corporal.format(
    name=nome, weight=peso, height=altura, imc=imc_calculo
)

print(imc_final)