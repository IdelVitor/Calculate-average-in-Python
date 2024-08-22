import os

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

questoes_objetivas = []
respostas = []

def pergunta_e_resposta():
    while True:
        numero_de_questoes = int(input('Me fale a quantidade de questões que você gostaria de fazer: '))
        for i in range(numero_de_questoes):
            questao = input(f'Me fale a questão {i+1}: ')
            questoes_objetivas.append(questao)
            while True:
                itens = input(f'Me fale a resposta correta da questão {i+1} (a/b/c/d): ')
                if itens in ['a', 'b', 'c', 'd']:
                    respostas.append(itens)
                    break
                else:
                    print('Dado inválido, por favor insira a resposta correta (a/b/c/d).')
        break

def quantidade_de_alunos():
    while True:
        quantidade = int(input('Me fale a quantidade de alunos que você gostaria de fazer a prova: '))
        if quantidade < 1:
            print('Quantidade inválida, por favor insira um número maior que 0.')
        else:
            limpar_terminal()
            return quantidade

def resultado():
    numero_de_alunos = quantidade_de_alunos()
    for aluno in range(numero_de_alunos):
        print(f"Aluno {aluno + 1}:")
        acertos = 0
        erros = 0
        for i in range(len(questoes_objetivas)):
            while True:
                resposta = input(f'Me fale a sua resposta da questão {i+1} (a/b/c/d): ')
                if resposta not in ['a', 'b', 'c', 'd']:
                    print('Dado inválido, por favor insira a resposta correta (a/b/c/d).')
                else:
                    if resposta == respostas[i]:
                        acertos += 1
                    else:
                        erros += 1
                    break
        print(f"Aluno {aluno + 1} teve {acertos} acertos e {erros} erros.")


pergunta_e_resposta()
resultado()