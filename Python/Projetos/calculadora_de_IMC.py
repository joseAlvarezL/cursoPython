# calculadora de IMC

nome = input('Digite seu nome: ')
altura = input('Digite sua altura: ')
peso = input('Digite seu peso: ')
idade = input('Digite sua idade: ')

nome1 = str(nome)
altura1 = float(altura)
peso1 = int(peso)
idade1 = int(idade)

nascimento = 2024 - idade1
calculo_imc = peso1/altura1**2

calculo = '\nSeu nome é: {name}\nVocê possui {height:.2f} de altura\nSeu peso é {weight} KG\nSua idade é {age}\nData de nascimento: {birth}\nO resultado do seu IMC: {imc:.3f}'

imc_total = calculo.format(
    name=nome1, height=altura1, weight=peso1, age=idade1, birth=nascimento, imc=calculo_imc
)

print(imc_total)