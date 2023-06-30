from http.client import PRECONDITION_FAILED
from mailbox import NoSuchMailboxError
from pymongo import MongoClient
import os
import customtkinter

connection_string = "mongodb+srv://Open25:open24712@open25.gikx5hl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client.Open25
collection = db.usuario



def cargarProducto():
    global db
    codBarra = str(input("ingrese codigo de barra:\n"))
    nom = str(input("ingrese nombre:\n"))
    precio = float(input("ingrese precio:\n"))
    cant = int(input("ingrese cantidad:\n"))
    document = {"codBarra": codBarra, "nom": nom, "precio": precio, "cant": cant}
    collection = db.producto
    collection.insert_one(document)
    

def actPrecio():
    global db
    codBarra = str(input("ingrese nombre:\n"))
    precio = float(input("ingrese nombre:\n"))

    myquery = { "codBarra": codBarra }
    newvalues = { "$set": { "precio": precio } }

    collection = db.producto
    collection.update_one(myquery, newvalues)

def informe():
    global db
    collection = db.venta
    documentos = collection.find()
    for documento in documentos:
       print(documento)

def button_callback():
    print("button clicked")
def slider_event(value): 
    print(value)

def login():
    documentos = collection.find()
    nombre = str(input("ingrese nombre:\n"))
    contra = str(input("ingrese contra:\n"))
    for documento in documentos:
        if documento["name"] == nombre:
            if documento["password"] == contra:
                print("logeado correctamente")
                perm = documento["perm"]
                return perm


def pagPrincipal(perms):
    if perms == "admin":
        cargarProducto()
        actPrecio()
        informe()
    elif perms == "vendedor":
        print("reemplaza esto por favor nicolas no te olvides")



pagPrincipal(login())

app = customtkinter.CTk()
app.geometry("800x500")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
entry = customtkinter.CTkEntry(app, width=120, height=25, corner_radius=10)
entry.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
slider = customtkinter.CTkSlider(app, width=160, height=16, border_width=5.5, command=slider_event)
slider.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
progressbar = customtkinter.CTkProgressBar(app, orientation="horizontal")
button.pack(padx=20, pady=20)

app.mainloop()



# Cadena de conexión de MongoDB Atlas


# Insertar un documento en la colección
#  document = {"name": "John", "password": "jasdjasdasd"}
#  collection.insert_one(document)




os.system("pause")
