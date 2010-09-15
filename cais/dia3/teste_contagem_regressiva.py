# coding: utf-8
from unittest import TestCase, main
from contagem_regressiva import regressiva

class Test_contagem_Regressiva(TestCase):
    def teste_entrada_1(self):
        entrada = 1
        saida_esperada = [1, 0]
        recebido = regressiva( entrada )
        self.assertEquals(recebido, saida_esperada) 

    def teste_entrada_2(self):
        entrada = 2
        saida_esperada = [2, 1, 0]
        recebido = regressiva( entrada  )
        self.assertEquals(recebido, saida_esperada) 

    def teste_entrada_3(self):
        entrada = 3
        saida_esperada = [3, 2, 1, 0]
        recebido = regressiva( entrada  )
        self.assertEquals(recebido, saida_esperada)    

    def teste_entrada_4(self):
        entrada = 4
        saida_esperada = [4, 3, 2, 1, 0]
        recebido= regressiva( entrada )
        self.assertEquals(recebido, saida_esperada)

    def teste_entrada_5(self):
        entrada = 5
        saida_esperada = [5, 4, 3, 2, 1, 0]
        recebido = regressiva(entrada)
        self.assertEquals(recebido, saida_esperada) 

    def teste_entrada_5_negativo(self):
        entrada = -5
        self.assertRaises(ValueError, regressiva, entrada)   

    def teste_entrada_5_string(self):
        entrada = '5'
        self.assertRaises(TypeError, regressiva, entrada) 

if __name__ == "__main__":
	main()

