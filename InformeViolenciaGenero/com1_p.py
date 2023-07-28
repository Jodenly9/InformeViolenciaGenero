from com1_l import dar_dia

def pedir_dia(mm,aa): 
        """La funcion solicitara el dia de la denuncia, a la persona denunciante,
cual esta representada en dia como dd"""
        dia = int(input("Ingrese el dia: "))
        max_dia= dar_dia(mm,aa)
        while dia <=0 or dia > max_dia:
                print("Dia incorecto")
                dia = int(input("Ingrese el dia: "))
        return dia

def pedir_mes(semestre):
        """La funcion solicitara el mes de la denuncia, a la persona denunciante,
cual esta representada en mes como mm"""
        mes = int(input("Ingrese el mes: "))
        while (mes <= 0 or mes > 12) or (mes >=1 and mes <=6 and semestre== 2 ) or (mes >=7 and mes<=12 and semestre== 1):
                print("Mes incorrecto")
                mes = int(input("Ingrese el mes: "))
        return mes