while True:
  hora = input('Me fale a somente a hora em número: ')
  if not hora.isdigit():
    print('Dado inválido')
  else:
    hora = int(hora)
    if hora >= 0 and hora <=11:
        print('Bom Dia')
        break
    elif hora >= 12 and hora <=17:
        print('Boa Tarde')
        break
    elif hora >=18 and hora <=23:
        print('Boa Noite')
        break
    else: 
       print('Hora inválida, tente novamente')