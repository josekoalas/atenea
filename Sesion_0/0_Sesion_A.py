print('Hello World')
4 + 5 #Suma
#[Out]# 9
50 - 25 #Resta
#[Out]# 25
6 * 4 #Mult
#[Out]# 24
10 / 3 #Div
#[Out]# 3.3333333333333335
10.0 // 3 #DivEntera
#[Out]# 3.0
10 % 3 #Modulo
#[Out]# 1
2 ** 8 #Exp
#[Out]# 256
10 - 4 * 3 #OrdenOperaciones
#[Out]# -2
(10 - 4) * 3 #Parentesis
#[Out]# 18
a = 256 #Int
a
#[Out]# 256
type(a)
#[Out]# builtins.int
print(a)
b = 9.99 #Float
b
#[Out]# 9.99
type(b)
#[Out]# builtins.float
c = a + 2*b #Expresion
c
#[Out]# 275.98
d = 5+3j #Complex
d
#[Out]# (5+3j)
type(d)
#[Out]# builtins.complex
e = 'Texto' #String, es igual ' que "
f = 'Hello World'
print(e + ', ' + f)
type(e)
#[Out]# builtins.str
g = True #Bool
g
#[Out]# True
type(g)
#[Out]# builtins.bool
print(g == 1)
print(g == 0)
h, i, j = 256, True, 'Hey' #AsignacionMult
print(h + ' ' + i + ' ' + j)
print(str(h) + ' ' + str(i) + ' ' + j)
k = -100 #Negativo
abs(k) #ValorAbsoluto
#[Out]# 100
l = 6+3j #Complejo
abs(l) #Modulo
#[Out]# 6.708203932499369
m = 256
float(m) #ConvertirIntFloat
#[Out]# 256.0
m
#[Out]# 256
n = float(m)
n
#[Out]# 256.0
o = int(n) #ConvertirFloatInt
o
#[Out]# 256
sin(90)
from math import * #LibreriaMatematicas
sin(90)
#[Out]# 0.8939966636005579
sin(2.0)
#[Out]# 0.9092974268256817
cos(10)
#[Out]# -0.8390715290764524
tan(1

)
#[Out]# 1.5574077246549023
sinh(1)
#[Out]# 1.1752011936438014
asin(1)
#[Out]# 1.5707963267948966
pi
#[Out]# 3.141592653589793
e
#[Out]# 2.718281828459045
exp(1)
#[Out]# 2.718281828459045
log(1)
#[Out]# 0.0
log10(1)
#[Out]# 0.0
sqrt(2)
#[Out]# 1.4142135623730951
a = 9.6431
floor(a)
#[Out]# 9
round(a)
#[Out]# 10
ceil(a)
#[Out]# 10
get_ipython().system('clear ')
from math import *
sin(a)
#[Out]# -0.21659179899598333
pi
#[Out]# 3.141592653589793
e
#[Out]# 2.718281828459045
sin(pi)
#[Out]# 1.2246467991473532e-16
exp(1)
#[Out]# 2.718281828459045
log(e)
#[Out]# 1.0
x = 2.5
round(x)
#[Out]# 2
x = 2.51
round(x)
#[Out]# 3
# ???
ceil(x)
#[Out]# 3
floor(x)
#[Out]# 2
trunc(x)
#[Out]# 2
y = -3.5
ceil(y)
#[Out]# -3
floor(y)
#[Out]# -4
print(ceil(y) + ' ' +  floor(y))
print(str(ceil(y)) + ' ' +  str(floor(y)))
round(y)
#[Out]# -4
sen(pi / 2)
sin(pi / 2)
#[Out]# 1.0
sin(deg(90))
sin(90º)
degree(90)
degrees(90)
#[Out]# 5156.620156177409
radians(90)
#[Out]# 1.5707963267948966
sin(radians(90))
#[Out]# 1.0
from cmath import *
import cmath as cm
z = 4 + 3j
z.real #ParteReal
#[Out]# 4.0
z.imag #ParteImaginaria
#[Out]# 3.0
cm.phase(z)
#[Out]# 0.6435011087932844
phase(z)
#[Out]# 0.6435011087932844
sin(4)
#[Out]# (-0.7568024953079282-0j)
cm.atan2(z.imag, z.real) #FaseZ
atan2(z.imag, z.real) #FaseZ
#[Out]# 0.6435011087932844
polar(z) #ConvertirPolar
#[Out]# (5.0, 0.6435011087932844)
abs(z)
#[Out]# 5.0
phase(z)
#[Out]# 0.6435011087932844
cart(5.0, 0.6435011087932844)
rect(5.0, 0.6435011087932844) #ConvertirCartesiana
#[Out]# (4+3j)
get_ipython().system('clear ')
l = [5, 2.5, True, 'Hey', [2, 3, 4]] #DefinirLista
l
#[Out]# [5, 2.5, True, 'Hey', [2, 3, 4]]
len(l)
#[Out]# 5
len(l) #NumeroElementos
#[Out]# 5
l[0] #Acceder (Empiezan en 0)
#[Out]# 5
l[1]
#[Out]# 2.5
l[2]
#[Out]# True
l[3]
#[Out]# 'Hey'
l[4]
#[Out]# [2, 3, 4]
l[4][0]
#[Out]# 2
l[-1] #UltimoElemento
#[Out]# [2, 3, 4]
type(l)
#[Out]# builtins.list
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
len(x)
#[Out]# 10
n = len(x)
max(x) #NumeroMaisAlto
#[Out]# 9
min(x) #NumeroMaisBaixo
#[Out]# 0
sum(x) #Sumatorio
#[Out]# 45
x[3] += 1
x
#[Out]# [1, 2, 3, 5, 5, 6, 7, 8, 9, 0]
get_ipython().system('clear ')
