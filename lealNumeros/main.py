from num2words import num2words
from datetime import datetime
from translate import Translator


# CHANGELOGS -> https://discord.com/invite/394ChkbKrt
# 0.0.6 - Added multiple languages
# 0.0.5 - Added function to calculate (add, subtract, multiply and divide)
# 0.0.5 - Added function to compare days (by date: day/month/year)
# 0.0.4 - Added function to compare difference between numbers.
#
# PYPI LINK: https://pypi.org/project/lealnumeros/
class LealNumerosAPI():

    # (pt-br) Exemplo: 1.100.100 | 1.000
    # (en) Example: 1.100.100 | 1.000
    def numerosPontuados(numero):
        numero_str = str(numero)
        quantia_letras = len(numero_str)

        numeros = []
        for i, letra in enumerate(numero_str[::-1]):
            if i % 3 == 0 and i != 0:
                numeros.append('.')
            numeros.append(letra)
        
        numero_formatado = ''.join(numeros[::-1])
        return numero_formatado

    def numerosSimbolos(numero, lang = 'en'):

        if lang == 'pt-BR':
            traducao = Translator(to_lang=lang, from_lang='en')
            traducao_resultado = traducao.translate('Thousand').capitalize()
        else:
            traducao = Translator(to_lang=lang, from_lang='pt-br')
            traducao_resultado = traducao.translate('mil').capitalize()

        numero_str = str(numero)
        quantia_letras = len(numero_str)

        # PT-BR
        # Formatos disponíveis: (8) Mil
        #                           M (Milhão)
        #                           B (Bilhão)
        #                           T (Trilhão)
        #                           Q (Quadrilhão)
        #                           Qi (Quintilhão)
        #                           Sx (Sextilhão)
        #                           Sp (Septilhão)
        
        if quantia_letras <= 3:
            numero_formatado = numero_str

        elif quantia_letras <= 6:
            if numero_str[:-3] == '1':
                numero_formatado = f'{traducao_resultado}'
            else:
                numero_formatado = f'{numero_str[:-3]}{traducao_resultado}'
            

        elif quantia_letras <= 9:
            numero_formatado = f'{numero_str[:-6]}M'

        elif quantia_letras <= 12:
            numero_formatado = f'{numero_str[:-9]}B'

        elif quantia_letras <= 15:
            numero_formatado = f'{numero_str[:-12]}T'

        elif quantia_letras <= 18:
            numero_formatado = f'{numero_str[:-15]}Q'

        elif quantia_letras <= 21:
            numero_formatado = f'{numero_str[:-18]}Qi'

        elif quantia_letras <= 24:
            numero_formatado = f'{numero_str[:-21]}Sx'

        else:
            numero_formatado = f'{numero_str[:-24]}Sp'
            
        return numero_formatado

    def numerosNome(numero, lang = 'pt-BR'):
        numero_nome = num2words(numero, lang=lang)
        numero_nome = numero_nome.capitalize()

        return numero_nome

    def numerosDiferenca(numero_um, numero_dois):
        if numero_um > numero_dois: # Se o 'numero_um' for maior que o 'numero_dois'
            resposta = numero_um - numero_dois

        elif numero_um < numero_dois: # Se o 'numero_dois' for maior que o 'numero_um'
            resposta = numero_dois - numero_um

        else:
            resposta = 0 # Caso os números forem iguais.

        return 

    def numerosCalculadora(conta):

        # Simplificar para quem utilizar
        conta = conta.split()

        numero_um = int(conta[0])
        operador = str(conta[1])
        numero_dois = int(conta[2])

        # Código...
        operadores = ['+','-','*','/']

        if operador in operadores: # teste
            if operador == '+':
                resultado = numero_um + numero_dois
            elif operador == '-':
                resultado = numero_um - numero_dois
            elif operador == '*':
                resultado = numero_um * numero_dois
            elif operador == '/':
                resultado = numero_um / numero_dois

            return resultado
            
        else:
            return 'Operator not found.'

    # Verificar a diferença de dias.
    def dataDiferenca(dia, mes, ano):
        formato = '%d/%m/&Y'
        data_registrada = datetime.strptime(f'{int(dia)}/{int(mes)}/{int(ano)}', '%d/%m/%Y') # Pegar a data da ação (registro, punição e ect...)
        data_atual = datetime.now() # Pegar data atual (quando o código acontecer)

        dia = str(data_atual - data_registrada)

        return dia[:3]