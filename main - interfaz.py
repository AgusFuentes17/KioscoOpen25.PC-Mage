from pymongo import MongoClient
import customtkinter
from datetime import date
import threading

class FuncionPrincipal:
    def __init__(self):
        # Inicializa los atributos de la clase
        self.dato_compartido = None
        self.connection_string = "mongodb+srv://Open25:open24712@open25.gikx5hl.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(self.connection_string)
        self.db = self.client.Open25
        self.fecha = str("")

    def caja(self, montoIni, montoPre, montoFin):
        global fecha

        cantCajas = 1

        documentos = self.db.caja.find()
        for documento in documentos:
            if documento["fecha"] == fecha:
                cantCajas += 1

        codCaja = fecha +"-"+ str(cantCajas)

        document = {"codCaja": codCaja, "fecha": fecha, "montoIni": montoIni, "montoFin": montoFin, "montoPre": montoPre}

        try:
            collection = self.db.caja
            collection.insert_one(document)
        except:
            print("ocurrio un error")

    def venderProducto(self, codBarra):
        
        try:
            collection = self.db.producto
            documento = collection.find()
            for pro in documento:
                if pro["codBarra"] == codBarra:
                    precio = pro["precio"]
                    cant = pro["cant"]
                    myquery = { "codBarra": codBarra }
                    newvalues = { "$set": { "cant": cant -1 } }
                    collection.update_one(myquery, newvalues)
                    return codBarra, precio
        except:
            print("el codigo de barras no existe")

    def realizarVenta(self, codCaja, total, arCodigosBarras):
        global fecha
        
        document = {"fecha": fecha, "arrayProductos": arCodigosBarras, "codCaja": codCaja, "monto": total }

        try:
            collection = self.db.venta
            collection.insert_one(document)
        except:
            print("ocurrio un error")

        return total


    def cargarProducto(self, codBarra, nom, precio, cant):
        
        document = {"codBarra": codBarra, "nom": nom, "precio": precio, "cant": cant}

        try:
            collection = self.db.producto
            collection.insert_one(document)
        except:
            print("ocurrio un error")


    def actPrecio(self, codBarra, precio):
        myquery = { "codBarra": codBarra }
        newvalues = { "$set": { "precio": precio } }

        try:
            collection = self.db.producto
            collection.update_one(myquery, newvalues)
        except:
            print("An exception occurred 1")


    def informe(self, ):
        try:
            collection = self.db.caja
            documentos = collection.find()
            for documento in documentos:
                print(documento)
        except:
            print("An exception occurred 2")
        
    def login(self, nombre, contra):
        global fecha
        global perm

        collection = self.db.usuario

        fecha = date.today().strftime("%d/%m/%Y")
        print(fecha)
        print("porque chota se reproduce esto")
        try:
            documentos = collection.find()
            for documento in documentos:
                if documento["name"] == nombre:
                    if documento["password"] == contra:
                        print("logeado correctamente")
                        perm = documento["perm"]
                        
        except:
            print("An exception occurred 3")

                    
    def ejecutar(self):
    
        self.dato_compartido = "¡Hola desde la función principal!"
    
    
    def otra_funcion(self):
        # Código de otra función dentro de la clase
        pass

class Interfaz:
    def __init__(self, funcion_principal):
        self.funcion_principal = funcion_principal
    
    def ejecutar(self):
        print(self.funcion_principal.dato_compartido)  # Imprime el dato recibido de la función principal
        app = customtkinter.CTk()
        app.geometry("400x150")

        def funcion():
            print("gaysex")
        
        entry = customtkinter.CTkEntry(app, width=120, height=25, corner_radius=10)
        entry2 = customtkinter.CTkEntry(app, width=120, height=25, corner_radius=10)
        button = customtkinter.CTkButton(app, text="my button", command= funcion())
        
        self.funcion_principal.login("Javier","contra")
        entry.pack()
        entry2.pack()
        button.pack()

        app.mainloop()
        self.otra_funcion()
        
    
    def otra_funcion(self):
        # Código de otra función dentro de la clase
       
        pass






funcion_principal = FuncionPrincipal()
interfaz = Interfaz(funcion_principal)


hilo_interfaz = threading.Thread(target=interfaz.ejecutar)
hilo_interfaz.start()

funcion_principal.ejecutar()