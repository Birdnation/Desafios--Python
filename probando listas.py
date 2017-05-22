#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:08:01 2017

@author: rodrigo
"""
#Almacenamiento de los datos
idVuelo = []        #Almacena las ID del vuelo
cantPasajero = []   #Almacena la cantidad de pasajeros por vuelo
ciudadOrigen = []   #Almacena las ciudades de origen por vuelo
ciudadDestino = []  #Almacena las ciudades de destino por vuelo
duracion = []       #Almacena las duraciones por vuelo
duracion2 = []      #Almacena las duraciones de la condicion if (**)

#Ingreso al while
numVuelo = ""       #Variable auxiliar para ingresar al while
while numVuelo != "-1":     #Verificar la variable si es diferente de la condicion de salida -1
    numVuelo = input(\
    "Por favor ingrese el numero de vuelo "\
    "(Si no desea agregar mas vuelos ingrese valor -1): ")                  #Variable para el ID de vuelo
    if numVuelo != "-1":                                                    #Verificar la condicion de salida
        if numVuelo in idVuelo:                                             #If para verificar si el vuelo ya existe
            print ("El numero de vuelo ya existe.")                         #Si ya existe
        else:
            canPas = int(input("Ingrese la cantidad de pasajeros: "))       #Variable para la cantidad de pasajeros
            ciuOrig = input("Ingrese la ciudad de origen: ")                #Variable para la ciudad de origen
            ciuDest = input("Ingrese la ciudad de destino: ")               #Variable para la ciudad de Destino
            durac = int(input("Ingrese la duracion del vuelo: "))           #Variable para la duracion
            cantPasajero.append(canPas)             #Agregar la cantidad de pasajeros al almacenamiento en lista
            ciudadOrigen.append(ciuOrig)            #Agregar la ciudad de origen al almacenamiento en lista
            ciudadDestino.append(ciuDest)           #Agregar la ciudad de destino al almacenamiento en lista
            duracion.append(durac)                  #Agregar la duracion al almacenamiento en lista
            idVuelo.append(numVuelo)                #Agregar la ID de vuelo al almacenamiento en lista
            if ciuOrig == "Antofagasta" and ciuDest == "Santiago de Chile": #(**) Verifica la condicion origen y destino a la vez
                duracion2.append(durac)             #Agregar la duracion al almacenamiento en lista
print ("")
print ("Resultados".center(50,"#"))                 #Barra de Resultados
print ("La cantidad de vuelos realizados es: " + str(len(idVuelo)))             #Muestra la cantidad de Vuelos (a)
print ("El vuelo con la mayor cantidad de pasajeros transportados es: ID" + \
       str(idVuelo[cantPasajero.index(max(cantPasajero))]) + ", Con " + \
       str(cantPasajero[cantPasajero.index(max(cantPasajero))]) + \
       " Pasajeros transportados.")                                             #(b)

print ("")
contar = ciudadDestino.count("Logoño")
porcentajeLogoño = (contar / len(idVuelo)) * 100
print ("El porcentaje de vuelos a Logoño fue de: " + \
       str(porcentajeLogoño) + "%")                                             #(c)
print ("")

suma = 0                #Variable auxiliar
for i in duracion:      
    suma = suma + i
promDuracion = suma / len(duracion)
print ("La duracion promedio de todos los vuelos es de :" \
       + str(promDuracion) + "Horas")                                           #(d)

suma2 = 0
for u in duracion2:
    suma2 = suma2 + u
print ("")
print ("la cantidad total de pasajeros transportados desde" + \
       "Antofagasta a Santiago es: " + str(suma2) + " Personas")                #(e)
