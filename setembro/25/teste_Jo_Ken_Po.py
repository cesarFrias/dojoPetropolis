# coding: utf-8
from unittest import TestCase, main
from JoKenPo import jokenpo

class TestJoKenPo(TestCase):
	def teste_pedra_pedra(self):
		jogador1 = 'pedra'
		jogador2 = 'pedra'
		esperado = 'empate'
		resultado = jokenpo(jogador1, jogador2)

		self.assertEqual(esperado, resultado)
		
	def teste_pedra_papel(self):
		jogador1 = 'pedra'
		jogador2 = 'papel'
		esperado = 'jogador2'
		resultado = jokenpo(jogador1, jogador2)
		self.assertEqual(esperado, resultado)

	def teste_pedra_tesoura(self):
		jogador1 = 'pedra'
		jogador2 = 'tesoura'
		esperado = 'jogador1'
		resultado = jokenpo(jogador1, jogador2)
		self.assertEqual(esperado, resultado)

	def teste_papel_pedra(self):
		jogador1 = 'papel'
		jogador2 = 'pedra'
		esperado = 'jogador1'
		resultado = jokenpo(jogador1, jogador2)

		self.assertEqual(esperado, resultado)

	def teste_papel_papel(self):
		jogador1 = 'papel'
		jogador2 = 'papel'
		esperado = 'empate'
		resultado = jokenpo(jogador1, jogador2)

		self.assertEqual(esperado, resultado)
		
	def teste_papel_tesoura(self):
		jogador1 = 'papel'
		jogador2 = 'tesoura'
		esperado = 'jogador2'
		resultado = jokenpo(jogador1, jogador2)

		self.assertEqual(esperado, resultado)

	def teste_tesoura_pedra(self):
		jogador1 = 'tesoura'
		jogador2 = 'pedra'
		esperado = 'jogador2'
		resultado = jokenpo(jogador1, jogador2)

		self.assertEqual(esperado, resultado)

	def teste_tesoura_papel(self):
		jogador1 = 'tesoura'
		jogador2 = 'papel'
		esperado = 'jogador1'
		resultado = jokenpo(jogador1, jogador2)

		self.assertEqual(esperado, resultado)

	def teste_tesoura_tesoura(self):
		jogador1 = 'tesoura'
		jogador2 = 'tesoura'
		esperado = 'empate'
		resultado = jokenpo(jogador1, jogador2)

		self.assertEqual(esperado, resultado)

if __name__ == '__main__':
	main()
