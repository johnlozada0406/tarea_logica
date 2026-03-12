# Contexto: Diagnóstico médico básico.
# Enunciado: Implementa un sistema de reglas de inferencia:
# Premisa 1: Si el paciente tiene fiebre ($F$) y tos ($T$), entonces tiene gripe ($G$).
# Premisa 2: Si el paciente tiene gripe ($G$), se le receta descanso ($D$).
# Reto en Python: Si un paciente llega con fiebre = True y tos = True,
# crea un pequeño motor de inferencia que concluya automáticamente que el paciente necesita descanso

#F and T --> G 
#V and V --> V

def boleado(variable):
    if variable=="s":variable=True
    else:variable=False
    return variable

F = boleado(input("tiene fiebre? s/n "))
T = boleado(input("tiene toz? s/n "))

#Reglas = premisas entonces conclusion []

rules = [
    (['fiebre', 'tos'], 'gripe'),
    (['gripe'], 'descanso')
]
facts = {
    "fiebre" : F,
    "tos" : T}

for condiciones, conclusion in rules:
    if all(facts.get(c, False) for c in condiciones):
        facts[conclusion] = True
    else:facts[conclusion] = False

print("necesitas descanso ")
print(facts[conclusion])