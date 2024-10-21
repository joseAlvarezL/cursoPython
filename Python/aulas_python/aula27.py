"""
Fatiamento de strings
 012345678 # 8 indices
 Olá mundo # 9 caracteres
-987654321
Fatiamento [i:f:p] [::] //Inicio, Fim e Passo
Obs.: a função len retorna a qtd de caracteres da variavel/str
# Contagem(123456789) ≠ Índice (0123456789)
"""
variavel = 'Olá mundo'
print(variavel[4:]) # Ele vai até o final da str

print(variavel[4:7]) # O final não é incluido

print(variavel[4:8]) 

print(variavel[0:5]) 

print(variavel[:5]) 

print(variavel[-8:-2]) 

print(len(variavel[3])) 

print(len(variavel))

print(variavel[0:9:1])

print(variavel[0:9:2])

print(variavel[0:9:3])

print(variavel[::-1]) # [-1] cmç a ir para tras / inverte

print(variavel[-1:-10:-2]) 

print(variavel[0:len(variavel):1])