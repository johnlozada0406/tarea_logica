from sympy import symbols, Or, And, Implies, Equivalent
# Contexto: Filtro de becas universitarias.
# Enunciado: Un estudiante es elegible para una beca si cumple una de estas dos condiciones:
# Su promedio es mayor o igual a 9.0.
# Su promedio es mayor a 8.0 y su nivel socioeconómico es bajo (1 o 2).
# Reto en Python: Escribe un script que compare los datos de un estudiante contra estas reglas de comparación lógica.

#Ex()
estudiante =  [{"nombre": "juan", "promedio": 10, "nivel socioeconomico": "bajo"}, {"nombre": "jose", "promedio": 4, "nivel socioeconomico": "alto"},
               {"nombre": "andres", "promedio": 6, "nivel socioeconomico": "medio"},{"nombre": "valen", "promedio": 2, "nivel socioeconomico": "alto"},
               {"nombre": "diego", "promedio": 5, "nivel socioeconomico": "medio"},{"nombre": "diana", "promedio": 5, "nivel socioeconomico": "bajo"},]

condicion1 = any( E["promedio"] >= 9 for E in estudiante)

condicion2 = any( E["promedio"] >= 8 and E["nivel socioeconomico"] == "bajo" for E in estudiante)

beca = Or(condicion1,condicion2)

print(beca)