#DEFINICION DE MODULOS
#Maximo Comun Divisor y Minimo Comun Multiplo

#Obtener numero entero positivo
def int_input(t):
	correct = False
	n = 0
	while(not correct):
		try:
			n = int(input(t))
			if n < 1:
				print("No puede ser un numero negativo")
			else:
				correct = True
		except:
			print("No es un numero entero")
	return n

#Lista de numeros primos hasta el numero indicado
def primes(n):
    if n < 2:
        return []
    else:
        pl = [2] #Lista de primos
        for i in range(3, n):
            isPrime = True
            for j in pl:
            	#Eliminar aquellos mayores que la mitad por eficiencia
                if j > n ** 0.5:
                    break
                #Eliminar si ya está en la lista o es multiplo
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                pl.append(i)
        return pl

#Elige los factores de entre la lista de primos hasta ese numero
def pre_factors(n):
	fl = []
	for p in primes(n):
		while n%p==0:
			fl.append(p)
			n=n//p
			if n < 2:
				return fl
def factors(n):
	m = pre_factors(n)
	if m == None: m = ([n])
	return m

#Dividir en factores y exponentes
def order_factors(f):
	n = []
	e = []
	for i in f:
		if i in n:
			ind = n.index(i)
			e[ind] += 1
		else:
			n.append(i)
			e.append(1)
	return (n, e)


#Calcular MCM (Minimo Comun Multiplo)
def mcm(a, b):
	#Suponemos que el mcm incluye todos los factores de b
	base = b[0].copy()
	exp = b[1].copy()

	for i in range(len(a[0])):
		isCommon = False
		for j in range(len(b[0])):
			if a[0][i] == base[j]:
				exp[j] = max(a[1][i], exp[j])
				isCommon = True
				break
		if not isCommon and not a[0][i] in base:
			base.append(a[0][i])
			exp.append(min(a[1][i], exp[j]))

	m = 1
	for i in range(len(base)):
		m = m * base[i] ** exp[i]
	return m


#Calcular MCD (Maximo Comun Divisor)
def mcd(a, b):
	base = []
	exp = []
	for i in range(len(a[0])):
		for j in range(len(b[0])):
			if a[0][i] == b[0][j]:
				base.append(a[0][i])
				exp.append(min(a[1][i], b[1][j]))
				break
	m = 1
	for i in range(len(base)):
		m = m * base[i] ** exp[i]
	return m
