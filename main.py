from pymongo import MongoClient
import customtkinter
from datetime import date

connection_string = "mongodb+srv://Open25:open24712@open25.gikx5hl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
try:
    db = client.Open25
except:
  print("An exception occurred 4")
fecha = str("")


def button_callback():
    print("button clicked")
def slider_event(value): 
    print(value)


app = customtkinter.CTk()
app.geometry("800x500")

    
def caja():
    global db
    global fecha

    montoIni = float(input("ingrese monto inicial de la caja\n"))
    opc = 1
    montoPre = 0
    cantCajas = 1

    documentos = db.caja.find()
    for documento in documentos:
        if documento["fecha"] == fecha:
            cantCajas += 1

    codCaja = fecha +"-"+ str(cantCajas)

    while opc != 0:
        opc = int(input("que quiere hacer 1 realizar venta 2 cerrar caja"))
        if opc == 1:
            montoPre += realizarVenta(codCaja)

    montoFin = float(input("ingrese monto final de la caja\n"))
    montoPre += montoIni

    document = {"codCaja": codCaja, "fecha": fecha, "montoIni": montoIni, "montoFin": montoFin, "montoPre": montoPre}

    try:
        collection = db.caja
        collection.insert_one(document)
    except:
        print("ocurrio un error")

    pagPrincipal()

def realizarVenta(codCaja):
    global db
    global fecha
    
    opc = 1
    total = 0
    arCodigosBaras = []
    
    while opc != 0:
        opc = int(input("que quiere hacer 1 anadir producto 2 terminar venta"))
        if opc == 1:
            codBarra = str(input("ingrese el codigo de barra del producto"))
            
            try:
                collection = db.producto
                documento = collection.find()
                for pro in documento:
                    if pro["codBarra"] == codBarra:
                        precio = pro["precio"]
                total += precio
                print("el precio del producto es " + str(precio))
                arCodigosBaras.append(codBarra)
            except:
                print("el codigo de barras no existe")
                
                
            
    document = {"fecha": fecha, "arrayProductos": arCodigosBaras, "codCaja": codCaja, "monto": total }

    try:
        collection = db.venta
        collection.insert_one(document)
    except:
        print("ocurrio un error")

    return total


def cargarProducto():
    global db
    codBarra = str(input("ingrese codigo de barra:\n"))
    nom = str(input("ingrese nombre:\n"))
    precio = float(input("ingrese precio:\n"))
    cant = int(input("ingrese cantidad:\n"))
    document = {"codBarra": codBarra, "nom": nom, "precio": precio, "cant": cant}

    try:
        collection = db.producto
        collection.insert_one(document)
    except:
        print("ocurrio un error")
    
    pagPrincipal()

def actPrecio():
    global db
    codBarra = str(input("ingrese codigo de barra:\n"))
    precio = float(input("ingrese el nuevo precio:\n"))

    myquery = { "codBarra": codBarra }
    newvalues = { "$set": { "precio": precio } }

    try:
        collection = db.producto
        collection.update_one(myquery, newvalues)
    except:
        print("An exception occurred 1")
    
    pagPrincipal()

def informe():
    global db
    try:
        collection = db.caja
        documentos = collection.find()
        for documento in documentos:
            print(documento)
    except:
        print("An exception occurred 2")
    
    pagPrincipal()
    
def login():
    global db
    global fecha
    global perm

    collection = db.usuario

    nombre = str(input("ingrese su nombre"))
    contra = str(input("ingrese su contraseña"))

    fecha = date.today().strftime("%d/%m/%Y")
    print(fecha)
    try:
        documentos = collection.find()
        for documento in documentos:
            if documento["name"] == nombre:
                if documento["password"] == contra:
                    print("logeado correctamente")
                    perm = documento["perm"]   
                    
    except:
        print("An exception occurred 3")

    
def pagPrincipal():
    global perm
    if perm == "admin":
        while True:
            opc = int(input("que quiere hacer 1 cargar producto 2 actualizar precio 3 informe"))
            if opc == 1:
                cargarProducto()
            if opc == 2:
                actPrecio()
            if opc == 3:
                informe()
    elif perm == "vendedor":
        while True:
            opc = int(input("que quiere hacer 1 realizar venta"))
            if opc == 1:
                caja()
                

login()
pagPrincipal()