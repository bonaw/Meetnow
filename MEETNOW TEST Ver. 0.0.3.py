# -*- coding: cp1252 -*-

#SETUP
from datetime import datetime, date, time, timedelta
import calendar

#Creacion de usuarios
usuarios = []
init=raw_input("¿Tienes un usuario?")
if(init=="si" or init=="Si"):
	#CODIGO DE INICIO DE SESION FALTANTE
	pass

else:
	nombre=raw_input("Ingresa tu nombre de usuario: ") #GUARDA USER EN LISTA
	usuarios.append(nombre)	
	passw=raw_input("Ingresa tu password")			   #GUARDA PASS EN LISTA
	usuarios[0].append(passw)
	email=raw_input("Ingresa tu email: ")			   #GUARDA EMAIL EN LISTA
	usuarios[0].append(email)

#Recepcion de los datos

#LUNES
lunes=[]
q=raw_input("¿Tienes horarios libres el Lunes? Si/No")
if(q=="si" or q=="Si"):
    x=input("¿Cuantos horarios libres tienes este Lunes?")
    for i in range(x):
        lunes.append(raw_input("Ingresa un rango de horario libre(Ej: 13:00-14:00)"))
else:
    pass


#MARTES
martes=[]
q=raw_input("¿Tienes horarios libres el Martes? Si/No")
if(q=="si" or q=="Si"):
    x=input("¿Cuantos horarios libres tienes este Martes?")
    for i in range(x):
        martes.append(raw_input("Ingresa un rango de horario libre(Ej: 13:00-14:00)"))
else:
    pass


#MIERCOLES
miercoles=[]
q=raw_input("¿Tienes horarios libres el Miercoles? Si/No")
if(q=="si" or q=="Si"):
    x=input("¿Cuantos horarios libres tienes este Miercoles?")
    for i in range(x):
        miercoles.append(raw_input("Ingresa un rango de horario libre(Ej: 13:00-14:00)"))
else:
    pass


#JUEVES
jueves=[]
q=raw_input("¿Tienes horarios libres el Jueves? Si/No")
if(q=="si" or q=="Si"):
    x=input("¿Cuantos horarios libres tienes este Jueves?")
    for i in range(x):
        jueves.append(raw_input("Ingresa un rango de horario libre(Ej: 13:00-14:00)"))
else:
    pass

#VIERNES
viernes=[]
q=raw_input("¿Tienes horarios libres el Viernes? Si/No")
if(q=="si" or q=="Si"):
    x=input("¿Cuantos horarios libres tienes este Viernes?")
    for i in range(x):
        viernes.append(raw_input("Ingresa un rango de horario libre(Ej: 13:00-14:00)"))
else:
    pass


#SABADO
sabado=[]
q=raw_input("¿Tienes horarios libres el Sabado? Si/No")
if(q=="si" or q=="Si"):
    x=input("¿Cuantos horarios libres tienes este Sabado?")
    for i in range(x):
        sabado.append(raw_input("Ingresa un rango de horario libre(Ej: 13:00-14:00)"))
else:
    pass


#DOMINGO
domingo=[]
q=raw_input("¿Tienes horarios libres el Domingo? Si/No")
if(q=="si" or q=="Si"):
    x=input("¿Cuantos horarios libres tienes este Domingo?")
    for i in range(x):
        domingo.append(raw_input("Ingresa un rango de horario libre(Ej: 13:00-14:00)"))
else:
    pass

lista=[lunes,martes,miercoles,jueves,viernes,sabado,domingo]


#Filtro de Horario via "Split"

	#LUNES
		#Los datos llegan como 12:00 - 15:00 y salen como 12:00,15:00 u 12; 00; 15; 00;
lunes_rangos=[]

for i in lunes:
	lunes_rangos.append(i.split("-"))

lunes_datospequenos=[]
for i in lunes_rangos:
	for f in i:
		lunes_datospequenos.append(f.split(":"))


	#MARTES
		#Los datos llegan como 12:00 - 15:00 y salen como 12:00,15:00
martes_rangos=[]

for i in martes:
	martes_rangos.append(i.split("-"))

martes_datospequenos=[]
for i in martes_rangos:
	for f in i:
		martes_datospequenos.append(f.split(":"))


	#MIERCOLES
		#Los datos llegan como 12:00 - 15:00 y salen como 12:00,15:00
miercoles_rangos=[]

for i in miercoles:
	miercoles_rangos.append(i.split("-"))

miercoles_datospequenos=[]
for i in miercoles_rangos:
	for f in i:
		miercoles_datospequenos.append(f.split(":"))


	#JUEVES
		#Los datos llegan como 12:00 - 15:00 y salen como 12:00,15:00
jueves_rangos=[]

for i in jueves:
	jueves_rangos.append(i.split("-"))

jueves_datospequenos=[]
for i in jueves_rangos:
	for f in i:
		jueves_datospequenos.append(f.split(":"))


	#VIERNES
		#Los datos llegan como 12:00 - 15:00 y salen como 12:00,15:00
viernes_rangos=[]

for i in viernes:
	viernes_rangos.append(i.split("-"))

viernes_datospequenos=[]
for i in viernes_rangos:
	for f in i:
		viernes_datospequenos.append(f.split(":"))


	#SABADO
		#Los datos llegan como 12:00 - 15:00 y salen como 12:00,15:00
sabado_rangos=[]

for i in sabado:
	sabado_rangos.append(i.split("-"))

sabado_datospequenos=[]
for i in sabado_rangos:
	for f in i:
		sabado_datospequenos.append(f.split(":"))


	#DOMINGO
		#Los datos llegan como 12:00 - 15:00 y salen como 12:00,15:00
domingo_rangos=[]

for i in domingo:
	domingo_rangos.append(i.split("-"))

domingo_datospequenos=[]
for i in domingo_rangos:
	for f in i:
		domingo_datospequenos.append(f.split(":"))

#FIN SPLIT DE DATOS
#HOLA MAMI ESTOY EN UN PROGRAMA.- Rafael Perez 2017.-

usuarioA=[lunes_datospequenos, martes_datospequenos, miercoles_datospequenos, jueves_datospequenos, viernes_datospequenos, sabado_datospequenos, domingo_datospequenos]

#para salida se incluyen los mismos datos de usuarioA en una lista con su numero de usuario 
#obtencion de numero de usuario
numerouser=usuarioA

#algoritmo comparador

#incluir descarga de usuarioB desde base de datos 
#al entrar usuarioB entra como lista con su numero de usuario y cambia su nombre localmente a usuarioB
#usuarioB sera el usuario selecionado con el que la persona se quiere reunir
#los datos de usuario b entran desde su numero de usuario asignado en su registro

usuarioB=[] #incluir numero de usuario en corchetes para referir a sus datos