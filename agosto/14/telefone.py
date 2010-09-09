# coding: utf-8

def frase_para_numero(frase):
	frase = frase_para_maiusculo(frase)
	lista2 = ['A', 'B', 'C']
	lista3 = ['D', 'E', 'F']
	lista4 = ['G', 'H', 'I']
	lista5 = ['J', 'K', 'L']
	lista6 = ['M', 'N', 'O']
	lista7 = ['P', 'Q', 'R', 'S']
	lista8 = ['T', 'U', 'V']
	lista9 = ['W', 'X', 'Y', 'Z']
	lista_caracteres_adicionais = ['-', '1', '0']
	saida = str()

	for caracter in frase:
		if caracter in lista2:
			saida += '2'
		elif caracter in lista3:
			saida += '3'
		elif caracter in lista4:
			saida += '4'
		elif caracter in lista5:
			saida += '5'
		elif caracter in lista6:
			saida += '6'
		elif caracter in lista7:
			saida += '7'
		elif caracter in lista8:
			saida += '8'
		elif caracter in lista9:
			saida += '9'
		elif caracter in lista_caracteres_adicionais:
			saida += caracter
		else:
			return 'Caracter invalido %s' % caracter
	return saida

def frase_para_maiusculo(frase):
	return frase.upper()
