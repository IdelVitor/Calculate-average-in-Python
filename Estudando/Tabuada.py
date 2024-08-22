while True:
    numero = int(input('Me diga um numero para a tabuada de 1 a 10:'))
    if numero < 1 or numero > 10:
        print('DADO INVÁLIDO')
    else: 
        for i in range(1,11):
            print(f'{numero} x {i} = {numero*i}')
