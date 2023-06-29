from pymongo import MongoClient
import os
# Cadena de conexión de MongoDB Atlas
connection_string = "mongodb+srv://Open25:open24712@open25.gikx5hl.mongodb.net/?retryWrites=true&w=majority"

# Crea una instancia del cliente de MongoDB
client = MongoClient(connection_string)

# Selecciona una base de datos
db = client.Open25

# Selecciona una colección
collection = db.usuario

# Insertar un documento en la colección
#  document = {"name": "John", "password": "jasdjasdasd"}
#  collection.insert_one(document)

documentos = collection.find()
nombre = str(input("ingrese nombre:\n"))
contra = str(input("ingrese contra:\n"))
for documento in documentos:
    if documento["name"] == nombre:
        if documento["password"] == contra:
            print("logeado correctamente")
    print(documento)


os.system("pause")