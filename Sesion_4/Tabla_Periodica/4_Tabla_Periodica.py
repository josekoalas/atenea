#IMPORTS
import os
import sys
import inspect
import numpy as np

#*** Tabla Pyriodica ***
#Calcula fórmulas de átomos y moléculas, además del peso molecular
#Necesitas el archivo "tablaperiodica" en la misma ubicación que este

#Este programa funciona con métodos (Los que empiezan por def), por lo tanto
#el programa en si se encuentra en las últimas lineas, y referencian a las superiores


#DIRECTORIO
#Obtener la localización del archivo .py
#Opción 1: RECOMENDADA
dir = os.path.dirname(os.path.abspath(__file__))
#Opción 2: No recomendada, está comentada
''' filename = inspect.getframeinfo(inspect.currentframe()).filename
dir = os.path.dirname(os.path.abspath(filename))
print(dir)
if dir[-9:] != "Periodica":
    dir += "/Sesion 4/Tabla Periodica" '''


#OBTENER DATOS
#Para gestionar errores como que no se encuentre el archivo, utilizamos try
def get_data():
    try:
        f = open(dir + "/tablaperiodica", "r") #Abrir el archivo, directorio + nombre
        data = f.readlines() #Obtener las lineas una por una
        t = [[],[],[]]

        for i in range(len(data)):
            #Formato de texto: H HIDROGENO 1
            line = data[i].rsplit()
            t0 = line[0]
            t1 = line[1]
            t2 = line[2]
            #Formato de las listas: ["H", "HIDROGENO", "1"]
            t[0].append(t0) #Las añadimos a nuestra tabla periodica
            t[1].append(t1) #Separamos simbolo, nombre y peso (0,1,2)
            t[2].append(t2)
        f.close()
        return t
    except:
        print("Error al tratar de acceder al archivo \"tablaperiodica\"")
        print("Compruebe el directorio, los permisos y el fichero para continuar")
        sys.exit()


#LEER ELEMENTO
def get_element(t, e = "", p = True):
    if e == "": #Esto nos permitirá pasar un elemento a la función, pero si se llama sin nada, nos pedirá una entrada
        e = input("Indica el símbolo del elemento: ") #Obtener simbolo elemento

    if len(e) > 2: e = e[0].upper() + e[1:3].lower()
    if len(e) == 2: e = e[0].upper() + e[1].lower()
    if len(e) == 1: e = e[0].upper()

    if e in t[0]: #Si está en la lista de simbolos
        i = t[0].index(e) #Obtenemos el indice
        ed = (t[0][i], t[1][i], t[2][i], i) #Creamos una tupla con los datos importantes y el indice (Nº Atomico - 1)
        if p: print("Simbolo: {} - Elemento: {} - Peso: {}".format(ed[0], ed[1], ed[2])) #Mostramos la informacion
        return ed
    else:
        if p: print("El elemento especificado no se encuentra en la tabla periódica")


#LEER MOLÉCULA
def get_molecule(t, m = ""):
    #Almacenar información molecular
    molecula = [[],[]] #Elemento, coeficiente

    if m == "":
        print("Introduce la cadena molecular")
        print("Para ello, escribe una serie de elementos (H) seguidos de sus coeficientes (2), por ejemplo, H20")
        print("No es necesario especificar el coeficiente si es 1, ni escribir mayúsculas, aunque puede hacerse")
        print("Los elementos pueden tener hasta 3 letras (Uuo) y los coeficientes hasta 2 cifras (16)")
        m = input("-> ") #Obtener cadena de molécula

    l = len(m) #Numero de caracteres
    #Debug information
    print("Cadena: {} - Longitud: {}".format(m, l))

    nl = 0 #Number of letters
    nn = 0 #Number of numbers

    for i in range(l):
        #Imaginemos tres caracteres: ***
        #* - Caracter, L - Letra, N - Numero

        c1 = False #Coeficiente igual a 1 por estar en medio, por defecto falso

        #LETRAS
        l0 = not m[i].isdigit() #L**
        if l0: #Si es una letra
            if nl == 0:
                if (i < l - 2): #Si no es la ultima ni la penultima letra
                    l1 = not m[i+1].isdigit() #*L*
                    l2 = not m[i+2].isdigit() #**L

                    if l0 and l1 and l2: #LLL
                        e = m[i:i+3]
                        if not (i < l - 3):
                            c1 = True
                    elif l0 and l1: #LLN
                        e = m[i:i+2]
                    elif l0: #LN*
                        e = m[i]
                elif (i < l - 1): #Penultima letra
                    l1 = not m[i+1].isdigit() #*L

                    if l0 and l1: #LL
                        e = m[i:i+2]
                        c1 = True
                    elif l0: #LN
                        e = m[i]
                elif (i < l): #Ultima letra
                    if l0: #L
                        e = m[i]
                        c1 = True

                #ELEMENTO
                elem = get_element(t, e, False) #Obtenemos elemento del nombre
                while elem == None and len(e) > 1:
                    e = e[:-1]
                    nl -= 1
                    c1 = True
                    elem = get_element(t, e, False)
                nl = len(e) - 1
                molecula[0].append(elem)
            else:
                nl -= 1

        #COEFICIENTE
        #Una vez tenemos el nombre del elemento, comprobamos si hay exponente despues
        #Nos aseguramos de que existen los dos siguientes lugares en caso de que e sea LLL y LL*
        else:
            nl = 0
            n0 = not l0 #N*
            if nn == 0:
                if (i < l - 1): #No es el ultimo numero
                    n1 = m[i+1].isdigit() #*N

                    if n0 and n1: #NN
                        c = m[i:i+2]
                    elif n0: #NL
                        c = m[i]
                elif (i < l): #Ultimo numero
                    if n0: #N
                        c = m[i]
                nn = len(c) - 1
                molecula[1].append(c)
                #print(c)
            else:
                nn -= 1

        if c1:
            c = "1"
            molecula[1].append(c)

    return molecula


#PESO MOLECULAR
def peso_molecular(m):
    #Molecula m, m[0] elemento - m[1] coeficientes
    #Elemento de la forma ["H", "HIDROGENO", 1, 1], por lo tanto, m[0][i][2] peso
    l = len(m[0]) #Cantidad de elementos
    s = 0 #Suma del peso molecular
    for i in range(l):
        s += float(m[0][i][2]) * float(m[1][i]) #Suma ponderada del peso y los coeficientes
    return s


#PROGRAMA
print("---\nBienvenido a la Tabla Pyriodica uwu\n---")

tabla = get_data() #Obtener datos de la tabla

#Bucle principal del programa
while(True):
    print("Elige una función:\n1.Ver Elemento(e)\n2.Ver Molécula(m)\n3.¡Peso Molecular!(p)\n4.Tabla Periodica(t)\n5.Salir(s)")
    inp = input("-> ")
    print("---")

    if(inp.upper() == "E" or inp == "1"):
      e = get_element(tabla)
      while e == None:
          e = get_element(tabla)
    elif(inp.upper() == "M" or inp == "2"):
      molecula = get_molecule(tabla)
      print("Molécula:")
      for i in range(len(molecula[1])):
          print(i)
          symbol = molecula[0][i][0]
          coef = molecula[1][i]
          print("Simbolo: {} - Coeficiente: {}".format(symbol, coef))
    elif(inp.upper() == "T" or inp == "4"):
      for i in range(len(tabla[0])):
              print("Simbolo: {} - Elemento: {} - Peso: {}".format(tabla[0][i], tabla[1][i], tabla[2][i]))
    elif(inp.upper() == "S" or inp == "5"):
           sys.exit()
    else: #Por defecto, peso molecular
          molecula = get_molecule(tabla)
          peso = peso_molecular(molecula)
          print("Molécula:")
          for i in range(len(molecula[1])):
              symbol = molecula[0][i][0]
              pelem = molecula[0][i][2]
              coef = molecula[1][i]
              print("Simbolo: {} - Coeficiente: {} - Peso: {}".format(symbol, coef, float(pelem) * float(coef)))
          print("Peso molecular: {}".format(peso))

    input("---\nPresiona enter para volver ")
    print("---")
