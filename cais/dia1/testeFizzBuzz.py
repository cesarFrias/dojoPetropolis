# -*- coding: utf-8 -*-

from FizzBuzz import fizzbuzz
from unittest import TestCase, main

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
		esperado = "Fizz"
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_4(self):
		entrada = 4
		esperado = 4
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_5(self):
		entrada = 5
		esperado = "Buzz"
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_6(self):
		entrada = 6
		esperado = "Fizz"
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
		esperado = "Fizz"
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_10(self):
		entrada = 10
		esperado = "Buzz"
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)

	def teste_entrada_15(self):
		entrada = 15
		esperado = "Fizzbuzz"
		retornado = fizzbuzz(entrada)
		self.assertEqual(esperado, retornado)


	
if __name__ == "__main__":
	main()
