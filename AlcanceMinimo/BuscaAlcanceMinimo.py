#Version 21-Febrero 2023
import numpy as np
##########################
import FuncionesAuxiliares
from AlcancePorAristas import acotaAlcanceMinPorAristas as acotaAlcance


##############################################################
#    Verifica que el nudo
# 1) No tenga puntos repetidos 
# 2) Tenga alcance aceptable, menor a 0.03 por default
# 3) Parametrización es de -pi a pi
# 4) x, y, z son arreglos
#############################################################

#Hace tantos nudos como se indique en las ternas
#Arreglar fases
def HazNudos(cantidad_de_nudos=1, intervalos = 500):
  indices = FuncionesAuxiliares.EscogeTernas(cantidad_de_nudos)
  Ternas = FuncionesAuxiliares.LeeTernas(indices)
  Alcances = []
  Fases = [[0.5, 0.2, 3.6] ]
  for terna in Ternas:
    print("terna: ", terna)
    for fase in Fases:
      Nudo = TrabajaNudo(Terna=terna, fases=fase, intervalos=intervalos)


def TrabajaNudo(Terna, fases, intervalos):
  a,b,c = Terna[0], Terna[1], Terna[2]
  t = np.linspace(-np.pi, np.pi, intervalos, endpoint=False)
  x, y, z = np.cos((a*t)+fases[0]), np.cos((b*t)+fases[1]), np.cos((c*t)+fases[2])
  
  #Hace el nudo con coordenadas [x[i], y[i], z[i]]
  Nudo =[ [x[i], y[i], z[i]] for i in range(intervalos) ]
  Nudo = np.array(Nudo)

  #Primer manera de ver si hay repeticiones
  #NRep - No puntos repetidos, SRep - Sí hay repeticiones
  Cantidad_Puntos = ''
  Nudo_PuntosUnicos = np.unique(Nudo, axis=0)
  if len(Nudo_PuntosUnicos) != intervalos:
    Cantidad_Puntos = 'NRep-'
  else:
    Cantidad_Puntos = 'SRep-'

  #Acota alcance usando la funcion acotaAlcanceMinPorAristas de AlcancePorAristas
  #BR = Bad Reach, GR = Good Reach
  alcance = acotaAlcance(Nudo, intervalos)
  #print(Terna, '-', format(alcance, '.30f'))
  if alcance < 0.03:
    FuncionesAuxiliares.GeneraPLYdeNudo('BadReach/'+Cantidad_Puntos+'BR', Nudo, Terna, fases, alcance)
    return False
  else:
    FuncionesAuxiliares.GeneraPLYdeNudo('GoodReach/'+Cantidad_Puntos+'GR', Nudo, Terna, fases, alcance)
    return True

