# Version 14 de Febrero
# Alcance por esferas del nudo simple

import numpy as np

#Acota alcance
def acotaAlcancePorEsferas(Nudo, intervalos, iteraciones):
	#Alcance inicial
	Pesos = []
	AlcancesPuntuales = []
	Aumentos = []
	autointerseccion = False
	i=0
	print('iteracion 1, buscando alcances iniciales')
	for i in range(intervalos):
		#los vecinos

		h = ( i - 1 )%intervalos
		j = ( i + 1 )%intervalos

		#Mide distancia a sus vecinos más proximos
		distancia1 = np.linalg.norm( Nudo[i] - Nudo[h] ) 
		distancia2 = np.linalg.norm( Nudo[i] - Nudo[j] )
		maximo = min(distancia1, distancia2)
		
		#Busca saturacion
		M = { h, i, j }
		peso = 0
		distancias = []

		for indice in range(intervalos):
			if indice not in M:
				distanciaIndice = np.linalg.norm( Nudo[i] - Nudo[indice] )
				if  distanciaIndice < maximo:
					peso = peso+1
					distancias.append(distanciaIndice)

		if peso == 0:
			alcance_i = maximo/2
			Aumentos.append(False)
		else:
			alcance_i = min(distancias)/2
			Aumentos.append(True)
			if alcance_i == 0.0:
				autointerseccion = True
				return AlcancesPuntuales,Aumentos, autointerseccion

		AlcancesPuntuales.append(alcance_i)		
		Pesos.append(peso)

	#Si no sirve el nudo por autointerseccion, acá termina
	if True in Aumentos:
		return AlcancesPuntuales, Aumentos, autointerseccion

	A2 = AlcancesPuntuales.copy()
	################	
	################

	radios = []
	for i in range(2, iteraciones):
		radios.append(i)

	for radio in radios:
		print('iteracion: ', radio)
		for i in range(intervalos):
			#Va a calcular la distancia permitida
			#M es el radio que va a excluir
			M={i}
			for a in range(radio):
				M.update( [(i-a)%intervalos, (i+a)%intervalos ])

			D = []
			for m in M:
				if m != i:
					#esto puede mejorar
					distancia_i_m = np.linalg.norm( Nudo[i] - Nudo[m] )
					D.append( distancia_i_m )

			maximo = max(D)
			###############

			peso = 0
			distancias = []

			#Distancias a todo el nudo
			for indice in range(intervalos):
				if (indice not in M) and (Aumentos[indice] != True):
					#esto puede mejorar
					distanciaIndice = np.linalg.norm( Nudo[i] - Nudo[indice] )
					if  distanciaIndice <= maximo:
						peso = peso+1
						distancias.append(distanciaIndice)

			if peso == 0:
				alcance_i = maximo/3
				Aumentos [indice]= False
			else:
				d = min(distancias)
				alcance_i = d/3
				Aumentos[indice] = True
			AlcancesPuntuales[i] = alcance_i		
			Pesos = peso
	if autointerseccion == True:
		print("no deberia pasar---------------------")

	return AlcancesPuntuales, Aumentos, autointerseccion

