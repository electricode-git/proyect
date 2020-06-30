	#Ej_Arrays_Ej_006
print('Array Nombres = "Juan,"Juana","Andrea","Andres","Martin","Martina","Joaquin","Julia","Julio","Facundo"');
print("Ingresa un nombre, ponlo en capitalize ");
print ("Busco si el dato 'nombre' esta en mi Array con print");
print ('print("Nombre" in Nombres);');

Nombres= ["Juan","Juana","Andrea","Andres","Martin","Martina","Joaquin","Julia","Julio","Facundo"]
Nombre= str (input ("ingrese un nombre:"))
Nombre= Nombre.capitalize ()
if Nombre in Nombres:
	print (Nombre)

