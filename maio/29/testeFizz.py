# coding: utf-8
from unittest import TestCase, main

from fizzBuzz import fizzbuzz

class Test_FizzBuzz(TestCase):
	
	def test_retorna_fizz_modulo_0(self):
		numero = 0
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'fizzbuzz')

	def test_retorna_fizz_modulo_1(self):
		numero = 1
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 1)

	def test_retorna_fizz_modulo_2(self):
		numero = 2
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 2)

	def test_retorna_fizz_modulo_3(self):
		numero = 3
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'fizz')

	def test_retorna_fizz_modulo_4(self):
		numero = 4
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 4)

	def test_retorna_fizz_modulo_5(self):
		numero = 5
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'buzz')

	def test_retorna_fizz_modulo_6(self):
		numero = 6
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'fizz')

	def test_retorna_fizz_modulo_7(self):
		numero = 7
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 7)

	def test_retorna_fizz_modulo_8(self):
		numero = 8
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 8)

	def test_retorna_fizz_modulo_9(self):
		numero = 9
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'fizz')
	
	def test_retorna_fizz_modulo_10(self):
		numero = 10
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'buzz')

	def test_retorna_fizz_modulo_12(self):
		numero = 12
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'fizz')

	def test_retorna_fizz_modulo_15(self):
		numero = 15
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'fizzbuzz')

	def test_retorna_fizz_modulo_20(self):
		numero = 20
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'buzz')

	def test_retorna_fizz_modulo_30(self):
		numero = 30
		resultado = fizzbuzz(numero)
		self.assertEqual(resultado, 'fizzbuzz')

if __name__ == "__main__":
	main()
