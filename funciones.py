import random
#150 lineas ke no sirven jijiji

#ID RANDOM
def codigoran():
    code = random.randint(1000,9999)
    return code

def menu():
    print("1.	Registrar consumo")
    print("2.	Listar los todos los consumos")
    print("3.	Imprimir hoja consumo")
    print("4.	Buscar un consumo por ID")
    print("5.	Salir del programa")
def registrocons(lista:list):
    id = codigoran()
    
    while True:
        nombre = input("Ingrese nombre del jugador: ")
        if nombre != "" and nombre.isalpha():
            break
        else:
            continue
    while True:
        apellido = input("Ingrese apellido del jugador: ")
        if apellido != "" and apellido.isalpha():
            break
        else:
            continue
    nombre_completo = nombre + " " + apellido  
    while True: #Edad Jugador
        try:
            edad = int (input("Ingrese edad: "))
            if edad > 0:
                break
            elif edad == 0 and edad < 0:
                continue
        except:
            print("Error")
            continue
    while True:
        print("1. Los Genios de la garrafa")
        print("2. Los Compiladores Despiertos")
        print("3. Código Borracho")
        print("4. Los programadores perezosos")
        print("5. Ctrl+Alt+Derrota")
        try:
            opc = int(input("¿A que equipo pertenece?\n"))
            if opc == 1:
                equipo = "Los Genios de la Garrafa"
                break
            elif opc == 2:
                equipo = "Los Compiladores Despiertos"
                break
            elif opc == 3:
                equipo = "Código Borracho"
                break
            elif opc == 4:
                equipo = "Los Programadores Perezosos"
                break
            elif opc == 5:
                equipo = "Ctrl+Alt+Derrota"
                break
        except:
            print("Error")
            continue
    while True:
        try:
            viernes = int(input("Consumo día viernes: "))
            if viernes >= 0:
                break
            elif viernes < 0:
                continue
        except:
            print("Error")    
    while True:
        try:
            sabado = int(input("Consumo día Sábado: "))
            if sabado >= 0:
                break
            elif sabado < 0:
                continue
        except:
            print("Error") 
    while True:
        try:
            domingo = int(input("Consumo día Domingo: "))
            if domingo >= 0:
                break
            elif domingo < 0:
                continue
        except:
            print("Error") 
    total = viernes + sabado + domingo
    if total >= 3:
            lista.append([id,nombre_completo,edad,equipo,viernes,sabado,domingo])
    else:
        print("No aplica")
    

def listar(lista):
    print("ID Consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSabado\tDomingo")
    for user in lista:
        print(f"{user[0]}\t\t{user[1]}\t{user[2]}\t{user[3]}\t{user[4]}\t{user[5]}\t{user[6]}")


def idsearch(lista): #AYUDAAAAAA
    try:
        id = int(input("Ingrese ID: "))
        if id == codigoran() in lista:
            print("ID Consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSabado\tDomingo")
            for user in lista:
                for codigo in user:
                    print(f"{user[0]}\t\t{user[1]}\t{user[2]}\t{user[3]}\t\t{user[4]}")
                    break
        else:
            print("ID No encontrada")
    except:
        print("Error")
                
#with open("planilla.csv", "w", newline="") as archivo: #Ni idea papito no me acuerdo del csv
    print("")

def imprtxt(lista): #Imprimir por Equipo
    while True:
        print("1. Los Genios de la garrafa")
        print("2. Los Compiladores Despiertos")
        print("3. Código Borracho")
        print("4. Los programadores perezosos")
        print("5. Ctrl+Alt+Derrota")
        try:
                opc = int(input("¿De que equipo desea la plantilla?\n"))
                if opc == 1:
                    with open("Los Genios de la Garrafa.csv", "w", newline="") as archivo:
                        archivo.write(f"ID Consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSabado\tDomingo")
                        for user in lista:
                            archivo.write(print(f"{user[0]}\t\t{user[1]}\t{user[2]}\t{user[3]}\t{user[4]}\t{user[5]}\t{user[6]}"))
                        break
                elif opc == 2:
                    with open("Los Compiladores Despiertos.csv", "w", newline="") as archivo:
                        archivo.write(f"ID Consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSabado\tDomingo")
                        archivo.write(f"")
                        break
                elif opc == 3:
                    with open("Código Borracho.csv", "w", newline="") as archivo:
                        archivo.write(f"ID Consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSabado\tDomingo")
                        archivo.write(f"")
                        break
                elif opc == 4:
                    with open("Los Programadores Perezosos.csv", "w", newline="") as archivo:
                        archivo.write(f"ID Consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSabado\tDomingo")
                        archivo.write(f"")
                        break
                elif opc == 5:
                    with open("Ctrl+Alt+Derrota.csv", "w", newline="") as archivo:
                        
                        archivo.write(f"ID Consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSabado\tDomingo")
                        archivo.write(f"")
                        break
        except:
                print("Error")
                continue