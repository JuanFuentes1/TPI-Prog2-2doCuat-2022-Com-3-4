from conexiones import Conexiones

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
            print("\nAutomovil cargado exitosamente\n")
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
            print("\nAutomovil modificado correctamente\n")
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
            print("\nEl automovil se ha eliminado correctamente\n")
        except:
            print("Ha ocurrido un error al eliminar el automovil")
        finally:
            conexion.cerrarConexion()

    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles=cantidadDisponibles+1 WHERE marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("\nAutomovil modificado correctamente\n")
        except:
            print('Error al actualizar un automovil')
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
