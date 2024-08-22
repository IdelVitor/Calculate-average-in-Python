import funçãoMedia as fn

numero1 = int(input('Me diga um numero: '))
numero2 = int(input('Me diga um numero: '))

print(fn.media(numero1, numero2))

while True:
    sair = input('Se desejar sair, digite "s": ').strip().lower()

    if len(sair) > 1:
        print('Dado inválido, digite novamente!')
    else: 
        if sair == 's':
            print('Obrigado por utilizar o app')
            break
        else:
            print('Você optou por continuar.')
            break

