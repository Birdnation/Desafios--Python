# -*- coding: utf-8 -*-
#@author: Rodrigo Dominguez Rut: 17392282-5
#Desafio 4 Calculo geometria de un circulo de radio R
import os

#Mensaje de Bienvenida
print ("#".center(63,"#"))
print ("#  Programa para calcular Geometria de un circulo de radio R  #")
print ("#".center(63,"#"))
print ("")
radio = int(input("Ingrese el valor del radio en (cm): "))
pi = 3.1416

#Creacion del menu
def menu():

    print ("")
    print ("Radio introducido: " + str(radio) + "(cm)")
    print ("Selecciona una opción")
    print ("\t1 - Calculo de diametro")
    print ("\t2 - Calculo de perimetro")
    print ("\t3 - Calculo de área")
    print ("\t0 - Reingresar radio")
    print ("\t9 - salir")
    
while True:

    #muestra el menu
    menu()
    
    #solicitar opcion
    opcionMenu = input("ingrese un numero y precione enter >>")
    
    #Calculo diametro
    if opcionMenu == "1":
        diametro = radio * 2
        print ("")
        print ("Has seleccionado el diametro...")
        print ("El diametro del circulo de radio: " + str(radio) + "(cm) es: " + str(diametro) + "(cm)")
        print ("")
        input ("Presiona enter para continuar...")
        os.system("cls") #limpiar la pantalla //nota si os es diferente de windows use crear en vez de cls
    #Calculo perimetro
    elif opcionMenu == "2":
        perimetro = 2 * pi * radio
        perimetro = round (perimetro,2)
        print ("")
        print ("Has seleccionado el perimetro...")
        print ("El perimetro de un circulo de radio: " + str(radio) + "(cm) es: " + str(perimetro) + "(cm)")
        print ("")
        input ("Presiona enter para continuar...")
        os.system("cls") #limpiar la pantalla
    #Calculo Area    
    elif opcionMenu == "3":
        area = pi * (radio ** 2)
        area = round (area,2)
        print ("")
        print ("Has seleccionado el área")
        print ("El area de un circulo de radio: " + str(radio) + "(cm) es: " + str(area) + "(cm^2)")
        print ("")
        input ("Presiona enter para continuar...")
        os.system("cls") #limpiar la pantalla
    #Ninguna de las anteriores
    elif opcionMenu == "9":
        print ("")
        print ("Hasta luego...")
        break
    
    #Cambiar valor del radio
    elif opcionMenu == "0":
        print ("")
        radio = int(input ("Ingrese el valor del radio en (cm): "))
        input ("Presiona enter para continuar...")
        os.system("cls") #limpiar la pantalla
        
    else:
         print ("")
         input("No has pulsado ninguna opción correcta...\nPresiona enter para continuar...")
         os.system("cls") #limpiar la pantalla
