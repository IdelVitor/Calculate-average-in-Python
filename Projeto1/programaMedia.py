import funçãoMedia as fn
while True:
        numero1 = int(input('Me diga um numero: '))
        numero2 = int(input('Me diga um numero: '))

        print(fn.media(numero1, numero2))


        sair = input('Se desejar sair, digite "s": ').strip().lower()
        if sair == 's':
                fn.opção(sair)
                break  
        elif sair == 'n':
                fn.opção(sair)
        else:
                print('Dado inválido, digite novamente!')

