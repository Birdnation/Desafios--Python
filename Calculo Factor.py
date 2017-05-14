#Created on Sat May  6 22:56:43 2017
#@author: Rodrigo Dominguez Rut: 17392282-5
#Desafio 3 Calculo del factor Programacion
import time

valX = input ("Ingrese valor de x:")
valY = input ("Ingrese valor de y:")
valZ = input ("ingrese valor de z:")

calculoFactor = (((((int(valX) ** int(valZ)) / int(valY)) + (int(valZ) ** 2)) ** 2) - ((int(valX) + int(valY)) ** 2))
print ("Calculo a realizar:\n[(((X^Z)/Y)+Z^2)]^2 - (X-Y)^2")
print ("Calculando...")
time.sleep(3.0)
print ("Resultado: " + str(calculoFactor))