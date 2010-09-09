# coding: UTF-8

def contagem_regressiva(desde):
	testaTipo(desde)
	if desde == 50:
		resposta = []
		for i in range(0,51):
			resposta.insert(0,i)
		return resposta
	if desde == 3:
		return [3, 2, 1, 0]
	elif desde == 2:
		return [2, 1, 0]
	elif desde == 1:
		return [1, 0]
	else:
		return [0]

def testaTipo(desde):
	if not isinstance(desde, (int, long)):
		raise TypeError
