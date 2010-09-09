# coding: utf-8
from unittest import TestCase, main
from utils import eh_palindromo

class Test_Palindromo(TestCase):
	def teste_1_eh_palindromo(self):
		entrada = 1
		self.assertTrue(eh_palindromo(entrada))

	def teste_13_eh_palindromo(self):
		entrada = 13 
		self.assertFalse(eh_palindromo(entrada))

	def teste_22_eh_palindromo(self):
		entrada = 22 
		self.assertTrue(eh_palindromo(entrada))

	def teste_117_eh_palindromo(self):
		entrada = 117 
		self.assertFalse(eh_palindromo(entrada))

	def teste_171_eh_palindromo(self):
		entrada = 171 
		self.assertTrue(eh_palindromo(entrada))

	def teste_1177_eh_palindromo(self):
		entrada = 1177 
		self.assertFalse(eh_palindromo(entrada))

	def teste_1771_eh_palindromo(self):
		entrada = 1771 
		self.assertTrue(eh_palindromo(entrada))

if __name__ == '__main__':
	main()
