# Version 21 Febrero 2023
# incluir path de carpetas 
import sys
sys.path.append('AlcanceMinimo')
sys.path.append('AlcanceInteractivo') 

#librerias necesarias para este modulo
import time
import os
import BuscaAlcanceMinimo

# #################################################
# # Nudos de Lissajous
# # HACE TANTOS NUDOS COMO QUIERO
# # 1 nudo por default
# # Puntos por default en  la parametrizacion: 500 
# # Ternas.txt
# #################################################

start = time.process_time()
BuscaAlcanceMinimo.HazNudos(cantidad_de_nudos=2, intervalos = 500)
end = time.process_time()
print('Ejecución en:', end - start)


