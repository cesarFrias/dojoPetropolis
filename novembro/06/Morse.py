# -*- coding: utf-8 -*-

DICIONARIO_MORSE = {
    '.-'   : 'A',
    '-...' : 'B',
    '-.-.' : 'C',
    '-..'  : 'D',
    '.'    : 'E',
    '..-.' : 'F',
    '--.'  : 'G',
    '....' : 'H',
    '..'   : 'I',
    '.---' : 'J',
    '-.-'  : 'K',
    '.-..' : 'L',
    '---'  : 'M',
    '-.'   : 'N',
    '---'  : 'O',
    '.--.' : 'P',
    '--.-' : 'Q',
    '.-.'  : 'R',
    '...'  : 'S',
    '-'    : 'T',
    '..-'  : 'U',
    '...-' : 'V',
    '.--'  : 'W',
    '-..-' : 'X',
    '-.--' : 'Y',
    '--..' : 'Z',
}

SEPARADOR = '|'

def morse(entrada):
    if SEPARADOR in entrada:
        retorno = str()
        letras = entrada.split(SEPARADOR)
        for letra in letras:
            if letra in DICIONARIO_MORSE:
                retorno += DICIONARIO_MORSE[letra]
    else:
        retorno = DICIONARIO_MORSE[entrada]
    
    return retorno
