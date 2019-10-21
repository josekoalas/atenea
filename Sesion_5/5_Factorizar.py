#Descomponer en factores primos

def int_input(t):
	try:
		i = int(input(t))
		return i
	except:
		print("No es un número entero")
		return 0

def primes(n):
    if n < 2:
        return []
    else:
        pl = [2] #Prime List
        for i in range(3, n):
            isPrime = True
            for j in pl:
                if j > n ** 0.5:
                    break
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                pl.append(i)
        return pl

def factors(n):
    fl = []
    for p in primes(n):
        while n%p==0:
            fl.append(p)
            n=n//p
            if n < 2:
                return fl

factors(10)

print(factors(99999))
