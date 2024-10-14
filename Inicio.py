#Entrada de datos: 
Nombre = str(input("Ingresa tu nombre: "))
Edad = int(input("Ingresa tu edad: "))
Salario = float(input("Ingresa tu salario mensual: "))
HorasTrabajadas = int(input("Ingresa tus horas trabajadas por semana: "))
#Funciones: 
Edad5Años = Edad+5
SalarioAnual = Salario*12
SalarioHora = (Salario/31)/12
#Salida:
print(" ¡¡HOLA "+Nombre+"!! ")
print(" ¡¡En 5 años tendrás "+str(Edad5Años)+" años!! ")
print(" ¡¡Tu salario anual será de: "+str(SalarioAnual)+" pesos!! ")
print(" ¡¡Tu salario por hora es de: "+str(SalarioHora)+" pesos!!")