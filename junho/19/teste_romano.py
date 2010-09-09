# coding: utf-8
from unittest import TestCase, main
from utils import converte_romano

#class Test_Romano(TestCase):
class StubTests(TestCase):
	def teste_0_em_romano(self):
		entrada = 0
		self.assertRaises (ValueError, converte_romano, entrada)

	def teste_negativo_em_romano(self):
		entrada = -1
		self.assertRaises (ValueError, converte_romano, entrada)

	def teste_1_em_romano(self):
		entrada = 1
		#resultado_esperado = "i"
		self.assertEqual(resultado_esperado, converte_romano(entrada))

	def teste_2_em_romano(self):
		entrada = 2
		resultado_esperado = "ii"
		self.assertEqual(resultado_esperado, converte_romano(entrada))

	def teste_3_em_romano(self):
		entrada = 3
		resultado_esperado = "iii"
		self.assertEqual(resultado_esperado, converte_romano(entrada))

	def teste_4_em_romano(self):
		entrada = 4
		resultado_esperado = "iv"
		self.assertEqual(resultado_esperado, converte_romano(entrada))

	def teste_5_em_romano(self):
		entrada = 5
		resultado_esperado = "v"
		self.assertEqual(resultado_esperado, converte_romano(entrada))

	def teste_6_em_romano(self):
		entrada = 6
		resultado_esperado = "vi"
		self.assertEqual(resultado_esperado, converte_romano(entrada))

	def teste_7_em_romano(self):
		entrada = 7
		resultado_esperado = "vii"
		self.assertEqual(resultado_esperado, converte_romano(entrada))

	def teste_8_em_romano(self):
		entrada = 8
		resultado_esperado = "viii"
		self.assertEqual(resultado_esperado, converte_romano(entrada))

	def teste_9_em_romano(self):
		entrada = 9
		resultado_esperado = "ix"
		self.assertEqual(resultado_esperado, converte_romano(entrada))


if __name__ == '__main__':
	main()
