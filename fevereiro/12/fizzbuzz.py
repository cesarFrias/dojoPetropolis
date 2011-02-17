# -*- coding: utf-8 -*-

def fizzbuzz(entrada):
    if entrada % 15 == 0:
        return "fizzbuzz"
    elif entrada % 3 == 0:
        return "fizz"
    elif entrada % 5 == 0:
        return "buzz"
    else:
        return entrada
