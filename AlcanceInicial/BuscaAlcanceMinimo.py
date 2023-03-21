#Version 21-Febrero 2023
import numpy as np
##########################
import FuncionesAuxiliares
from AlcancePorEsferas import acotaAlcancePorEsferas as acotaAlcancePorEsferas


##############################################################
#    Verifica que el nudo
# 1) No tenga puntos repetidos 
# 2) Tenga alcance aceptable, menor a 0.03 por default
# 3) Parametrización es de -pi a pi
# 4) x, y, z son arreglos
#############################################################

#Hace tantos nudos como se indique en las ternas
#Lee la terna correspondiente del archivo Ternas.txt
#Valores dafault 100,500, 5, [0,0,0]
#Regresa las rutas de los archivos:
#Ruta
#RutaAlcances
#RutaAumentos
def HazNudos(indice = 100, intervalos = 500, iteraciones = 5, Fase = [0,0,0], umbral=0.001):
  terna = FuncionesAuxiliares.LeeTernas([indice])
  print("-Terna: ", terna[0])
  print("-Fase: ", Fase)
  Ruta, RutaAlcances, RutaAumentos, sirve = TrabajaNudo(Terna=terna[0],
                                                fases=Fase, 
                                                intervalos=intervalos,
                                                iteraciones = iteraciones,
                                                umbral = umbral)
  return Ruta, RutaAlcances, RutaAumentos, sirve

# 1) Hace nudo original
# 2) Acota alcance puntual por esferas
# 3) Escribe archivo de alcances puntuales
# 4) Escribe archivo de aumentos
# 5) Clasifica si sirve o no dependiendo del umbral o si tiene autointersecciones
def TrabajaNudo(Terna, fases, intervalos, iteraciones, umbral):
  a,b,c = Terna[0], Terna[1], Terna[2]
  t = np.linspace(-np.pi, np.pi, intervalos, endpoint=False)
  x, y, z = np.cos((a*t)+fases[0]), np.cos((b*t)+fases[1]), np.cos((c*t)+fases[2])
  
  #Hace el nudo con coordenadas [x[i], y[i], z[i]]
  Nudo =[ [x[i], y[i], z[i]] for i in range(intervalos) ]
  Nudo = np.array(Nudo)

  Alcances, Aumentos, autointerseccion = acotaAlcancePorEsferas(Nudo, intervalos, iteraciones)
  RutaAlcances = FuncionesAuxiliares.EscribeAlcancesPuntualesTXT(Alcances, Terna, fases)
  RutaAumentos = FuncionesAuxiliares.EscribeAumentosTXT(Aumentos, Terna, fases)

  alcance = min(Alcances)

  if autointerseccion:
    sirve = False
    motivo = 'Autoint'
    print('No sirve por autointerseccion')
  else:
    if alcance < umbral:
      sirve = False
      motivo = 'Alcance'
      print('No sive alcance menor a umbral=', umbral, 'alcance=', alcance)
    else:
      sirve = True
      motivo = 'Sirve'

  ruta = 'Nudos/Sencillos/'
  Ruta = FuncionesAuxiliares.GeneraPLYdeNudo(ruta, Nudo, Terna, fases, alcance, iteraciones, sirve, motivo)
  return Ruta, RutaAlcances, RutaAumentos, sirve

