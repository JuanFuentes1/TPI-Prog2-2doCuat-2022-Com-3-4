import sqlite3
from turtle import color

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("2- Modificar Automovil")
            print("1- Cargar Automovil")
            print("0- Salir de menu")
            print("3 - Cargar Moto")
            nro = int(input("Por favor ingrese un número"))
            if nro == 1:
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                precio = input("Por favor ingrese el precio del automovil: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
            if nro ==2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar=Automovil(marca,modelo,precio)
                automovil_a_modificar.modificar_automoviles()
                
            if nro ==3: 
             marca = input("Por favor ingrese la marca de la moto: ")
             modelo = input("Por favor ingrese el modelo de la moto: ")
             precio = input("Por favor ingrese el precio de la moto: ")
             cilindrada = input("Por favor ingrese la cilindrada: ")
             color = input("Por favor ingrese el color: ")
             fecha = input("Por favor ingrese la fecha de ultimo ingreso: ")
             nuevo_automovil = Moto(marca,modelo,precio,cilindrada,color,fecha)
             nuevo_automovil.cargar_moto()
                
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30), precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()
    
    def crearTablas(self):
        conexion = Conexiones2()
        conexion.abrirConexion2()
        conexion.miCursor2.execute("DROP TABLE IF EXISTS Moto")
        conexion.miCursor2.execute("CREATE TABLE Moto (id_moto INTEGER PRIMARY KEY , marca VARCHAR(30), modelo VARCHAR(30), cilindrada VARCHAR(30), precio FLOAT NOT NULL , color VARCHAR(30), fecha DATETIME)")    
        conexion.miConexion2.commit()       
        conexion.cerrarConexion2()

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
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
        
    
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()  
        
class Conexiones2:
    
    def abrirConexion2(self):
        self.miConexion2 = sqlite3.connect("Concesionaria")
        self.miCursor2 = self.miConexion2.cursor()
        
    def cerrarConexion2(self):
        self.miConexion2.close()         
        
class Moto:
    def __init__(self, marca, modelo, precio, cilindrada, color, fecha ):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cilindrada = cilindrada
        self.color = color
        self.fecha = fecha
        
        
    def cargar_moto(self):
            conexion = Conexiones2()
            conexion.abrirConexion2()
         
            try:
             conexion.miCursor2.execute("INSERT INTO Moto(marca,modelo,precio,color,cilindrada,fecha) VALUES('{}', '{}','{}','{}', '{}', '{}')".format(self.marca, self.modelo,self.precio,self.color, self.cilindrada, self.fecha))
             conexion.miConexion2.commit()
             print("Moto cargada exitosamente")
            except:
             print("Error al agregar una moto")
            finally:
             conexion.cerrarConexion2()
          


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
