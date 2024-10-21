"""
Introdução ao try/except
try -> tentar  executar o código
except -> ocorreu algum erro ao tentar executar
"""
# Dica: Utilize o F2 para renomear em lote

numero_str = input(
    'Vou dobrar o número que vc digitar: '
    )
try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# print(numero_str.isdigit())
#  isdigit() | retorna True se só houver dígitos(0-9) na string.

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número') 

"""
Diferença entre try/except e if/else no Python

🧠 try/except captura e lida com exceções (erros), enquanto if/else verifica condições lógicas e controla o fluxo normal do código sem lidar com erros.

# if e else são para lógica, try/except são para erros (exceptions).
"""
