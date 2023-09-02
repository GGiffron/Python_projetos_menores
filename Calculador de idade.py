#Programado por Gabriel Giffron da Costa Silva (Estudante de Ciencias da Computacao da Universidade Anhanguera, Uberlandia-MG) (01/09/2023)

import datetime

# Solicita ao usuário o ano de nascimento

ano_nascimento = int(input("Digite o ano de nascimento: "))

# Obtem o ano atual

ano_atual = datetime.datetime.now().year

# Calcula a idade

idade = ano_atual - ano_nascimento

# Exibe a idade

print(f"Sua idade atual é {idade} anos.")