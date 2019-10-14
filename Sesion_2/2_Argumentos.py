#Programa con argumentos

import sys

l = len(sys.argv)

for i in range(l):
	print('Argumento', i, 'es', sys.argv[i])
