nome = 'José Alvarez'
altura = 1.70
peso = 70
imc = peso/altura**2

"f-strings" # f = formatação
linha_1 = f'{nome}, tem, {altura:.2f}, de altura'
linha_2 = f'pesa:, {peso}, quilos e seu IMC é:'
linha_3 = f'{imc:.3f}'

print(linha_1)
print(linha_2)
print(linha_3)

    # José tem 1.70 de altura,
    # pesa 70 quilos e seu IMC é
    # 24.221
