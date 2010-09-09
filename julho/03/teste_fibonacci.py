# coding: utf-8
from unittest import TestCase, main
from utils import sequencia_fibonacci

class Test_Fibonacci(TestCase):
	def teste_nenhum_elemento(self):
		entrada = 0
		resultado_esperado = []
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_1_elemento(self):
		entrada = 1
		resultado_esperado = [1,]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_2_elementos(self):
		entrada = 2
		resultado_esperado = [1, 1]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_3_elementos(self):
		entrada = 3
		resultado_esperado = [1, 1, 2]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_4_elementos(self):
		entrada = 4
		resultado_esperado = [1, 1, 2, 3]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_5_elementos(self):
		entrada = 5
		resultado_esperado = [1, 1, 2, 3, 5]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_6_elementos(self):
		entrada = 6
		resultado_esperado = [1, 1, 2, 3, 5, 8]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_7_elementos(self):
		entrada = 7
		resultado_esperado = [1, 1, 2, 3, 5, 8, 13]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_8_elementos(self):
		entrada = 8
		resultado_esperado = [1, 1, 2, 3, 5, 8, 13, 21]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_9_elementos(self):
		entrada = 9
		resultado_esperado = [1, 1, 2, 3, 5, 8, 13, 21, 34]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

	def teste_10_elementos(self):
		entrada = 10
		resultado_esperado = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
		self.assertEqual(resultado_esperado, sequencia_fibonacci(entrada))

if __name__ == '__main__':
	main()
