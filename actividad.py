from sympy import symbols, Or, And, Implies, Equivalent


#Enunciado: La bóveda se abre ($B$) si y solo si se introduce la clave correcta
#  ($C$) y el escáner de retina es positivo ($R$), o si se activa la llave de 
# emergencia ($E$).

#B = (C and R) or E enunciado

def boleado(variable):
    if variable=="s":variable=True
    else:variable=False
    return variable

B = True
C = boleado(input("clave correcta? s/n "))
R = boleado(input("Retina correcta? s/n "))
E = boleado(input("llave de emergencia? s/n "))

aaa = And(C,R)
segundo_elemento = Or(E,aaa)
Respuesta = Equivalent(B, segundo_elemento )

print( Respuesta)