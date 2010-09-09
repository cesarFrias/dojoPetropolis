# coding: utf-8
from unittest import TestCase, main
from telefone import frase_para_numero

class Test_telefone(TestCase):
	def test_entrada_A_saida_2(self):
		entrada = 'A'
		saida = 2
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_a_saida_2(self):
		entrada = 'a'
		saida = 2
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_B_saida_2(self):
		entrada = 'B'
		saida = 2
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_C_saida_2(self):
		entrada = 'C'
		saida = 2
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_d_saida_3(self):
		entrada = 'D'
		saida = 3
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_D_saida_3(self):
		entrada = 'd'
		saida = 3
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_E_saida_3(self):
		entrada = 'E'
		saida = 3
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_F_saida_3(self):
		entrada = 'F'
		saida = 3
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_G_saida_4(self):
		entrada = 'G'
		saida = 4
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_H_saida_4(self):
		entrada = 'H'
		saida = 4
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_I_saida_4(self):
		entrada = 'I'
		saida = 4
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_K_saida_5(self):
		entrada = 'K'
		saida = 5
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_o_saida_6(self):
		entrada = 'o'
		saida = 6
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_S_saida_7(self):
		entrada = 'S'
		saida = 7
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_v_saida_8(self):
		entrada = 'v'
		saida = 8
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_z_saida_9(self):
		entrada = 'z'
		saida = 9
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_aD_saida_23(self):
		entrada = 'aD'
		saida = 23
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_aDw_saida_239(self):
		entrada = 'aDw'
		saida = 239
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_aDwI_saida_2394(self):
		entrada = 'aDwI'
		saida = 2394
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_aDwIJic_saida_2394542(self):
		entrada = 'aDwIJic'
		saida = 2394542
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_MYMISERABLEJOB_saida_69647372253562(self):
		entrada = 'MYMISERABLEJOB'
		saida = 69647372253562
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_outro_MYMISERABLEJOB_saida_69647372253562(self):
		entrada = 'MY-MISERABLE-JOB'
		saida = '69-647372253-562'
		self.assertEqual(str(saida), frase_para_numero(entrada))

	def test_entrada_com_caracter_invalido(self):
		entrada = 'qwer#'
		saida = 'Caracter invalido #'
		self.assertEqual(saida, frase_para_numero(entrada))
	
if __name__ == '__main__':
	main()
