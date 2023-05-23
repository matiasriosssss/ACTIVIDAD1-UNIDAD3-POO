from manejadorFacultades import ManejadorFacultades
if __name__ == '__main__':
    mF = ManejadorFacultades()
    mF.carga()
    
    print("""
    ----MENU----
    1_ Mostrar nombre, carreras y duracion de las carreras que hay en una facultad 
    2_ Codigo, Nombre y localidad de la facultad donde se dicta una carrera 
    0_ FIN
          """)
    o = int(input("Ingrese opcion deseada: "))
    
    if o == 1:
        cod = int(input("Ingrese codigo de la facultad: "))
        mF.opcion1(cod)
    elif o == 2:
        nom = input("Ingrese nombre de la carrera de la que solicita informacion: ")
        mF.opcion2(nom)
    elif o == 0:
        exit()
    else:
        print("Opcion invalida...")