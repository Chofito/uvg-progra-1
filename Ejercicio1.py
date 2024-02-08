# Parte 1, Ejercicio 1
print("Ejercicio 1: operaciones aritmeticas")
number1 = 0
number2 = 0

while True:
    try:
        number1 = int(input("Ingrese el primer numero: "))
        number2 = int(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print("Error: Ingrese un numero entero")

addition = number1 + number2
substraction = number1 - number2
multiplication = number1 * number2
divisionInteger = number1 // number2
divisionDecimal = number1 / number2
module = number1 % number2
pow = number1 ** number2

print(f'{number1} + {number2} = {addition}')
print(f'{number1} - {number2} = {substraction}')
print(f'{number1} * {number2} = {multiplication}')
print(f'{number1} // {number2} = {divisionInteger}')
print(f'{number1} / {number2} = {divisionDecimal}')
print(f'{number1} % {number2} = {module}')
print(f'{number1} ** {number2} = {pow}')

# Parte 2, Ejercicio 1
print("\nEjercicio 2: operaciones booleanas")
greaterThan = number1 > number2
greatherOrEqual = number1 >= number2
lessThan = number1 < number2
lessOrEqual = number1 <= number2
equal = number1 == number2
notEqual = number1 != number2
notEvaluation = number1 is not number2
andEvaluation = greaterThan and greatherOrEqual
orEvaluation = lessThan or lessOrEqual

print(f'{number1} > {number2} = {greaterThan}')
print(f'{number1} >= {number2} = {greatherOrEqual}')
print(f'{number1} < {number2} = {lessThan}')
print(f'{number1} <= {number2} = {lessOrEqual}')
print(f'{number1} == {number2} = {equal}')
print(f'{number1} != {number2} = {notEqual}')
print(f'{number1} is not {number2} = {notEvaluation}')
print(f'{number1} > {number2} and {number1} >= {number2} = {andEvaluation}')
print(f'{number1} < {number2} or {number1} <= {number2} = {orEvaluation}')
