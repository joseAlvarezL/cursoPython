"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel:!>10}')
print(f'{variavel:%<10}.')
print(f'{variavel:$^10}.')

print(f'{-1000.30213129321:-,.1f}')
# O valor formatado é negativo (-1000.30213129321).
# O sinal negativo (-) é sempre exibido automaticamente para números negativos, independentemente do especificador de formatação.

print(f'{1000.30213129321:-,.1f}') 
# O valor formatado é positivo (1000.30213129321).
# O sinal positivo (+) não é exibido por padrão, a menos que você use o especificador + na formatação (Alinhamento à esquerda).


print(f'{1000.30213129321:+,.1f}') # O + força a exibição do sinal, resultando em +1,000.3.

print(f'{1000.30213129321:0>+10,.1f}')
# 0>: Preenche com zeros à esquerda do número, mas depois do sinal.

print(f'{1000.30213129321:0=+10,.1f}')
# 0=: Preenche com zeros logo após o sinal do número, resultando em uma disposição onde o sinal aparece antes de qualquer preenchimento.

print(f'O hexadecimal de 1500 é {1500:08x}')

print(f'{variavel!r}')