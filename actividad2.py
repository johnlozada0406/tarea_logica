# #2. Lógica de Predicados (Cuantificadores)
# #Contexto: Gestión de inventario de una tienda.

# Enunciado: Tienes una lista de productos, cada uno con un nombre y un stock.
# Determina si todos los productos tienen stock mayor a 0 (Cuantificador Universal $\forall$).
# Determina si al menos uno de los productos es de la categoría "Lujo" (Cuantificador Existencial $\exists$).

#Ax(S)>0

productos = [{"nombre": "Pan", "stock": 10, "tipo": "Basico"}, {"nombre": "Reloj", "stock": 0, "tipo": "Lujo"}]

respuesta = all( S["stock"] > 0 for S in productos)

#Ex(L)
respuesta2 = any( L["tipo"] == "Lujo" for L in productos)

print( respuesta)
print( respuesta2)
