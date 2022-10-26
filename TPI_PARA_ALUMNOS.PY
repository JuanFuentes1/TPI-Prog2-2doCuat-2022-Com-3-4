import os
from Auto import Automovil
from Motos import Moto
from conexiones import Conexiones

class ProgramaPrincipal:

    def menu(self):
        while True:
            clearConsole()
            print("---Menu de opciones Concesionaria---\n")
            print("1- Cargar Automoviles")
            print("2- Modificar Automoviles")
            print("3- Eliminar Automoviles")
            print("4- Cargar disponibilidad Autos")
            print("5- Mostrar Automoviles")
            print("6- Cargar Motos")
            print("7- Modificar Motos")
            print("8- Eliminar Motos")
            print("9- Cargar disponibilidad Motos")
            print("10- Mostrar Motos")
            print("11- Mostrar registro historico Motos")
            print("12- Registro de modificaciones por fechas.")
            print("0- Salir de menu")
            nro = int(input("\nPor favor ingrese una opción: "))
            if nro == 1:
                clearConsole()
                print("--Cargar Automoviles--")
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                precio = input("Por favor ingrese el precio del automovil: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
                os.system("Pause")
            if nro == 2:
                clearConsole()
                print("--Modificar Automoviles--")
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar=Automovil(marca,modelo,precio)
                automovil_a_modificar.modificar_automoviles()
                os.system("Pause")
            if nro == 3:
                clearConsole()
                print("--Eliminar Automovil--")
                marca = input("Por favor ingrese el nombre de la marca del automovil a eliminar: ")
                modelo = input("Por favor ingrese el nombre del modelo ha eliminar: ")
                automovil_a_eliminar=Automovil(marca,modelo)
                automovil_a_eliminar.eliminar_automovil()
                os.system("Pause")
            if nro==4:
                clearConsole()            
                print("--Cargar Disponibilidad Autos--")
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                automovil_disponibles=Automovil(marca,modelo)
                automovil_disponibles.cargar_disponibilidad()
                os.system("Pause")
            if nro == 5:
                clearConsole()
                print("--Mostrar Automoviles--")
                Automovil.mostrar_automoviles()
                os.system("Pause")
            if nro == 6: 
                clearConsole()
                print("--Cargar Motos--")
                marca = input("Por favor ingrese la marca de la moto: ")
                modelo = input("Por favor ingrese el modelo de la moto: ")
                precio = input("Por favor ingrese el precio de la moto: ")
                color = input("Por favor ingrese el color: ")
                cilindrada = input("Por favor ingrese la cilindrada: ")
                cantidadDisponibles = input("Por favor ingrese el stock: ")
                fecha = input("Por favor ingrese la fecha del ultimo precio: ")
                nueva_moto = Moto(marca,modelo,precio,color,cilindrada,cantidadDisponibles,fecha)
                nueva_moto.cargar_moto()
                os.system("Pause")
            if nro == 7:
                clearConsole()
                print("--Modificar Motos--")
                print("Actualizando registros historicos.")
                Moto.registrar_historicos(self)
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                fecha = input("Por favor ingrese la fecha de la modificacion: ")
                moto_a_modificar=Moto(marca,modelo,precio,color,cilindrada,cantidadDisponibles,fecha)
                moto_a_modificar.modificar_motos()
                os.system("Pause")
            if nro == 8:
                clearConsole()
                print("--Eliminar Motos--")
                marca = input("Por favor ingrese el nombre de la marca del automovil a eliminar: ")
                modelo = input("Por favor ingrese el nombre del modelo ha eliminar: ")
                moto_a_eliminar=Moto(marca,modelo)
                moto_a_eliminar.eliminar_motos()
                os.system("Pause")
            if nro==9:
                clearConsole()            
                print("--Cargar disponibilidad Motos--")
                marca = input("Por favor ingrese la marca de la moto: ")
                modelo = input("Por favor ingrese el modelo de la moto: ")
                motos_disponibles=Moto(marca,modelo,precio,color,cilindrada,cantidadDisponibles,fecha)
                motos_disponibles.cargar_disponibilidad()
                os.system("Pause")
            if nro == 10:
                clearConsole()
                print("--Mostrar Motos--")
                Moto.mostrar_motos()
                os.system("Pause")
            if nro == 11:
                clearConsole()
                print("--Mostrar Registro Historico Motos--")
                Moto.mostrar_motos_historico()
                os.system("Pause")
            if nro == 12:
                clearConsole()
                print("Registro por fechas\n")
                fecha = input('Ingrese la fecha: ')
                registro_fechas = Moto(marca,modelo,precio,color,cilindrada,cantidadDisponibles,fecha)
                registro_fechas.mostrar_motos_fecha()
                os.system("Pause")
            if nro == 0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30), precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()
    
    def crearTablas2(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS Moto")
        conexion.miCursor.execute("CREATE TABLE Moto (id_moto INTEGER PRIMARY KEY, marca VARCHAR(30), modelo VARCHAR(30), precio INTEGER, color VARCHAR(30), cilindrada VARCHAR(30), cantidadDisponibles INTEGER, fecha DATETIME)")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()
    
    def crearTablas3(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS historico_motocicletas")
        conexion.miCursor.execute("CREATE TABLE historico_motocicletas (id_moto INTEGER PRIMARY KEY, marca VARCHAR(30), modelo VARCHAR(30), precio INTEGER, color VARCHAR(30), cilindrada VARCHAR(30), cantidadDisponibles INTEGER, fecha DATETIME)")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

clearConsole()

         
programa = ProgramaPrincipal()
programa.crearTablas()
programa.crearTablas2()
programa.crearTablas3()
programa.menu()