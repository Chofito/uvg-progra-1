print("Ejercicio 2: Condicionales")
print("Actividad 1")

monthNumber = 1

while True:
    try:
        monthNumber = int(input("Ingrese el número de mes: "))
        
        if monthNumber >= 1 and monthNumber <= 12:
          break
        else:
          print("El número de mes ingresado no es válido, ingrese un número entre 1 y 12")
    except ValueError:
        print("El número de mes ingresado no es válido, ingrese un número entre 1 y 12")
  
if monthNumber == 1:
  print("Mes " + str(monthNumber) + ": Enero")
elif monthNumber == 2:
  print("Mes " + str(monthNumber) + ": Febrero")
elif monthNumber == 3:
  print("Mes " + str(monthNumber) + ": Marzo")
elif monthNumber == 4:
  print("Mes " + str(monthNumber) + ": Abril")
elif monthNumber == 5:
  print("Mes " + str(monthNumber) + ": Mayo")
elif monthNumber == 6:
  print("Mes " + str(monthNumber) + ": Junio")
elif monthNumber == 7:
  print("Mes " + str(monthNumber) + ": Julio")
elif monthNumber == 8:
  print("Mes " + str(monthNumber) + ": Agosto")
elif monthNumber == 9:
  print("Mes " + str(monthNumber) + ": Septiembre")
elif monthNumber == 10:
  print("Mes " + str(monthNumber) + ": Octubre")
elif monthNumber == 11:
  print("Mes " + str(monthNumber) + ": Noviembre")
elif monthNumber == 12:
  print("Mes " + str(monthNumber) + ": Diciembre")
else:
  print("El número de mes ingresado no es válido, ingrese un número entre 1 y 12")

print("\nActividad 2")
numberA = None
numberB = None
numberC = None

while True:
    try:
        if numberA is None:
          numberA = int(input("Ingrese el primer número: "))
        if numberB is None:
          numberB = int(input("Ingrese el segundo número: "))
        if numberC is None:
          numberC = int(input("Ingrese el tercer número: "))
        break
    except ValueError:
        print("Error: Ingrese un número entero")

if numberA > numberB:
  if numberA > numberC:
    print(f"El número mayor es {numberA}")
  else:
    if numberA == numberC:
      print(f"Los números mayores son {numberA} y {numberC}")
    else :
      print(f"El número mayor es {numberC}")
else:
  if numberA == numberB:
    if numberA > numberC:
      print(f"Los números mayores son {numberA} y {numberB}")
    else:
      if numberA == numberC:
        print(f"Los números {numberA}, {numberB} y {numberC} son iguales")
      else:
        print(f"El número mayor es {numberC}")
  else:
    if numberB > numberC:
      print(f"El número mayor es {numberB}")
    else:
      if numberB == numberC:
        print(f"Los números mayores son {numberB} y {numberC}")
      else:
        print(f"El número mayor es {numberC}")

print("\nActividad 3")
userBirthMonth = None
userBirthDay = None
monthAndDays = (
  ("Enero", 31),
  ("Febrero", 29),
  ("Marzo", 31),
  ("Abril", 30),
  ("Mayo", 31),
  ("Junio", 30),
  ("Julio", 31),
  ("Agosto", 31),
  ("Septiembre", 30),
  ("Octubre", 31),
  ("Noviembre", 30),
  ("Diciembre", 31)
)

while True:
  try:
    userBirthMonth = int(input("Ingrese el número de su mes de nacimiento: "))
    
    if userBirthMonth < 1 or userBirthMonth > 12:
      print("Error: Ingrese un número de mes valido entre 1 y 12")
    else:
      break
  except ValueError:
    print("Error: Ingrese un número entero")
    
while True:
  try:
    userBirthDay = int(input("Ingrese el número de su día de nacimiento: "))
    
    if userBirthDay < 1 or userBirthDay > monthAndDays[userBirthMonth - 1][1]:
      print(f"Error: Ingrese un día valido para el mes de {monthAndDays[userBirthMonth - 1][0]} entre 1 y {monthAndDays[userBirthMonth - 1][1]}")
    else:
      break
  except ValueError:
    print("Error: Ingrese un número entero")
    
# Zodiac signs
zodiacSigns = (
  ((1, 20), (2, 18), "Acuario"),
  ((2, 19), (3, 20), "Piscis"),
  ((3, 21), (4, 19), "Aries"),
  ((4, 20), (5, 20), "Tauro"),
  ((5, 21), (6, 20), "Géminis"),
  ((6, 21), (7, 22), "Cancer"),
  ((7, 23), (8, 22), "Leo"),
  ((8, 23), (9, 22), "Virgo"),
  ((9, 23), (10, 22), "Libra"),
  ((10, 23), (11, 21), "Escorpio"),
  ((11, 22), (12, 21), "Sagitario"),
  ((12, 22), (1, 19), "Capricornio"),
)

if userBirthDay >= zodiacSigns[userBirthMonth - 1][0][1]:
  print(f"Su signo zodiacal es {zodiacSigns[userBirthMonth - 1][2]}")
else:
  print(f"Su signo zodiacal es {zodiacSigns[userBirthMonth - 2][2]}")
