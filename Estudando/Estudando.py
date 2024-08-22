# Formatação
frase = '   Vamos até o brasil   '
print(frase[6:9])
print(len(frase)-frase.count(' '))
print(frase.count('a',0,16))
print(frase.find('abdriid'))
print('Vamos' in frase)
print(frase.replace('Vamos','Bora')) #Troca uma palavra por outra
print(frase.upper()) # Tramsforma em maiúculo
print(frase.lower()) # Transforma em minúsculo
print(frase.capitalize()) # So a primeira letra fica maiúscula
print(frase.title()) # A primeira letra de cada palavra fica maiúscula
print(frase.strip()) # Remove todos os espaços inúteis
print(frase.rstrip()) # Remove os espaços inúteis a direita
print(frase.lstrip()) # Remove os espações inúteis a esquerdaf
f1 = (frase.split()) # Divide a string considerando os espaços
print('-'.join(f1)) #
print(frase.startswith('V'))
#Bibliotecas
'''
from time import sleep
sleep(1)
'''
'''
import random
random(): Retorna um número aleatório entre 0 e 1.
randint(a, b): Retorna um número inteiro aleatório no intervalo [a, b], incluindo ambos os extremos.
choice(seq): Retorna um elemento aleatório de uma sequência (como uma lista, tupla ou string).
shuffle(seq): Embaralha aleatoriamente os elementos de uma sequência (como uma lista).
sample(population, k): Retorna uma lista de k elementos únicos selecionados aleatoriamente de uma população (sequência) sem substituição.
uniform(a, b): Retorna um número de ponto flutuante aleatório no intervalo [a
'''
'''
import os
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    limpar_terminal()
'''
'''
import math

math.ceil() - arredonda para cima 
math.floor() - arredonda para baixo
math.trunc() - eliminar o número da vírgula para frente
math.pow() - potência
math.sqrt() - raiz quadrada
math.factorial() - fatorar
math.sin()  - Seno 
math.cos() - Cosseno 
math.tan() - Tangente 
math.exp() - Exponencial 
math.log() - Logaritmo 
math.pi - Valor de pi
'''

# A seguir, são apresentados alguns dos principais métodos de listas em Python:
'''
enumerate() # devolve uma tupla contendo uma contagem (a partir de start, cujo padrão é 0) e os valores obtidos na iteração sobre iterable.
len() # Devolve o comprimento (o número de itens)
sorted() # Ordena elementos ordem crescente
sum() # Soma todos os elementos
max() # Devolve o maior item em um iterável ou o maior de dois ou mais argumentos.
min() # Devolve o menot item em um iterável ou o menor de dois ou mais argumentos.
range() # Os argumentos para o construtor de intervalo devem ser inteiros. Se o argumento step for omitido, será usado o padrão 1. Se o argumento start for omitido, será usado o padrão 0. Se step for zero, uma exceção ValueError será levantada.
append(): # adiciona um elemento ao final da lista.(bota na lista)
extend(): # adiciona os elementos de outra lista ao final da lista atual.
insert(): # insere um elemento em uma posição específica da lista.
remove(): # remove a primeira ocorrência de um elemento na lista.
pop(): # remove e retorna um elemento de uma posição específica da lista.
sort(): # ordena os elementos da lista em ordem crescente.
reverse(): # inverte a ordem dos elementos da lista.
count() : # Devolve o número de vezes em que elemento_x aparece na lista.
copy(): # Devolve uma cópia rasa da lista.
'''