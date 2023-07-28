def ingresar_anio():
    '''Esta función pide al usuario el año y lo devuelve verificado.'''
    anio= int(input('Ingrese el año(2021 en adelante):'))
    while anio < 2021:
        print ("Año menor a 2021")
        anio= int(input('Ingrese el año(2021 en adelante):'))
    if anio >= 2021:
        return anio
    return anio

def ingresar_semestre():
    '''Esta función pide al usuario que ingrese el semestre, 1 o 2, y lo devuelve verificado.'''
    semestre= int(input('Ingrese el semestre(1 o 2):'))
    while semestre != 1 and semestre != 2:
        print ('Incorrecto, ingrese el semestre(1 o 2).')
        semestre= int(input('Ingrese el semestre(1 o 2):'))
    if semestre ==1 or semestre ==2:
        return semestre

def dar_dia(mes, anio):
    '''Esta función recibe por parametro, mes y año, devuelve el dia verificado.'''
    bisiesto= False
    if anio % 400 == 0 or (anio % 100 != 0 and anio % 4 ==0):
        bisiesto= True
    
    if mes == 2:
        if bisiesto== True:
            dia=29
        else:
            dia=28
    elif mes==4 or mes==6 or mes==9 or mes==11:
        dia = 30
    else:
        dia = 31
    return dia