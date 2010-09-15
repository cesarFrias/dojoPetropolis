# coding: utf-8

def fizzbuzz(entrada):
	if entrada%15 == 0:
		return "FIZZBUZZ"
	elif entrada%5 == 0:
		return "BUZZ"
	elif entrada %3 == 0:
		return "FIZZ"
	else:
		return entrada



	"""
	if entrada==3 or entrada==6:
		return "FIZZ"
	elif entrada==5 or entrada==50 or entrada==20:
		return "BUZZ"
	elif entrada==15 or entrada==30 or entrada == :
		return "FIZZBUZZ"
	else:
		return entrada
	"""




if __name__ == "__main__":
	main()
