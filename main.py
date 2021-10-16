
##################################################################
#Trabajo numero 5 de Programación en la capacitación TICS
#Nombre: Israel Jonathan Chávez González
#Matricula: 11840280
#Grupo: 507 Vespertino 
###################################################################

import os
import time

PI = 3.1416
n = 0

while n == 0:
    
    #Bienvenida
    os.system("cls")
    print("\nHola, espero que estes bien, soy un programa hecho por Israel Jonathan Chávez Gonzalez - 11840280\nTengo la funcion de calcular el area de un cilindro :)\n\n1) Para continuar\n2) Para salir\n")
    c = input("\nEija una de las opciones: ")
    if c == '1':
        
        #Continuación
        os.system("cls")
        print("Bienvenid@, quisiera saber su nombre :)\n")
        name = input("Su nombre: ")
        os.system("cls")
        print(f"¡Me da gusto seguir teniendote aqui {name.title()}!\n\nAhora calcularemos el area de un cilindro, deberas proporcionarme los siguientes datos:\n\n1) Altura en centimetos\n2) Radio de alguna de las bases en centimetros\n")
        time.sleep(5)
        
        #Captura de datos 
        altura = int(input("Altura: "))
        radio = int(input("Radio: "))
        os.system("cls")
        print("¡Comencemos!")
        time.sleep(2)
        os.system("cls")
        print(f"Ahora trabajare con {altura}cm de altura y {radio}cm de radio")
        time.sleep(2)
        os.system("cls")
        print("Estoy haciendo las operaciones correspondientes...\n")
        
        #Proceso de calculo
        hr = altura + radio
        resultado = 2 * PI * radio * hr
        time.sleep(5)
        os.system("cls")
        print(f"El area del cilindro es: {float(resultado)}cm^2\n\n")
        time.sleep(5)
        print("Si desea hacer otro calculo solo de enter, de lo contrario escriba 0")
        r = input("¿Que desea hacer?: ")
        if r == '0':
            n = 1
        else:
            pass
    else:
        n = 1
else:
    #Despedida
    os.system("cls")
    print("\n\n\nFue un placer, adios <3\n\n\n")
    os.system("exit")
