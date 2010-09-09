# -*- coding: utf-8 -*-

def bem_vindo(nome, sexo, estado_civil):
	if sexo == 'masculino':
		return 'bem vindo, senhor {0}'.format( nome )
		'''
		if nome == 'Miguel':
			return "bem vindo, senhor Miguel"
		if nome == 'Cesar':
			return "bem vindo, senhor Cesar"
		else:
			return "bem vindo, senhor Jefferson"
		'''
	elif estado_civil == 'casada':
		return 'bem vinda, senhora {0}'.format( nome )
		'''
		if nome == "Luciana":
			return 'bem vinda, senhora Luciana'
		else:
			return 'bem vinda, senhora Lucia'
		'''
	else:
		return 'bem vinda, senhorita {0}'.format( nome )
		#return 'bem vinda, senhorita Lucia'

