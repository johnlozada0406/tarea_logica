from sympy import symbols, Or, And, Implies

P, Q, R = symbols('P Q R')

expr = Implies(Or(P, Q), R)

from sympy.logic.boolalg import truth_table
for inputs, value in truth_table(expr, [P, Q, R]):
    print(dict(zip(['P','Q','R'], inputs)), value)
premises = And(Implies(P, Q), Implies(Q, R))
result = all(val for _, val in truth_table(Implies(premises, Implies(P, R)), [P,Q,R]))
print('Argumento válido:', result)