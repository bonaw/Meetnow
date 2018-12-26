# -*- coding: cp1252 -*-
#recepcion de los datos

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




#Filtro de Horario via "Split" a Horario Militar

