#Programado por Gabriel Giffron da Costa Silva (Estudante de Ciencias da Computacao da Universidade Anhanguera, Uberlandia-MG) (01/09/2023)

# Conversor de Moedas em Tempo Real com base nas taxas de transição do Forex

from forex_python.converter import CurrencyRates

# Crie uma instância do CurrencyRates
c = CurrencyRates()
choice = None

while True:
    
    # Solicitar a quantia e a moeda de origem
    amount = float(input("\nDigite a quantia em moeda de origem: "))

    from_currency = input("Digite a moeda de origem (por exemplo, USD, EUR, JPY): ").upper()

    # Solicitar a moeda de destino
    to_currency = input("Digite a moeda de destino (por exemplo, BRL, GBP, AUD): ").upper()

    # Use a biblioteca para obter a taxa de câmbio atual
    conversion_rate = c.get_rate(from_currency, to_currency)

    # Calcule a quantia equivalente na moeda de destino
    converted_amount = amount * conversion_rate

    # Exiba o resultado
    print(f"\n{amount} {from_currency} é equivalente a {converted_amount:.2f} {to_currency}")

    # Pergunte ao usuário se deseja continuar ou sair
    
    choice = input("\nDeseja fazer outra conversão (S/N)? ").upper()
    if choice != 'S':
        break