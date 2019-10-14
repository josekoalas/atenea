print("Segunda Sesión")
i = [12, 43, 64, 675]
i[:2]
#[Out]# [12, 43]
i[2:]
#[Out]# [64, 675]
i[range(2)]
get_ipython().system('clear ')
x = [4, 6, 5, 7]
type(x)
#[Out]# builtins.list
x[0*

1]
#[Out]# 4
t = (8, 9, 10, 11) #Tupla (Lista no modificable)
t[2]
#[Out]# 10
t[1] = 0
type(t)
#[Out]# builtins.tuple
y = tuple(x)
y
#[Out]# (4, 6, 5, 7)
y = tuple(x) #Convertir lista a tupla
list(y)
#[Out]# [4, 6, 5, 7]
#
get_ipython().system('clear ')
#NumPy
import numpy as np
x = np.array([3,4,5,7,8,2,7,4,7,4,6,5]) #Crear vector a partir de lista
x
#[Out]# array([3, 4, 5, 7, 8, 2, 7, 4, 7, 4, 6, 5])
type(x)
#[Out]# numpy.ndarray
x.shape
#[Out]# (12,)
x.ndim #Numero Dimensiones
#[Out]# 1
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a.ndim
#[Out]# 2
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
get_ipython().system('clear ')
x.shape
#[Out]# (12,)
a.shape
#[Out]# (3, 3)
x.size
#[Out]# 12
for i in range(10):
break
u = "uwu"
for i in range(10):
    u = u + "uwu"
    print uwu
    break
for i in range(10):
    u = u + "uwu"
    print(u)
    break

for i in range(10):
    u = u + "uwu"
    print(u);
    
for i in range(100):
    u = u + "uwu"
    print(u);
    
get_ipython().system('clear ')
if (1 == 0):
    print("HEY")
else:
    print("Oh :(")

def test():

    
    break

def test(x):
    if (x>0):
        print("Positive")
    else:
        print("Negative")

test(10)
test(-124
)
a.itemsize
#[Out]# 4
a.itemsize #NumeroElementos
#[Out]# 4
a.dtype #Data Type
#[Out]# dtype('int32')
get_ipython().system('clear ')
a.size
#[Out]# 9
x.size
#[Out]# 12
for i in x.size:
    print(x[i])

for i in range(x.size):
    print(x[i])

y
#[Out]# (4, 6, 5, 7)
y = array(x, dtype="float")
y = np.array(x, dtype="float")
y.dtype
#[Out]# dtype('float64')
y.itemsize
#[Out]# 8
get_ipython().system('clear ')
y
#[Out]# array([ 3.,  4.,  5.,  7.,  8.,  2.,  7.,  4.,  7.,  4.,  6.,  5.])
get_ipython().system('clear ')
#np.arange(inicio, fin, incremento)
#np.linspace(inicio, fin, n elementos) fin si incluido
b = np.arange(1, 100, 5)
c = np.linspace(1, 1000, 3000)
b
#[Out]# array([ 1,  6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81,
#[Out]#        86, 91, 96])
c
#[Out]# array([    1.        ,     1.33311104,     1.66622207, ...,   999.33377793,
#[Out]#          999.66688896,  1000.        ])
print(c)
get_ipython().system('clear ')
#
#
#
get_ipython().system('clear ')
import matplotlib as plt
