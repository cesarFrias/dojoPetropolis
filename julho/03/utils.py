def sequencia_fibonacci(quantidade):
	a, b = 1, 1
	lista = list()
	for i in xrange(quantidade):
		lista.append(a)
		a, b = b, a + b

	return lista

def eh_palindromo(numero):
	aux = numero
	inverso = 0
	while aux > 0:
		inverso *= 10
		inverso += aux % 10
		aux //= 10

	return numero == inverso

