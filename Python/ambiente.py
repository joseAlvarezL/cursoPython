nome = 'jose'
idade = int('18')
peso = 70
nascimento = 2024-idade
altura = 1.70
imc = peso/altura**2

corpo = 'O paciente {identidade} possui a idade de {idade} e sua data de nascimento: {data_de_nascimento} ele tem {altura_metros:.2f} e seu IMC é: {indice_de_massa_corporal:.3f}'.format(
    identidade=nome, idade=idade, quilos=peso, data_de_nascimento=nascimento, altura_metros=altura,indice_de_massa_corporal=imc
)

print(corpo)