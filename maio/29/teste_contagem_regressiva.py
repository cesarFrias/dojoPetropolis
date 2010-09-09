# coding: utf-8
from unittest import TestCase, main
from contagem_regressiva import contagem_regressiva


class Test_contagem_Regressiva(TestCase):

	def test_nao_e_numero_levanta_erro(self):
		parametro = "nao e um numero"
		self.assertRaises(
			TypeError, contagem_regressiva, parametro)

	def test_nao_e_numero_levanta_erro_2(self):
		parametro = "12"
		self.assertRaises(
			TypeError, contagem_regressiva, parametro)

	def test_desde_0(self):
		parametro = 0
		resultado_esperado = [0]

		resultado = contagem_regressiva(parametro)
		self.assertEqual(resultado_esperado, resultado)


	def test_desde_1(self):
		parametro = 1
		resultado_esperado = [1, 0]

		resultado = contagem_regressiva(parametro)
		self.assertEqual(resultado_esperado, resultado)


	def test_desde_2(self):
		parametro = 2
		resultado_esperado = [2, 1, 0]

		resultado = contagem_regressiva(parametro)
		self.assertEqual(resultado_esperado, resultado)

	
	def test_desde_3(self):
		parametro = 3
		resultado_esperado = [3, 2, 1, 0]

		resultado = contagem_regressiva(parametro)
		self.assertEqual(resultado_esperado, resultado)

	def test_desde_50(self):
		parametro = 50
		resultado_esperado = []

		for numero in range(0,51):
			resultado_esperado.insert(0, numero)

		resultado = contagem_regressiva(parametro)
		self.assertEqual(resultado_esperado, resultado)



if __name__ == "__main__":
	main()

