from unittest import TestCase, main
from fizzbuzz import fizzbuzz

class TesteFizzBuzz(TestCase):
    def teste_numero_1_retorna_1(self):
        entrada = 1
        valor_esperado = 1
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_2_retorna_2(self):
        entrada = 2
        valor_esperado = 2
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_3_retorna_fizz(self):
        entrada = 3
        valor_esperado = "fizz"
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_4_retorna_4(self):
        entrada = 4
        valor_esperado = 4
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_5_retorna_buzz(self):
        entrada = 5
        valor_esperado = "buzz"
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_6_retorna_fizz(self):
        entrada = 6
        valor_esperado = "fizz"
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_7_retorna_7(self):
        entrada = 7
        valor_esperado = 7
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_8_retorna_8(self):
        entrada = 8
        valor_esperado = 8
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_9_retorna_9(self):
        entrada = 9
        valor_esperado = "fizz"
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_10_retorna_10(self):
        entrada = 10
        valor_esperado = "buzz"
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_11_retorna_11(self):
        entrada = 11
        valor_esperado = 11
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_12_retorna_fizz(self):
        entrada = 12
        valor_esperado = "fizz"
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_13_retorna_13(self):
        entrada = 13
        valor_esperado = 13
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_numero_15_retorna_fizzbuzz(self):
        entrada = 15
        valor_esperado = "fizzbuzz"
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

    def teste_entrada_1200_retorna_fizzbuzz(self):
        entrada = 1200
        valor_esperado = "fizzbuzz"
        self.assertEqual(valor_esperado,fizzbuzz(entrada))

    def teste_entrada_0_returna_fizzbuzz(self):
        entrada = 0
        valor_esperado = "fizzbuzz"
        self.assertEqual(valor_esperado, fizzbuzz(entrada))

if __name__ == '__main__':
    main()
