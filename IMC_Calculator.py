# Calculadora de IMC_Feita por Gabriel Giffron da Costa Silva-Estudante de Ciências da Computação (01/09/2023)

#Apresentação

print("Olá! Gostaria de calcular o seu IMC?\n")

#Digite o seu peso

peso = float(input("Por favor digite seu peso em Kg: "))

#Digite a sua altura

altura = float(input("Por favor digite sua altura em metros: "))

#Cálculo e Resultado

IMC = peso/altura**2

if IMC <= 18.5:
    print(f"\nHora de tomar aquela proteina e ganhar massa! Seu IMC está abaixo do ideal, sendo de {IMC:,.1f}.\n")

elif IMC > 18.5 and IMC <= 25:

    print(f"\nUm mito! Seu IMC é {IMC:,.1f} sendo o ideal, ta de Parabéns!!\n")

elif IMC > 25 and IMC <= 29.9:

    print(f"\nDa umas caminhadas e tranquilo! Levemente acima do peso, seu IMC é {IMC:,.1f}.\n")

elif IMC > 30 and IMC <= 34.9:

    print(f"\nFica ligado! Fazer uns exercícios e moderar na alimentação! Seu IMC é {IMC:,.1f}! Obesidade Grau I.\n")

elif IMC > 35 and IMC <= 39.9:

    print(f"\nPRERIGO! Seu IMC é {IMC:,.1f}! Necessários cuidados mais apropriados com a saúde!\n")

elif IMC >= 40:

    (f"\nS.O.S!! Seu IMC é {IMC:,.1f}! Procure um médico e cuide de sua saúde!\n")


print("\nObrigado por usar esta calculadora!")