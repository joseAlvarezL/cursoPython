# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar': # 1 condição só necessita if
    print('Você entrou no sistema')
    print(1234)

elif entrada == 'sair': # depende do if
    print('Você saiu do sistema')
    
else: # última opção - também depende do if
    print('Você não digitou nem ENTRAR nem SAIR')

print('FORA DOS BLOCOS')