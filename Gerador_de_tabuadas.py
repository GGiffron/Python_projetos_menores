#Programado por Gabriel Giffron da Costa Silva (Estudante de Ciencias da Computacao da Universidade Anhanguera, Uberlandia-MG) (01/09/2023)

"""
Exercicio Reciclado da minha lista de Exercicios em C 

4. Faca um algoritmo que calcule e mostre a tabuada de (+, -, * e /) de um numero digitado pelo usuario.
OBS: Quando se calcula em uma substracao um numero menor de um numero maior (ex:3 - 10) o resultado sera um numero negativo.
Pesquise como desprezar o sinal negativo para sempre termos um numero positivo

"""

numero = int(input("Informe o numero para o calculo da tabuada: "))

#Tabuada de soma e subtracao

print (f"Tabuada de + e - para o numero {numero}:")

for x in range (0, 9):

    print(f"{numero} + {x} = {numero+x}                 {numero} - {x} = {abs(numero - x)}")

#Tabuada de multiplicacao e divisao

for x in range (0,9):

    if x == 0:
        print(f"{numero} * {x} = {numero*x}              {numero} / {x} = não existe quociente")

    elif x > 0:
        print(f"{numero} * {x} = {numero*x}              {numero} / {x} = {numero/x:,.2f}")