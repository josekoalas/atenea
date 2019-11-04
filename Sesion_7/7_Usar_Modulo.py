import modulomc as mc

a, b = mc.int_input("A = "), mc.int_input("B = ")
fa = mc.order_factors(mc.factors(a))
fb = mc.order_factors(mc.factors(b))

print("Factores de A: {} - Factores de B: {}".format(fa, fb))
print("Maximo Comun Divisor: {} - Minimo Comun Multiplo: {}".format(mc.mcd(fa, fb), mc.mcm(fa,fb)))
