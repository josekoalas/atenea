#Escribe un programa en Python que monitorice as características da voz dunha persoa no tempo.
#Para simplificar o problema, o programa fará o seguinte:
import math
import cmath

#Lectura de datos
#Valor positivo, intensidade da voz no tempo
def get_input(t):
    i = ""
    while type(i) == str:
        try:
            i = input(t)
            if i == "":
                return None
            else:
                i = int(i)
        except:
            print("No es un número")
    return i

def voice_data():
    t = 0
    x = []
    while(True):
        i = get_input("Introduce la intensidad de la voz en t = {}: ".format(t))
        print(i)
        if i != None:
            if i > 0:
                x.append(i)
                t += 1
            else:
                print("No es positivo, prueba de nuevo o presiona enter para continuar")
        else:
            break
    return x

voice_data()

#Transformada de Fourier
def fourier(x):
    N = len(x)
    fl = []
    for n in range(N):
        f = 0.0
        for k in range(N):
            f += x[k] * cmath.exp(- 1j * cmath.pi * 2 * n * k / N)
        fl.append(f / N)
    return fl

f = fourier([1,2,3,4,5,4,3,2,1])
A = []
for i in f:
    A.append(math.sqrt(i.real ** 2 + i.imag ** 2))
print(A)
