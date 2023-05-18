
from lealNumeros import LealNumerosAPI

# Put punctuation in numbers
print(LealNumerosAPI.numerosPontuados(10000))
# Output: 10.000

# Put symbols
        # Available formats: (8)    Mil
        #                           M (Million)
        #                           B (Billion)
        #                           T (Trillion)
        #                           Q (Quadrillion)
        #                           Qi (Quintillion)
        #                           Sx (Sextillion)
        #                           Sp (Septillion)
print(LealNumerosAPI.numerosSimbolos(10000))
# Output: 10Mil

# Write the name of the number (EXCLUSIVE: portuguese-brazil)
print(LealNumerosAPI.numerosNome(100, lang='pt-br')) # (en) example lang:
#     LealNumerosAPI.numerosNome(100, lang='en')
# Output: Cem (pt-br)
# Output: One hundred (en)

# Write differences between numbers
print(LealNumerosAPI.numerosDiferenca(5, 10))
# Output: 5

# Write differences between days
print(f'{LealNumerosAPI.dataDiferenca(1, 2, 2023)} Days')

# Calculator
account = input('What is the mathematical account? (ex .: 10 + 5)')
result = LealNumerosAPI.numerosCalculadora(account)
print(result)
