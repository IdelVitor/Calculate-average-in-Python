while True:

    nome = str(input('Me fale seu nome:'))
    quantidade_de_letras_do_nome = len(nome)
    if quantidade_de_letras_do_nome <= 4:
        print('Seu nome é pequeno')
        break
    elif quantidade_de_letras_do_nome >= 5 and quantidade_de_letras_do_nome <= 6:
        print('Seu nome é normal')
        break
    else:
        print('Seu nome é muito grande')
        break
