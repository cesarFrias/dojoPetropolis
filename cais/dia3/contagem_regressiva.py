# coding: utf-8

def regressiva( numero_entrada ):
    if not isinstance(numero_entrada, (int, long)):
		raise TypeError
    else:
        if numero_entrada < 0:
            raise ValueError("O numero passado e negativo")
        else:    
            numero_entrada+=1
            lista = range(numero_entrada)
            lista.reverse()
        return lista








    """if numero_entrada  == 1:
        return [1, 0]
    elif numero_entrada == 2:
        return [2, 1, 0]
    elif numero_entrada == 3:    
        return [3, 2, 1, 0]
    elif numero_entrada == 4:        
        return [4, 3, 2, 1, 0]
    else:
        return [5, 4, 3, 2, 1, 0]"""



