"""
Iterando strings com while
"""
nome = 'Luiz Otávio'

i = 0
outro_nome = ''
while i < len(nome):
    letra = nome[i]
    outro_nome += f'*{letra}'
    i += 1
    print(outro_nome)