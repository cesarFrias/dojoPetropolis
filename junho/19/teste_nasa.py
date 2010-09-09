# coding: utf-8
from unittest import TestCase, main
from utils import contagem_regressiva

class Test_Nasa(TestCase):
			
	def test_de_0(self):
		entrada = 0
		resultado_esperado = [0]
		self.assertEqual(contagem_regressiva(entrada), resultado_esperado)
	
	def test_de_1_a_0(self):
		entrada = 1
		resultado_esperado = [1, 0]
		self.assertEqual(contagem_regressiva(entrada), resultado_esperado)
	
	def test_de_2_a_0(self):
		entrada = 2
		resultado_esperado = [2, 1, 0]
		self.assertEqual(contagem_regressiva(entrada), resultado_esperado)
	
	def test_de_3_a_0(self):
		entrada = 3
		resultado_esperado = [3, 2, 1, 0]
		self.assertEqual(contagem_regressiva(entrada), resultado_esperado)

	def test_de_12_a_0(self):
		entrada = 12
		resultado_esperado = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
		self.assertEqual(contagem_regressiva(entrada), resultado_esperado)
	

if __name__ == '__main__':
	main()
