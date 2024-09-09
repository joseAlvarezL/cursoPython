# Calculadora de IMC

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
peso = input('Digite seu peso: ')
altura = input('Digite sua altura: ')

nome1 = str(nome)
idade1 = int(idade)
peso1 = int(peso)
altura1 = float(altura)
data_nascimento = int(2024-idade1)

imc1 = peso1/altura1**2

dados = '\n\nSeu nome é: {name}\nSua idade é: {age}\nData de nascimento: {birth}\nPeso em quilos: {weight}KG\nSua altura: {height}\nCalculo de IMC: {imc:.2f}'

calculo_imc = dados.format(
    name=nome1, age=idade1, birth=data_nascimento, weight=peso1, height=altura1, imc=imc1
)

print(calculo_imc)