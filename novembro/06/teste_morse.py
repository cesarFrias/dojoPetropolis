# coding: utf-8
from unittest import TestCase, main
from Morse import morse

class TestMorse(TestCase):
    
    def test_retorna_U(self):
        entrada = '..-'
        esperado = 'U'
        retornado = morse(entrada)
        self.assertEqual(retornado, esperado)
    
    def test_retorna_A(self):
        entrada = '.-'
        esperado = 'A'
        retornado = morse(entrada)
        self.assertEqual(retornado, esperado)

    def test_retorna_C(self):
        entrada = '-.-.'
        esperado = 'C'
        retornado = morse(entrada)
        self.assertEqual(retornado, esperado)

    def test_retorna_B(self):
        entrada = '-...'
        esperado = 'B'
        retornado = morse(entrada)
        self.assertEqual(retornado, esperado)

    def test_retorna_AB(self):
        entrada = '.-|-...'
        esperado = 'AB'
        retornado = morse(entrada)
        self.assertEqual(retornado, esperado)

    def test_retorna_CU(self):
        entrada = '-.-.|..-'
        esperado = 'CU'
        retornado = morse(entrada)
        self.assertEqual(retornado, esperado)

    def test_retorna_CASA(self):
        entrada = '-.-.|.-|...|.-'
        esperado = 'CASA'
        retornado = morse(entrada)
        self.assertEqual(retornado, esperado)

    def test_retorna_PARALELEPIPEDO(self):
        entrada = '.--.|.-|.-.|.-|.-..|.|.-..|.|.--.|..|.--.|.|-..|---'
        esperado = 'PARALELEPIPEDO'
        retornado = morse(entrada)
        self.assertEqual(retornado, esperado)

if __name__ == '__main__':
	main()
