import funciones as func

#Registro de Consumo/Jugadores

ListaConsumo = []

while True:
    func.menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1": #Registro de jugadores
        func.registrocons(ListaConsumo)
    elif opcion == "2": #Listar jugadores
        func.listar(ListaConsumo)
    elif opcion == "3": #imprimir hoja consumo
        func.imprtxt(ListaConsumo)
    elif opcion == "4": #Buscar consumo por id 
        func.idsearch(ListaConsumo)    
    elif opcion == "5": #Salir del programa
        print("Saliendo")
        break