valorPrestação = float(input('Qual o valor da prestação: '))
diasAtraso = int(input('Quantos dias de atraso: '))
valorTotal = float(input('Qual o valor total da dívida: '))

def valorPagamento(valorPrestação, diasAtraso, valorTotal):
   
  while True:
    if diasAtraso <= 0:
      print(f'O valor da prestação é de: {valorPrestação}')
      break
    else:
      multa = valorPrestação * 0.03
      juros = valorPrestação * 0.001 * diasAtraso
      valorFinal = valorPrestação + multa + juros
    
      valorTotal -= valorFinal

      if valorTotal < 0:
          print('Você não tem dívidas')
      else:
          print(f'O valor da prestação com atraso é de: {valorFinal}')
          print(f'O valor total da dívida é de: {valorTotal}')
      break
    
valorPagamento(valorPrestação, diasAtraso, valorTotal)