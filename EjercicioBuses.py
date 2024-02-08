from datetime import date

tipoViaje = (
  ("General", 100, "\n- Paradas constantes según necesidad.\n- Lugar asignado "),
  ("Ejecutivo", 150, "\n- Servicio directo sin paradas\n- Lugar asignado\n- Aire acondicionado\n- Servicio de TV "),
  ("Plus", 200, "\n- Servicio directo sin paradas\n- Lugar asignado\n- Aire acondicionado\n- Servicio de TV\n- Servicio de refrigerio")
)

descuentos = (
  # Descuentos General, horario en 24 horas, porcentaje
  ("General", "04:00 - 11:59", 0),
  ("General", "12:00 - 19:59", 0),
  ("General", "20:00 - 03:59", 5),
  # Descuentos Ejecutivo, horario en 24 horas, porcentaje
  ("Ejecutivo", "04:00 - 11:59", 10),
  ("Ejecutivo", "12:00 - 19:59", 12),
  ("Ejecutivo", "20:00 - 03:59", 15),
  # Descuentos Plus, horario en 24 horas, porcentaje
  ("Plus", "04:00 - 11:59", 12),
  ("Plus", "12:00 - 19:59", 15),
  ("Plus", "20:00 - 03:59", 18),
)

nombrePasajero = None
nitFactura = None
nombreFactura = None
direccion = None
lugarDeArribo = None
lugarDeDestino = None
tipoDeBus = None
horaSalida = None
descuento = 0
descuentoCalculado = 0
totalAPagar = 0
viajeSeleccionado = None

print("Bienvenido al servicio de buses!")
print("A continuacion se le pediran ciertos datos para que pueda viajar con nosotros!")

while True:
  nombrePasajero = input("Ingrese el nombre del pasajero: ")
  if nombrePasajero == "":
    print("El nombre del pasajero es requerido")
  else:
    break

while True:
  nitFactura = input("Ingrese el NIT de la factura: ")
  if nitFactura == "":
    print("El NIT de la factura es requerido")
  else:
    break
  
while True:
  nombreFactura = input("Ingrese el nombre para la factura: ")
  if nombreFactura == "":
    print("El nombre para la factura es requerido")
  else:
    break

while True:
  direccion = input("Ingrese la dirección de la factura: ")
  if direccion == "":
    print("La dirección de la factura es requerida")
  else:
    break

while True:
  lugarDeArribo = input("Ingrese el lugar de arribo: ")
  if lugarDeArribo == "":
    print("El lugar de arribo es requerido")
  else:
    break
  
while True:
  lugarDeDestino = input("Ingrese el lugar de destino: ")
  if lugarDeDestino == "":
    print("El lugar de destino es requerido")
  else:
    break

while True:
  tipoDeBus = input("Ingrese el tipo de bus (General, Ejecutivo, Plus): ")
  if tipoDeBus == "":
    print("El tipo de bus es requerido")
  else:
    tipoDeBus = tipoDeBus.capitalize()
    if tipoDeBus not in ["General", "Ejecutivo", "Plus"]:
      print("El tipo de bus ingresado no es válido, revise e intente de nuevo, asegurese que el nombre coincida")
    else:
      break
    
while True:
  horaSalida = input("Ingrese la hora de salida en el formato indicado (HHMM): ")
  
  try:
    horaSalida = int(horaSalida)
    
    if horaSalida < 0 or horaSalida > 2400:
      print("La hora de salida ingresada no es válida, revise e intente de nuevo")
  except ValueError:
    print("La hora de salida ingresada no es válida, revise el formato indicado (ej. 1345) e intente de nuevo")

  if horaSalida == "":
    print("La hora de salida es requerida")
  else:
    break
  
for desc in descuentos:
  if desc[0] == tipoDeBus:    
    if horaSalida >= int(desc[1].split(" - ")[0].replace(":", "")) and horaSalida <= int(desc[1].split(" - ")[1].replace(":", "")):
      descuento = desc[2]
      break
    # Validate especial case from 0000 to 0359
    if horaSalida >= 0 and horaSalida <= 359:
      descuento = desc[2]

for tipo in tipoViaje:
  if tipo[0] == tipoDeBus:
    viajeSeleccionado = tipo
    totalAPagar = tipo[1] - (tipo[1] * (descuento / 100))
    
descuentoCalculado = viajeSeleccionado[1] * (descuento / 100)
    
# from 0000 to 00:00, it can also be 000 to 00:00
horaSalida = str(horaSalida).zfill(4)
horaSalida = f"{horaSalida[:2]}:{horaSalida[2:]}"
    
print(f"\nAutobuses UVG – {tipoDeBus}")
print(f"Fecha: {date.today().strftime('%d/%m/%Y')}")
print(f"Nombre Cliente: {nombrePasajero}")
print(f"Nit: {nitFactura}")
print(f"Nombre Factura: {nombreFactura}")
print(f"Lugar de origen: {lugarDeArribo}")
print(f"Lugar de destino: {lugarDeDestino}")
print(f"Tipo servicio: {tipoDeBus}")
print(f"Hora de viaje: {horaSalida}")
print(f"Costo boleto: Q. {viajeSeleccionado[1]}.00")
print(f"Descuento: Q. {descuentoCalculado}")
print(f"Total a pagar: Q. {totalAPagar}")
print(f"\n******************************")
print(f"{viajeSeleccionado[2]}")

print("\nMuchas gracias por escoger nuestros servicios, que tenga un excelente viaje!")
