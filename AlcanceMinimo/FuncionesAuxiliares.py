# Version 21 Febrero 2023
import numpy as np
import random
import sys

#Lee el archivo Ternas.txt
#Se debe aumentar 5 por el encabezado
def LeeTernas(Indices):
  Ternas = []
  fichero = open('AlcanceMinimo/Ternas/Ternas.txt')
  #fichero = open('Ternas/Ternas.txt')
  lineas = fichero.readlines()
  for i in Indices:
    terna_cadena = lineas[i+5]
    terna_cadena = terna_cadena.replace('\n', '')
    terna_cadena = terna_cadena.replace('[', '')
    terna_cadena = terna_cadena.replace(']', '')
    terna_arreglo = terna_cadena.split()
    terna = [int(elemento) for elemento in terna_arreglo]
    Ternas.append(terna)
  return Ternas

def EscogeTernas(cantidad_de_nudos):
  Ternas = []
  fichero = open('AlcanceMinimo/Ternas/Ternas.txt')
  lineas = fichero.readlines()
  cantidad_de_ternas = len(lineas)
  baraja = [i for i in range(1, cantidad_de_ternas+1)]
  TernasAEscoger = random.sample(baraja, cantidad_de_nudos)
  TernasAEscoger.sort()
  return TernasAEscoger


def ArchivoPLY(Nombre_Archivo, vertices=[], caras=[], aristas=[], terna=[], fases=[], alcance=0):
  name = Nombre_Archivo+'.ply'
  comentario1 = 'Periodos: '+str(terna)
  comentario2 = 'Fases: '+str(fases)
  comentario3 = 'Alcance: '+str(alcance)
  numero_vertices = len(vertices)
  numero_caras= len(caras)
  numero_aristas = len(aristas)
  with open(name, 'w') as writefile:
      #Encabezado del archivo
      writefile.write("ply\n")
      writefile.write("format ascii 1.0\n")
      writefile.write("comment "+comentario1+"\n")
      writefile.write("comment "+comentario2+"\n")
      writefile.write("comment "+comentario3+"\n")
      writefile.write("element vertex "+str(numero_vertices)+"\n")
      writefile.write("property float x\n")
      writefile.write("property float y\n")
      writefile.write("property float z\n")
      writefile.write("element face "+str(numero_caras)+"\n")
      writefile.write("property list uchar int vertex_indices\n")
      writefile.write("element edge "+str(numero_aristas)+"\n")
      writefile.write("property int32 vertex1 \n")
      writefile.write("property int32 vertex2\n")
      writefile.write("end_header\n")
      #Escribe los vértices
      for w in vertices:
          v=np.array(w)
          y = np.array2string(v,  formatter={'float_kind':lambda x: "%.10f" % x})
          y=y.replace('[', "")
          y=y.replace(']', "")
          writefile.write(""+y+"\n")

      #Escribe las aristas   
      for f in caras:
          puntos = str(len(f))
          g=np.array(f)
          y = np.array2string(g)
          y=y.replace('[', '')
          y=y.replace(']', '')
          writefile.write(puntos+' '+y+"\n")
              #Escribe las aristas   
      for f in aristas:
          g=np.array(f)
          y = np.array2string(g)
          y=y.replace('[', '')
          y=y.replace(']', '')
          writefile.write(' '+y+"\n")
  print('Escribí archivo:', name)
  return True

def GeneraPLYdeNudo(Calificacion, Nudo, Terna, fase, alcance):
  intervalos = len( Nudo )
  Vertices = Nudo
  Aristas = []
  for j in range( intervalos):
    Aristas.append([j%intervalos, (j+1)%intervalos])
  nombre_x = "cos(" + str(Terna[0]) + "t+" +str(fase[0]) + ')_'
  nombre_y = "cos(" + str(Terna[1]) + "t+" +str(fase[1]) + ')_'
  nombre_z = "cos(" + str(Terna[2]) + "t+" +str(fase[2]) + ')'
  name = Calificacion+'-'+nombre_x+nombre_y+nombre_z
  ArchivoPLY("Nudos/"+name, vertices=Vertices, aristas=Aristas, terna=Terna, fases=fase, alcance=alcance)


