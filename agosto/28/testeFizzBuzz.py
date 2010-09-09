# -*- coding: utf-8 -*-

from unittest import TestCase, main
from FizzBuzz import fizzbuzz 

class TestFizzBuzz(TestCase):

	def teste_entrada_1(self):
		entrada = 1
		esperado = 1
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_2(self):
		entrada = 2
		esperado = 2
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_3(self):
		entrada = 3
		esperado = 'fizz'
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_4(self):
		entrada = 4
		esperado = 4
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_5(self):
		entrada = 5
		esperado = 'buzz'
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_6(self):
		entrada = 6
		esperado = 'fizz'
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_7(self):
		entrada = 7
		esperado = 7
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_8(self):
		entrada = 8
		esperado = 8
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_9(self):
		entrada = 9
		esperado = 'fizz'
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)
	
	def teste_entrada_10(self):
		entrada = 10
		esperado = 'buzz'
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_11(self):
		entrada = 11
		esperado = 11
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_12(self):
		entrada = 12
		esperado = 'fizz'
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_15(self):
		entrada = 15
		esperado = 'fizzbuzz'
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_30(self):
		entrada = 30
		esperado = 'fizzbuzz'
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_45(self):
		entrada = 45
		esperado = 'fizzbuzz'
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

if __name__ == "__main__":
	main()
