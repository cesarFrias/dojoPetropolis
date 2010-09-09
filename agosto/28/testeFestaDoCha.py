# -*- coding: utf-8 -*-

from unittest import TestCase, main
from festaDoCha import bem_vindo

class TestFestaDoCha(TestCase):

	def teste_homem_solteiro_miguel(self):
		nome = 'Miguel'
		sexo = 'masculino'
		estado_civil = 'solteiro'
		esperado = 'bem vindo, senhor Miguel'
		retornado = bem_vindo (nome, sexo, estado_civil)
		self.assertEqual( esperado, retornado )

	def teste_mulher_solteira_lucia(self):
		nome = 'Lucia'
		sexo = 'feminino'
		estado_civil = 'solteira'
		esperado = 'bem vinda, senhorita Lucia'
		retornado = bem_vindo (nome, sexo, estado_civil)
		self.assertEqual( esperado, retornado )

	def teste_homem_solteiro_jefferson(self):
		nome = 'Jefferson'
		sexo = 'masculino'
		estado_civil = 'solteiro'
		esperado = 'bem vindo, senhor Jefferson'
		retornado = bem_vindo (nome, sexo, estado_civil)
		self.assertEqual( esperado, retornado )

	def teste_mulher_casada_lucia(self):
		nome = 'Lucia'
		sexo = 'feminino'
		estado_civil = 'casada'
		esperado = 'bem vinda, senhora Lucia'
		retornado = bem_vindo (nome, sexo, estado_civil)
		self.assertEqual( esperado, retornado )

	def teste_mulher_casada_luciana(self):
		nome = 'Luciana'
		sexo = 'feminino'
		estado_civil = 'casada'
		esperado = 'bem vinda, senhora Luciana'
		retornado = bem_vindo (nome, sexo, estado_civil)
		self.assertEqual( esperado, retornado )

	def teste_homem_casado_cesar(self):
		nome = 'Cesar'
		sexo = 'masculino'
		estado_civil = 'casado'
		esperado = 'bem vindo, senhor Cesar'
		retornado = bem_vindo (nome, sexo, estado_civil)
		self.assertEqual( esperado, retornado )

	def teste_mulher_solteira_pamela(self):
		nome = 'Pamela'
		sexo = 'feminino'
		estado_civil = 'solteira'
		esperado = 'bem vinda, senhorita Pamela'
		retornado = bem_vindo (nome, sexo, estado_civil)
		self.assertEqual( esperado, retornado )

	def teste_mulher_casada_Ana(self):
		nome = 'Ana'
		sexo = 'feminino'
		estado_civil = 'casada'
		esperado = 'bem vinda, senhora Ana'
		retornado = bem_vindo (nome, sexo, estado_civil)
		self.assertEqual( esperado, retornado )

if __name__ == '__main__':
	main()
