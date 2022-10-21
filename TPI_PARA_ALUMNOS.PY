import sqlite3
import os

class ProgramaPrincipal:

    def menu(self):
        while True:
            clearConsole()
            print("---Menu de opciones Concesionaria---\n")
            print("1- Cargar Automoviles")
            print("2- Modificar Automoviles")
            print("3- Eliminar Automoviles")
            print("5- Mostrar Automoviles")
            print("6- Cargar Motos")
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
            if nro == 2:
                clearConsole()
                print("--Modificar Automoviles--")
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar=Automovil(marca,modelo,precio)
                automovil_a_modificar.modificar_automoviles()
            if nro == 3:
                clearConsole()
                print("--Eliminar Automovil--")
                marca = input("Por favor ingrese el nombre de la marca del automovil a eliminar: ")
                modelo = input("Por favor ingrese el nombre del modelo ha eliminar: ")
                automovil_a_eliminar=Automovil(marca,modelo)
                automovil_a_eliminar.eliminar_automovil()
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
                fecha = input("Por favor ingrese la fecha del ultimo precio: ")
                nuevo_automovil = Moto(marca,modelo,precio,color,cilindrada,fecha)
                nuevo_automovil.cargar_moto()
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
        conexion.miCursor.execute("CREATE TABLE Moto (id_moto INTEGER PRIMARY KEY, marca VARCHAR(30), modelo VARCHAR(30), precio INTEGER, color VARCHAR(30), cilindrada VARCHAR(30), fecha DATETIME)")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

clearConsole()

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()
    
    
    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}'".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
    
    def eliminar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}'".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("El automovil se ha eliminado correctamente")
        except:
            print("Ha ocurrido un error al eliminar el automovil")
        finally:
            conexion.cerrarConexion()
    
    @classmethod
    def mostrar_automoviles(cls):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos=conexion.miCursor.fetchall()
            print("\nA continuacion se muestra:\n")
            print("ID - MARCA - MODELO - PRECIO - STOCK")
            for i in autos:
                print(i)
        except:
            print("No hay ningun registro")
        finally:
            conexion.cerrarConexion()

      
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()  
        
class Moto:
    def __init__(self, marca, modelo, precio, color, cilindrada, fecha):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.cilindrada = cilindrada
        self.fecha = fecha
        
    def cargar_moto(self):
            conexion = Conexiones()
            conexion.abrirConexion()
         
            try:
             conexion.miCursor.execute("INSERT INTO Moto(marca,modelo,precio,color,cilindrada,fecha) VALUES('{}', '{}','{}','{}', '{}', '{}')".format(self.marca, self.modelo, self.precio, self.color, self.cilindrada, self.fecha))
             conexion.miConexion.commit()
             print("Moto cargada exitosamente")
            except:
             print("Error al agregar una moto")
            finally:
             conexion.cerrarConexion()
          


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.crearTablas2()
programa.menu()