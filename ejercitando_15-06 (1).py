#from Estructura import *

#lista = []
#for cont in range (3):
	#dato = input (f"Ingrese el dato numero {cont}:  ")
#	lista.append (dato)

#print (lista)


#En una primera parte con un bucle.\n\tingresa los nombres, apellidos y telefonos de 5 personas en 3 arrays "
#En una segunda parte ingresa un nombre y verigica que este en el array de nombres"
#\tSi el nombre pertenece a los ingresado imprime 'Es parte del grupo' "
#\timprime su apellido y telefono"
#\t\t(nota usa como referencia la posicion del index en donde lo encontastes el nombre


nombres = []
apellidos = []
telefonos = []
for cont in range (1,4):
	nombre = input (f"Ingrese el nombre de la persona numero {cont}:  ")
	nombres.append (nombre)
	
	apellido = input (f"Ingrese el apellido de la persona numero {cont}:  ")
	apellidos.append (apellido)
	
	telefono = input (f"Ingrese el telefono de la persona numero {cont}:  ")
	telefonos.append (telefono)
persona = str (input ("A quien busca?"))
while persona in nombres:
	ubicacionNombre = int (nombres.index (persona))
	print (f"Su apellido es {apellidos [ubicacionNombre]}  y su num de tel es:  {telefonos [ubicacionNombre]} ")
	break
else:
	print ("No Esta en la lista")
		
		
	
	
