def situacion_vivenciada():
        """la funcion solicitara el tipo de situacion vivenciada
que sufrio ante la persona que esta denunciando"""
        situacion = input("Ingrese la situacion(vs: Violencia Sexual”, “as: Acoso Sexual”, “cs: Connotación Sexista”, “ca_v: Comportamientos y Acciones de violencia: ")
        
        while (situacion != "vs" ) and (situacion != "as" ) and (situacion != "cs" )and (situacion != "ca_v" ):
                print("Situacion invalida, por favor introduzca de nuevo su situacion")
                situacion =input("Ingrese la situacion(vs: Violencia Sexual”, “as: Acoso Sexual”, “cs: Connotación Sexista”, “ca_v: Comportamientos y Acciones de violencia: ")
        
        return situacion

def cadena_a_numeros(cadena,cont_mas_1_tipo):
        cant_vacios= 0
        cant_den_situ =0
        for elem in cadena:
                if elem == "":
                        cant_vacios += 1
        if cant_vacios <3:
                cant_den_situ = cont_mas_1_tipo + cant_den_situ
                return cant_den_situ