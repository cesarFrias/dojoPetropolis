# coding: utf-8

def fizzbuzz(entrada):
	if entrada%3==0 and entrada%5==0:
		return "Fizzbuzz"
	elif entrada%3==0:
		return "Fizz"
	elif entrada%5==0:
		return "Buzz"
	else:
		return entrada

	#if entrada == 1:
	#	return 1
	#elif entrada == 2:
	#	return 2
	#elif entrada == 4:
	#	return 4 
	#elif entrada == 3 or entrada == 6 or entrada == 9:
	#	return "Fizz"
	#elif entrada == 7:
	#	return 7 
	#elif entrada == 8:
	#	return 8 
	#elif entrada == 11:
	#	return 11
	#else:
	#	return "Buzz"	


if __name__ == "__main__":
	pass
