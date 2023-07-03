import os
import time
import customtkinter
from mainInterfaz import BaseDatos

bd = BaseDatos()

def borrarPantalla():
	etiqueta1.pack_forget()
	etiqueta2.pack_forget()
	cajaTexto1.pack_forget()
	cajaTexto2.pack_forget()
	boton1.pack_forget()
	cargarProducto.pack_forget()
	actualizarPrecio.pack_forget()
	verInforme.pack_forget()
	abrirCaja.pack_forget()
	etiquetaCod.pack_forget()
	etiquetaNom.pack_forget()
	etiquetaPre.pack_forget()
	etiquetaCant.pack_forget()
	entryCod.pack_forget()
	entryNom.pack_forget()
	entryPre.pack_forget()
	entryCant.pack_forget()
	etiquetaFI.pack_forget()
	entryFIni.pack_forget()
	etiquetaFF.pack_forget()
	entryFFin.pack_forget()
	for widgets in scroll.winfo_children():
		widgets.pack_forget()
	for widgets in scroll1.winfo_children():
		widgets.pack_forget()
	
	
def mostrarMensaje(malo, msg):
	if malo:
		mensaje = customtkinter.CTkLabel(app, text = msg,text_color='red')
	else:
		mensaje = customtkinter.CTkLabel(app, text = msg,text_color='green')
	mensaje.pack(pady= (10,0))
	app.update()
	time.sleep(2)
	mensaje.pack_forget()


def ingresar():
	uno = cajaTexto1.get()
	dos = cajaTexto2.get()
	bd.login(uno, dos)
	time.sleep(0.5)
	main()
		
def main():
	if bd.perm == "admin":
		borrarPantalla()
		cargarProducto.pack(pady=(20, 0))
		actualizarPrecio.pack(pady=(20, 0))
		verInforme.pack(pady=(20, 0))
	elif bd.perm == "vendedor":
		borrarPantalla()
		abrirCaja.pack()
	elif bd.perm != "admin" or  bd.perm != "vendedor":
		mostrarMensaje(True,"Usuario o contraseña incorrectos")

def cargarPro():
	borrarPantalla()
	def cagarBD():
		cod = entryCod.get()
		nom = entryNom.get()
		pre = entryPre.get()
		cant = entryCant.get()
		if cod == "" or nom == "" or pre == "" or cant == "":
			mostrarMensaje(True, "Rellene todos los casilleros")
		else:
			bd.cargarProducto(cod,nom,pre,int(cant))
			botonAgPro.pack_forget()
			botonCancelar.pack_forget()
			main()
	
	def cancelar():
		botonAgPro.pack_forget()
		botonCancelar.pack_forget()
		main()

	entryCod.delete(0,customtkinter.END)
	entryNom.delete(0,customtkinter.END)
	entryPre.delete(0,customtkinter.END)
	entryCant.delete(0,customtkinter.END)
	etiquetaCod.pack()
	entryCod.pack()
	etiquetaNom.pack()
	entryNom.pack()
	etiquetaPre.pack()
	entryPre.pack()
	etiquetaCant.pack()
	entryCant.pack()
	botonAgPro = customtkinter.CTkButton(app, text="Cargar Producto", command = cagarBD)
	botonAgPro.pack(pady= (40,0))
	botonCancelar = customtkinter.CTkButton(app, text="Cancelar", command = cancelar)
	botonCancelar.pack(pady= (10,0))
	

def actPrecio():
	def cagarBD():
		cod = entryCod.get()
		pre = entryPre.get()
		cant = entryCant.get()
		if cod == "" or pre == "" or cant == "":
			mostrarMensaje(True, "Rellene todos los casilleros")
		else:
			bd.actPrecio(cod,pre, cant)
			botonAgPro.pack_forget()
			botonCancelar.pack_forget()
			main()

	def cancelar():
		botonAgPro.pack_forget()
		botonCancelar.pack_forget()
		main()

	borrarPantalla()
	etiquetaCod.pack()
	entryCod.delete(0,customtkinter.END)
	entryCod.pack()
	etiquetaPre.pack()
	entryPre.delete(0,customtkinter.END)
	entryPre.pack()
	etiquetaCant.pack()
	entryCant.delete(0,customtkinter.END)
	entryCant.pack()
	botonAgPro = customtkinter.CTkButton(app, text="Actualizar Producto", command = cagarBD)
	botonAgPro.pack(pady= (40,0))
	botonCancelar = customtkinter.CTkButton(app, text="Cancelar", command = cancelar)
	botonCancelar.pack(pady= (10,0))
	
def verInfo():
	borrarPantalla()
	def cancelar():
		botonCancelar.pack_forget()
		botonBuscar.pack_forget()
		scroll1.pack_forget()
		main()
	def buscar():
		fi = entryFIni.get()
		ff = entryFFin.get()
		if fi == "" or ff == "":
			mostrarMensaje(True, "Rellene todos los casilleros")
		else:
			arr = bd.informe(fi, ff)
			for a in arr:
				txt = customtkinter.CTkLabel(scroll1, text = a)
				txt.pack(pady= (20,0))
			
		

	etiquetaFI.pack()
	entryFIni.pack()
	etiquetaFF.pack()
	entryFFin.pack()
	botonBuscar= customtkinter.CTkButton(app, text="Buscar Cajas", command = buscar)
	botonBuscar.pack(pady= (10,10))
	
	
	scroll1.pack()

	botonCancelar = customtkinter.CTkButton(app, text="Salir", command = cancelar)
	botonCancelar.pack(pady= (10,0))

def caja():
	def dentroCaja():
		etiquetaMI.pack_forget()
		entryMI.pack_forget()
		botonMI.pack_forget()
		scroll.pack_forget()
		etiquetaCod.pack_forget()
		entryCod.pack_forget()
		botonIngresar.pack_forget()

		botonV.pack()
		botonCC.pack()
		

	def venta():
		borrarPantalla()
		global total
		total = 0
		botonV.pack_forget()
		botonCC.pack_forget()

		etiquetaCod.pack()
		entryCod.pack()
		
		
		botonIngresar.pack()

		scroll.pack(pady=(20, 20))
		etiquetaTiV.pack()
		entryVuelto.pack()
		botonVuelto.pack()
		etiquetaV.pack()
		botonTerminarVenta.pack(pady=(10, 0))



		

	def terminarVenta():
		etiquetaTiV.pack_forget()
		entryVuelto.pack_forget()
		botonVuelto.pack_forget()
		etiquetaV.pack_forget()
		global total
		global arrCodBarras
		global codCaja
		global montoPre
		montoPre += total
		botonTerminarVenta.pack_forget()
		bd.realizarVenta(codCaja,total,arrCodBarras)
		dentroCaja()

	def pedirMontoFin():
		botonV.pack_forget()
		botonCC.pack_forget()
		global montoFin
		etiquetaMF.pack()
		entryMF.pack()
		botonFin.pack()

	def cerrarCaja():
		global montoPre
		global codCaja
		global montoFin
		global montoIni
		etiquetaMF.pack_forget()
		entryMF.pack_forget()
		botonFin.pack_forget()
		montoFin = entryMF.get()
		montoPre += montoIni
		bd.cerrarCaja(codCaja,int(montoFin),montoPre)
		main()

	def calcularVuelto():
		
		global total
		vuelto = int(entryVuelto.get()) - total
		etiquetaV.configure(text = "Vuelto :" + str(vuelto))
		entryVuelto.delete(0,customtkinter.END)
		app.update()
	
	def abrirCaja():
		global codCaja
		global montoIni
		montoIni = int(entryMI.get())
		codCaja = bd.abrirCaja(montoIni)
		dentroCaja()


	def venderProducto():
		
		global total
		global arrCodBarras
		codPro = entryCod.get()
		entryCod.delete(0,customtkinter.END)
		
		if codPro == "":
			mostrarMensaje(True, "Ingrese el codigo de barras")
		else:
			nombre,precio = bd.venderProducto(codPro)
			if precio != 0:
				total += int(precio)
				
				txt = customtkinter.CTkLabel(scroll, text = nombre +": "+ precio + "$")
				txt.pack()
				arrCodBarras.append(codPro)
			else:
				if nombre == "0":
					mostrarMensaje(True, "No queda stock")
				if nombre == "1":
					mostrarMensaje(True, "No existe codigo de barra")

	
	borrarPantalla()
	
	etiquetaMI = customtkinter.CTkLabel(app, text = "Ingresar monto inicial")
	botonIngresar = customtkinter.CTkButton(app, text="ingresar", command = venderProducto)
	entryMI = customtkinter.CTkEntry(app)
	botonTerminarVenta = customtkinter.CTkButton(app, text="Terminar venta", command = terminarVenta)
	botonMI = customtkinter.CTkButton(app, text="Aceptar", command = abrirCaja)
	botonV = customtkinter.CTkButton(app, text="Realizar Venta", command = venta)
	botonCC = customtkinter.CTkButton(app, text="Cerrar Caja", command = pedirMontoFin)
	
	etiquetaTiV = customtkinter.CTkLabel(app, text = "Ingresar monto pagado")
	entryVuelto = customtkinter.CTkEntry(app)
	botonVuelto = customtkinter.CTkButton(app, text="Calcular vuelto", command = calcularVuelto)
	etiquetaV = customtkinter.CTkLabel(app, text = "Vuelto:")

	etiquetaMF = customtkinter.CTkLabel(app, text = "Ingresar monto final")
	botonFin = customtkinter.CTkButton(app, text="ingresar", command = cerrarCaja)
	entryMF = customtkinter.CTkEntry(app)
	etiquetaMI.pack()
	entryMI.pack()
	botonMI.pack()

app = customtkinter.CTk()
app.geometry("700x600")
scroll = customtkinter.CTkScrollableFrame(app, width=500, height=150)
scroll1 = customtkinter.CTkScrollableFrame(app, width=500, height=150)
total = 0
codCaja = 0
arrCodBarras = []
montoPre = 0
montoFin = 0
montoIni = 0

marca = customtkinter.CTkLabel(app, text = "Open 25")
etiqueta1 = customtkinter.CTkLabel(app, text = "Usuario")
etiqueta2 = customtkinter.CTkLabel(app, text = "Contraseña")
cajaTexto1 = customtkinter.CTkEntry(app)
cajaTexto2 = customtkinter.CTkEntry(app)
boton1 = customtkinter.CTkButton(app, text="Iniciar sesion", command = ingresar)

cargarProducto = customtkinter.CTkButton(app, text="Cargar Producto", command = cargarPro)
actualizarPrecio = customtkinter.CTkButton(app, text="Actualizar Producto", command = actPrecio)
verInforme = customtkinter.CTkButton(app, text="Ver Informe", command = verInfo)

abrirCaja = customtkinter.CTkButton(app, text="Abrir caja", command = caja)

etiquetaCod = customtkinter.CTkLabel(app, text = "Codigo de Barras")
etiquetaNom = customtkinter.CTkLabel(app, text = "Nombre")
etiquetaPre = customtkinter.CTkLabel(app, text = "Precio")
etiquetaCant = customtkinter.CTkLabel(app, text = "Cantidad")
entryCod= customtkinter.CTkEntry(app)
entryNom = customtkinter.CTkEntry(app)
entryPre = customtkinter.CTkEntry(app)
entryCant= customtkinter.CTkEntry(app)

etiquetaFI = customtkinter.CTkLabel(app, text = "Fecha de inicio")
etiquetaFF = customtkinter.CTkLabel(app, text = "Fecha de fin")
entryFIni= customtkinter.CTkEntry(app, placeholder_text="dd/mm/aaaa")
entryFFin = customtkinter.CTkEntry(app, placeholder_text="dd/mm/aaaa")



	
marca.pack(pady=(40, 20))
etiqueta1.pack()
cajaTexto1.pack()
etiqueta2.pack()
cajaTexto2.pack()
boton1.pack(pady= (40,0))
app.mainloop()
