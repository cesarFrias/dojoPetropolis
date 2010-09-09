# coding: utf-8

def contagem_regressiva(desde):
	if desde == 0:
		return [0]
	else:
		retorno = contagem_regressiva(desde - 1)
		retorno.insert(0, desde)
		return retorno

def converte_romano(numero):
	if numero <= 0:
		raise ValueError
	if numero < 4:
		return "i" * numero
	elif numero == 4:
		return 'iv'
	elif 5 <= numero < 9:
		return 'v{0}'.format('i' * (numero - 5))
	else :
		return 'ix'


		
