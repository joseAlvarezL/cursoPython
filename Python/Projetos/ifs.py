entrada = input('Vc deseja [E]ntrar ou [S]air? ')
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


if entrada == 'E' or entrada == 'e': # entrada == 'e': Verifica se a entrada é igual a 'e'.
    print("Você entrou")

    if nome == 'jose' or nome == 'lupita':
        print(f'seu nome é {nome}')

        if idade == "18" or idade == "20":
            print(f'vc acertou a idade {idade}')
            
        else:
            print("vc errou a idade")
    else:
        print("vc errou o nome")
else:
    print("vc errou a entrada")


