# Version 21 de Febrero
# alcance por aristas del nudo simple

import numpy as np
from itertools import product as cartesian
  
#Acota alcance
def acotaAlcanceMinPorAristas(Nudo, intervalos):
  Rectas = []
  #Hace ecuaciones paramétricas de todas las aristas del nudo simple
  for i in range(intervalos):
    j = (i+1)%intervalos
    Rectas.append( EcuacionParametricaRecta(Nudo[i], Nudo[j]) )
  i=0
  #En Distancias voy a guardar todas las distancias de las aristas a las aristas
  Distancias = []
  #Para una recta, no va a considerar a sus vecinos (radio 20)
  for i in range(intervalos):
    M = {i}
    a = 20
    for m in range(1,a):
      M.update( [(i-m)%intervalos, (i+m)%intervalos ])
    for k in range(intervalos):
      #Considera las rectas que no están en la vecindad M
      if k not in M:
        distanciaMin = DistanciaMinEntreDosSegmentos(Rectas[i], Rectas[k])
        Distancias.append(distanciaMin)
  return min(Distancias)

#Ecuacion paramétrica de la recta
#Recta = [R[0], R[1]]
#R[0]+\lambda*R[1]
def EcuacionParametricaRecta(Punto1, Punto2):
  P1=np.array(Punto1)
  P2=np.array(Punto2)
  V = np.array(P2-P1)
  R = np.array([Punto1, V])
  Recta = [R[0], R[1]]
  return Recta

#Aproxima la distancia minima entre dos segmentos de recta
#Recta = [R[0], R[1]]
def DistanciaMinEntreDosSegmentos(Recta1, Recta2):
  num_de_puntos = 6
  Distancias = []
  PuntosRecta1 = []
  PuntosRecta2 = []
  #Parametros \lambda de 0 a 1
  T = np.linspace(0, 1, num_de_puntos)
  for t in T:
    PuntosRecta1.append( Recta1[0]+( t*np.array( Recta1[1] ) ) )
    PuntosRecta2.append( Recta2[0]+( t*np.array( Recta2[1] ) ) )

  #Compara combinaciones de puntos
  Q = [i for i in range(0, num_de_puntos)]
  for q in cartesian(Q,Q):
    distancia = np.linalg.norm( PuntosRecta1[q[0]] - PuntosRecta2[q[1]] )
    Distancias.append(distancia)
  return min(Distancias)