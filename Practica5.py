dias =["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
nombre = []
kms = []

while True:
	num_conductores = int(input("Cuantos conductores tiene la empresa?:"))
	if num_conductores>0: break


for indice_cond in range(0,num_conductores):
	nombre.append(input("Nombre del conductor %d:" % (indice_cond + 1)))
	
	km_dias = []
	for indice_dias in range(0,7):
		km_dias.append(int(input("Cuantos km ha realizado el %s?:" % dias[indice_dias])))
	kms.append(km_dias)

total_kms = []
for km in kms:
	total_kms.append(sum(km))

for nombre, km in zip(nombre, total_kms):
	print("%s  ha realizado %d kms." % (nombre,km))
    

