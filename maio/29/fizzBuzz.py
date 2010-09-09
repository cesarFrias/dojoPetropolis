# coding: utf-8

def fizzbuzz(numero):
	if divide_por_3(numero) and divide_por_5(numero):
		return 'fizzbuzz'	
	elif divide_por_3(numero):
		return "fizz"
	elif divide_por_5(numero):
		return 'buzz'
	else:
		return numero


def divide_por_5(numero):
	return numero % 5 == 0		

def divide_por_3(numero):
	return numero % 3 == 0
		
