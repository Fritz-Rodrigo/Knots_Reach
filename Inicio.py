# Version 4 de marzo 2023
# incluir path de carpetas 
import sys
sys.path.append('AlcanceInicial')
sys.path.append('AlcanceInteractivo') 

#librerias necesarias para este modulo
import time
import os
import random
import BuscaAlcanceMinimo
import ConstruyeNudo


# #################################################
# # Nudos de Lissajous
# # HACE TANTOS NUDOS COMO QUIERO
# # 1 nudo por default
# # Puntos por default en  la parametrizacion: 500 
# # Ternas.txt
# #################################################

  

def Rutina(Indices = [100], intervalos = 3000, iteraciones = 5, Fases = [[0,0,0]], umbral=0.001):
	start = time.process_time()
	for indice in Indices:
		for fase in Fases:
			print('---------------------------------')
			print('Indice en el archivo Ternas.txt: ', indice)

			RutaNudo, RutaAlcances, RutaAumentos, sirve= BuscaAlcanceMinimo.HazNudos(indice=indice,
																				intervalos = intervalos,
																				iteraciones = iteraciones,
																				Fase = fase,
																				umbral = umbral)
			if sirve:
				RutaSalida ='Nudos/Inflados/'
				ConstruyeNudo.AlcanceInteractivo(RutaNudo, 
											RutaAlcances, 
											RutaAumentos,
											RutaSalida, 
											iteraciones)
	end = time.process_time()
	print('Ejecución en:', end - start)



def main():
    Rutina(Indices = [1, 50, 100 ],
    	intervalos = 1000,
    	iteraciones = 15,
    	Fases = [[1,1,0]],
    	umbral = 0.002)
    #trabajar caso 0.001

if __name__ == "__main__":
    main()

