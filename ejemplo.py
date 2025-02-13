"""
Ejemplo de uso de reglas de precedencia

La expresión es

(3 + 2) * 5 > 20 and not (10 % 3 == 0)
 
Paso a paso con precedencia aplicada ( así se lo debe hacer en algo
similar a una miniespecificación)

1.  Paréntesis internos primero

    (3 + 2) es igual a 5
    (10 % 3) es igual a 1 (El módulo da el residuo de la división 10 ÷ 3, que es 1)
    1 == 0 es igual a False (Comparación relacional: ¿1 es igual a 0? No.)

La expresión queda:
    5 * 5 > 20 and not False

2.  Multiplicación

    5 * 5 → 25

    Ahora se tiene:
    
    25 > 20 and not False

3.  Comparación relacional del símbolo (>)

    25 > 20 es igual a True
    
    La expresión ahora es:

    True and not False

4.  Negación (not) tiene prioridad sobre and

    not False → True
    
    Ahora se tiene:
    
    True and True

5.  Evaluación de and

    True and True es igual a True

6.  Resultado final es True

"""


resultado = (3 + 2) * 5 > 20 and not (10 % 3 == 0)
print("El resultado de la expresión: (3 + 2) * 5 > 20 and not (10 % 3 == 0) :",  resultado)
