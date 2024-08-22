import random

lista = []

while True:
    quantidade_de_dezenas = int(input('Me fale a quantidade de dezenas que você gostaria de marcar de 15 a 18 números:'))
    if quantidade_de_dezenas < 15 or quantidade_de_dezenas > 18:
        print('Quantidade inválida')
    else:
        for i in range(quantidade_de_dezenas):
            while True:
                numeros = int(input(f'Me fale os números {i+1}:'))
                if numeros in lista:
                    print("Número repetido. Por favor, digite um número diferente.")
                elif numeros < 1 or numeros > 25:
                    print("Número inválido. Por favor, digite um número entre 1 e 25.")
                else:
                    lista.append(numeros)
                    break
        break