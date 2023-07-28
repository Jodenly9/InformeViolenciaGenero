from com1_a import pedir_genero
from com1_a import pedir_claustro
from com1_f import situacion_vivenciada
from com1_f import cadena_a_numeros
from com1_l import ingresar_anio
from com1_l import ingresar_semestre

from com1_p import pedir_dia
from com1_p import pedir_mes

def main():
    '''El Programa le pedira al usuario que ingrese datos,que generara
un informe semestral de denuncias de violencia de genero y si un dato no es valido,
se pedira su reingreso hasta cumplir los requisitos de validez'''
    print("\n")
    print("Bienvenidos al Programa Transversal de Políticas de Género y Diversidad")
    print("\n")
    cont_denuncias=0
    cont_varon=0
    cont_mujer=0
    cont_otre=0
    cont_est=0
    cont_nodoc=0
    cont_doc=0
    cont_graduad=0
    cant_den_pares_mismo_claustro = 0
    cont_mas_1_tipo = 0
    anio= ingresar_anio()
    semestre= ingresar_semestre()
    max_exp = 0
    n_exp= int(input("Ingrese el número de expediente(0 para terminar):"))
    while n_exp > 0:
        if n_exp>= max_exp:
            max_exp= n_exp

        mes= pedir_mes(semestre)    
        dia= pedir_dia(mes,anio)
        
        cont_denuncias += 1
        print ('Ingrese los datos de la persona denunciante')
        genero_dte= pedir_genero()
        claustro_dte= pedir_claustro()
        if genero_dte == "v":
            cont_varon+= 1
        elif genero_dte == "m":
            cont_mujer+= 1
        else:
            cont_otre+= 1

        if claustro_dte == "e":
            cont_est+= 1
        elif claustro_dte == "n":
            cont_nodoc+= 1
        elif claustro_dte == "d":
            cont_doc+= 1    
        else:
            cont_graduad+=1
        cadena= ''
        cont= 1
        sit = situacion_vivenciada()
        
        cadena = cadena + sit
        seguir = input("Quiere seguir cargando tipos diferentes?(S para continuar, cualquier tecla para terminar)")
        while seguir== "S":
            sit = situacion_vivenciada()
            if sit not in cadena:
                cadena = cadena+"," + sit
                cont += 1
            seguir = input("Quiere seguir cargando tipos diferentes?(S para continuar, cualquier tecla para terminar):")

        if cont >=2:
            cont_mas_1_tipo += 1
        
        cant_den_situ= cadena_a_numeros(cadena,cont_mas_1_tipo)
        
        print('\n')
        print ('Ingrese los datos de la persona denunciada')
        genero_dda= pedir_genero()
        claustro_dda= pedir_claustro()
        
        
        print('\n')
        print("Numero de expediente:", n_exp)
        print('Denunciante')
        print('Género:',genero_dte)
        print('Claustro: ',claustro_dte)
        print('Fecha de denuncia:', dia,'/',mes,'/',anio )
        print('Denunciade')
        print('Género:',genero_dda)
        print('Claustro:',claustro_dda)
        print('Situaciones vivenciada:',cadena)        
        print('\n')
        print('¿Quiere cargar una nueva denuncia?')
        n_exp= int(input("Ingrese el número de expediente(0 para terminar):"))

        if claustro_dte == claustro_dda:
            cant_den_pares_mismo_claustro += 1
        porcentaje = cant_den_situ * 100 / cont_denuncias
    
    

    print('\n')
        
    print('Cantidad de denuncias:',cont_denuncias)
    print('Cantidad de denunciantes varones:',cont_varon)
    print('Cantidad de denunciantes mujeres:',cont_mujer)
    print('Cantidad de denunciantes otres:',cont_otre)
    print('Cantidad de denunciantes estudiantes:',cont_est)
    print('Cantidad de denunciantes no-docentes:',cont_nodoc)
    print('Cantidad de denunciantes docentes:',cont_doc)
    print('Cantidad de denunciantes graduados:',cont_graduad)
    print('\n')
    
    print('Porcentaje de situaciones múltiples:',porcentaje)
    print('Cantidad de denuncias entre pares del mismo claustro:',cant_den_pares_mismo_claustro)
    print("El numero maximo de expediente es:", max_exp)
    


main()