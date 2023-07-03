from pymongo import MongoClient
from datetime import date
import time



class BaseDatos:
    def __init__(self):
        self.connection_string = "mongodb+srv://Open25:open24712@open25.gikx5hl.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(self.connection_string)
        self.db = self.client.Open25
        self.fecha = str("")
        self.perm = ""
    

    def abrirCaja( self, montoIni):

        cantCajas = 1

        documentos = self.db.caja.find()
        for documento in documentos:
            cantCajas += 1

        codCaja = cantCajas

        document = {"codCaja": codCaja, "fecha": self.fecha, "montoIni": montoIni, "montoFin": 0, "montoPre": 0}

        try:
            collection = self.db.caja
            collection.insert_one(document)
        except:
            print("ocurrio un error")
        
        return codCaja

    def cerrarCaja(self, codCaja, montoFin, montoPre):
        myquery = { "codCaja": codCaja }
        newvalues = { "$set": { "montoFin": montoFin } }
        newvalues2 = { "$set": { "montoPre": montoPre } }

        try:
            collection = self.db.caja
            collection.update_one(myquery, newvalues)
            collection.update_one(myquery, newvalues2)
        except:
            print("An exception occurred 1")

    def venderProducto(self, codBarra):
        
        try:
            collection = self.db.producto
            documento = collection.find()
            for pro in documento:
                if pro["codBarra"] == codBarra:
                    precio = pro["precio"]
                    cant = pro["cant"]
                    nombre =  pro["nom"]
                    if cant > 0:
                        myquery = { "codBarra": codBarra }
                        newvalues = { "$set": { "cant": cant -1 } }
                        collection.update_one(myquery, newvalues)
                    else:
                        return "0" , 0
                    return nombre, precio
            return "1", 0
        except:
            print("el codigo de barras no existe")

    def realizarVenta(self, codCaja, total, arCodigosBarras):
        
        document = {"fecha": self.fecha, "arrayProductos": arCodigosBarras, "codCaja": codCaja, "monto": total }

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


    def actPrecio(self, codBarra, precio, cant):
        myquery = { "codBarra": codBarra }
        newvalues = { "$set": { "precio": precio } }
        newvalues2 = { "$set": { "cant": cant } }
        try:
            collection = self.db.producto
            collection.update_one(myquery, newvalues)
            collection.update_one(myquery, newvalues2)
        except:
            print("An exception occurred 1")


    def informe(self, fechaIni, fechaFin):
        
        arrayCajas = []
        collection = self.db.caja
        documentos = collection.find()

        cajasIni = collection.find({"fecha": fechaIni})
        ini = cajasIni[0]["codCaja"] - 1
        cajasFin = collection.find({"fecha": fechaFin})
        for i in cajasFin:
            fin = i["codCaja"]

        for i in range(ini, fin):
            text = "Caja n° " + str(documentos[i]["codCaja"]) + "\n"
            text += "Fecha: " + documentos[i]["fecha"] + "\n"
            text += "Monto Inicial: " + str(documentos[i]["montoIni"]) + "\n"
            text += "Monto Final: " + str(documentos[i]["montoFin"]) + "\n"
            text += "Monto Final Prediccion: " + str(documentos[i]["montoPre"]) + "\n"
            text += "Productos vendidos: "

            colVentas = self.db.venta
            docs = colVentas.find({"codCaja": i})
            for doc in docs:
                for pro in doc["arrayProductos"]:
                    colPro = self.db.producto
                    producto = colPro.find({"codBarra": pro})
                    nombre = producto[0]["nom"]
                    text += nombre + ", "
                text += "\n"

            arrayCajas.append(text)

        return arrayCajas
        
        
    def login(self, nombre, contra):

        collection = self.db.usuario

        self.fecha = date.today().strftime("%d/%m/%Y")
        print(self.fecha)
        try:
            documentos = collection.find()
            for documento in documentos:
                if documento["name"] == nombre:
                    if documento["password"] == contra:
                        print("logeado correctamente")
                        self.perm = documento["perm"]
                        
        except:
            print("An exception occurred 3")

