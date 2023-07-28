def pedir_claustro():
        """La función solicitara el claustro de
la persona denunciante (e: estudiante, n: no-docente, d: docente, g: graduade)"""
        claustro = input("Ingrese su claustro(e: estudiante, n: no-docente, d: docente, g: graduade): ")
        while (claustro != "e" ) and (claustro != "n" ) and (claustro != "d" )and (claustro != "g" ):
                print("Claustro invalido, por favor introduzca de nuevo su claustro")
                claustro = input("Ingrese su claustro(e: estudiante, n: no-docente, d: docente, g: graduade): ")
        if claustro == "e":
                c= "estudiante"
                #print("estudiante")
        elif claustro == "n":
                c= "no docente"
                #print("no docente")
        elif claustro == "d":
                c= "docente"
                #print("docente")
        elif claustro == "g":
                c= "graduade"
                #print("graduade")
        return claustro

def pedir_genero():
        """La función solicitara el género auto-percibido de la persona denunciante
(m: mujer, v:  varón, x: otre)"""
        '''cont_varon=0
        cont_mujer=0
        cont_otre=0'''
        gen = input("Ingrese su genero(m: mujer, v:  varón, x: otre): ")
        while (gen!="m") and (gen !="v") and (gen !="x"):
                print("Género invalido, por favor introduzca de nuevo su género")
                gen = input("Ingrese su genero(m: mujer, v:  varón, x: otre): ")
        if gen == "m":
                g= "Mujer"
                #print("Mujer")
        elif gen == "v":
                g= "varón"
                #print("Varon")
        elif gen == "x":
                g= "Otre"
                #print("Otre")
        return gen