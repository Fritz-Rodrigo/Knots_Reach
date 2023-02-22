#Version 12 de Febrero 2023
#Hace ternas ordenadas de números primos relativos
import numpy as np
from itertools import product as cartesian
from math import gcd as gcd
from datetime import datetime


timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)
date_time = datetime.fromtimestamp(timestamp)
d = date_time.strftime("%m/%d/%Y, %H:%M:%S")

A=[]
for i in range(1,12):
  A.append(i)
Ternas = []
for element in cartesian(A,A,A):
#Califica si son primos reltivos
  if gcd(element[0], element[1]) == gcd(element[1], element[2]) == gcd(element[0], element[2]) == 1:
    Ternas.append(np.array(element))

name = 'Ternas.txt'
with open(name, 'w') as writefile:
  cantidad = str(len(Ternas))
  writefile.write('###############################################'+"\n")
  writefile.write("# "+cantidad+' ternas para nudos'+"\n")
  writefile.write('# Version 1'+"\n")
  writefile.write('# '+d+"\n")
  writefile.write('###############################################'+"\n")
  for t in Ternas:
    y = np.array2string(t)
    writefile.write(""+y+"\n")

print("Termine:", name)