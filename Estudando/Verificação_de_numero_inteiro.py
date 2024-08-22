def verificacao_de_numero():
   
  while True:
    numero_inteiro = input('Me fale um número inteiro: ')
    try:
          numero = int(numero_inteiro)
          if numero % 2 == 0:
              print(f'{numero} é par')
          else:
              print(f'{numero} é ímpar')
          break
    except ValueError:
          print('O dado inserido não é um número inteiro.')

verificacao_de_numero()