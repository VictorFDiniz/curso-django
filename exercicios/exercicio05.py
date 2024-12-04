"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')
numero_int = int(numero_str)
numero_par = numero_int % 2 == 0
numero_impar = numero_int % 2 != 0

try:
    if numero_par:
        print('O número:', numero_int, 'é par')
    elif numero_impar:
        print('O número:', numero_int, 'é ímpar')
except:
    print('Entrada inválida!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input('Digite um horário para receber uma saudação: ')
hora_int = int(hora_str)

if hora_int >= 0 and hora_int <= 11:
    print("Bom dia!")
elif hora_int >= 12 and hora_int <= 17:
    print("Boa tarde!")
else:
    print("Boa noite!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_user = input("Digite seu nome: ")

# Calcula o comprimento do nome
tamanho_nome = len(nome_user)

# Verifica o tamanho do nome e imprime a mensagem correspondente
if tamanho_nome <= 4:
    print("Seu nome é curto.")
elif 5 <= tamanho_nome <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
