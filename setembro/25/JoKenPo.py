# coding: utf-8

__all__ = ['jokenpo']


dict_jokenpo = {
	'pedra': 0,
	'papel': 1,
	'tesoura': 2,
}


def jokenpo(jogador1, jogador2):
	jogador1 = dict_jokenpo[jogador1]
	jogador2 = dict_jokenpo[jogador2]

	ganhador = (jogador1 - jogador2) % 3

	return "jogador{0}".format(ganhador) if ganhador else "empate"

'''	
	if jogador1 == 'pedra':
		if jogador2 == 'papel':
			return 'jogador2'
		elif jogador2 == 'tesoura':
			return 'jogador1'

	elif jogador1 == "papel":
		if jogador2 == "pedra":
			return 'jogador1'
		elif jogador2 == "tesoura":
			return 'jogador2'

	elif jogador1 == "tesoura":
		if jogador2 == "pedra":
			return 'jogador2'
		elif jogador2 == "papel":
			return 'jogador1'

	return 'empate'
'''
