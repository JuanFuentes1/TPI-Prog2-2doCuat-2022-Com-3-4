from conexiones import Conexiones

class Moto:
    def __init__(self, marca, modelo, precio, color, cilindrada, cantidadDisponibles, fecha):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.cilindrada = cilindrada
        self.cantidadDisponibles = cantidadDisponibles
        self.fecha = fecha
        
    def cargar_moto(self):
            conexion = Conexiones()
            conexion.abrirConexion()
         
            try:
             conexion.miCursor.execute("INSERT INTO Moto(marca,modelo,precio,color,cilindrada,cantidadDisponibles,fecha) VALUES('{}', '{}','{}','{}','{}', '{}', '{}')".format(self.marca, self.modelo, self.precio, self.color, self.cilindrada, self.cantidadDisponibles,self.fecha))
             conexion.miConexion.commit()
             print("\nMoto cargada exitosamente\n")
            except:
             print("Error al agregar una moto")
            finally:
             conexion.cerrarConexion()
    
    def modificar_motos(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE Moto \
                SET precio='{}', fecha='{}' \
                where marca='{}' and modelo='{}' ".format(self.precio,self.fecha,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("\nMoto modificada correctamente\n")
        except:
            print('Error al actualizar la moto')
        finally:
            conexion.cerrarConexion()

    def eliminar_motos(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM Moto where marca='{}' and modelo='{}'".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("\nLa moto se ha eliminado correctamente\n")
        except:
            print("Ha ocurrido un error al eliminar la moto")
        finally:
            conexion.cerrarConexion()

    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE Moto SET cantidadDisponibles=cantidadDisponibles+1 WHERE marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("\nMoto modificada correctamente\n")
        except:
            print('Error al actualizar la moto')
        finally:
            conexion.cerrarConexion()
    
    @classmethod
    def mostrar_motos(cls):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM Moto")
            motos=conexion.miCursor.fetchall()
            print("\nA continuacion se muestra:\n")
            print("ID - MARCA - MODELO - PRECIO - COLOR - CILINDRADA - STOCK - FECHA")
            for i in motos:
                print(i)
        except:
            print("No hay ningun registro")
        finally:
            conexion.cerrarConexion()

    @classmethod
    def mostrar_motos_historico(cls):
            conexion = Conexiones()
            conexion.abrirConexion()
            try:
                conexion.miCursor.execute("SELECT * FROM historico_motocicletas")
                motos=conexion.miCursor.fetchall()
                print("\nRegistro Historico:\n")
                print("ID - MARCA - MODELO - PRECIO - COLOR - CILINDRADA - STOCK - FECHA")
                for i in motos:
                    print(i)
            except:
                print("No hay ningun registro historico")
            finally:
                conexion.cerrarConexion()

    def mostrar_motos_fecha(self):
            conexion = Conexiones()
            conexion.abrirConexion()
            try:
                conexion.miCursor.execute("SELECT * FROM historico_motocicletas WHERE fecha <= '{}' ".format(self.fecha))
                motos=conexion.miCursor.fetchall()
                print("\nRegistro anterior:\n")
                print("ID - MARCA - MODELO - PRECIO - COLOR - CILINDRADA - STOCK - FECHA")
                for i in motos:
                    print(i)
            except:
                print("No hay ningun registro historico")
            finally:
                conexion.cerrarConexion()

    def registrar_historicos(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO historico_motocicletas (marca,modelo,precio,color,cilindrada,cantidadDisponibles,fecha) \
             SELECT marca,modelo,precio,color,cilindrada,cantidadDisponibles,fecha \
             FROM Moto")
            conexion.miConexion.commit()
        except:
            print('Error al registrar historicos')
        finally:
            conexion.cerrarConexion()