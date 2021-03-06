from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder
from anadirVehiculo import AgregarVehiculo
import requests
""" 
Los botones de vehiculo, Ubicacion y Eliminar los implemento como clases aparte, esto con el objeto de poder obtener la instancia de cada
btn al presionar uno, ya que desde el kv solo es mandar como parametro a la funcion (self) si el btn es presionado, hay otras formas, 
pero no quiero, con esto puedo obtener el id correspondiente al vehiculo.
"""
#l=[]
k=Builder.load_string("""
<SecondWindow>:
    name: "segunda"
    BoxLayout:
        id:box
        orientation:"vertical"
        BoxLayout:
            size_hint_y:0.3
            orientation:"vertical"
            Label: 
                text: "Administrador de vehiculos"
            BoxLayout:
                Label: 
                    text: "Vehiculo"
                Label: 
                    text: "Ubicacion"
                Label: 
                    text: "Eliminar"
        ScrollView:
            id: scroll
            GridLayout:
                id: contenedorFilas
                cols: 1
                size_hint_y: None #Si esto no se pone, el scroll no aparece.
                row_default_height: root.height*0.1
                height: self.minimum_height
        BoxLayout:
            size_hint_y:0.25
            spacing: 50 
            padding: 20,30,50,10 #Margenes: izquierda, arriba, derecha, abajo
            Button: 
                text: "Agregar Vehiculo"
                on_release:
                	root.oprimidoBtnAgregarVehiculo()
            Button: 
                text: "GPS"
                on_release:
                	root.pantallas(app)
                	root.manager.current="gps"

<BotonVehiculo>:
    on_press: app.root.current="tableroPrincipal"
<BotonUbicacion>:
    on_press: root.ubicacionVehiculo()
<BotonEliminar>:
    on_press: root.eliminarVehiculo()
""")
class BotonVehiculo(Button):
	def tableroVehiculo(self):
		pass

class BotonUbicacion(Button):
	def ubicacionVehiculo(self):
		ip_request = requests.get('https://get.geojs.io/v1/ip.json')
		my_ip = ip_request.json()['ip']
		geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
		geo_data = geo_request.json()

		#Agregar ubicacion DB
		print(self.parent.children[2].text) #Para obtener el nombre del vehiculo.
		print(geo_data['latitude'], geo_data['longitude'])

		self.popup = Popup(title="ESTADO",
							content=Label(text="Ubicacion guardada correctamente"),
							size_hint=(0.7, 0.2))
		self.popup.open()
	
class BotonEliminar(Button):
	"""ATENCION
		Para la f eliminarVeh no me permite eliminar botones con el parent cosa que es extraña, porque con solo poner self.parent me muestra el pad
		re del btn, supuse que tal vez me interpretaba el btn como un objeto diferente, como sea, lo que hice fue crear una lista l con todos 
		los objetos boxlayout creados, luego comparo ese con el boxlayout padre de mi btn seleccionado y borro los botones (veh, ubic, elim)
		pero desde el obj metido en la lista y funciona. Luego meti el gridLayout que contiene a todos los boxlayout en la ultima pos de la lis
		ta para poder accederlo y elimimar el boxlayout que contiene al boton oprimido, lo elimina, pero en la terminal de cmd salen errores
		al yo cerrar la ventana de kivy.

		LO HE SOLUCIONADO
		Utilizando la lista l para meter los objetos BoxLayout y Grid ([objBox,objBox,objBox,..., objGridLayout]) podia eliminar los 
		objetos BoxLayout si se seleccionaba el boton respectivo, sin embargo al cerrar la aplicacion, se generaban errores, lo que pienso,
		que yo eliminaba un box pero como era una copia quedaba el otro, esto puede generar incosistencias, al hacer la prueba unitaria con este
		modulo, me di cuenta que mi implementacion funcionaba con normalidad, sin necesidad de una lista, solo con self.parent... ahora, he quitado
		el codigo kv del archivo vistas.kv y lo integro en este archivo y funciona.
	"""
	def eliminarVehiculo(self):
		print (self.parent.children[2].text) #saca el nombre del vehiculo a eliminar de BD
		self.parent.parent.remove_widget(self.parent)
		#print(self.parent.remove_widget(self)) #Es para que elimine los botones con respecto al eliminar, pero genera error, si se prueba como un modulo
								 #individual esta bien.
		"""
		for obj in l:
			if self.parent==obj:
				l[-1].remove_widget(obj)
		"""
class SecondWindow(Screen):
	#l=[]
	def __init__(self, **kwargs):
		super(SecondWindow, self).__init__(**kwargs)
		Clock.schedule_once(lambda dt:self.scrollVehiculos()) #hago este proceso, porque si trato de usar los self.ids desde el constructor,
											   #Me dara error, ya que no se han creado todavia, por eso con clock lo que trato es
											   #retardar el proceso, de esta manera funciona, con la func lambda no tengo que obtener dt.

	def oprimidoBtnAgregarVehiculo(self):
		self.content = AgregarVehiculo() #Este texto que paso lo captura el stringProperty
		self.content.bind(on_guardar=self._on_guardar) #segun mi analisis, es para dar el mando de on_answer a _on_answer
		self.popup = Popup(title="Agregue el vehiculo que desee",
							content=self.content,
							size_hint=(0.9, 0.9))
		self.popup.open()

	def pantallas(self, app):
			app.root.screens[3].actualizarMarcadores() #Es para que el mapa siempre aparesca centrado en la ubicacion actual

	def _on_guardar(self, instance):
		resultadoVentanaAgregarVehiculo=self.content.on_guardar() #La pos 0 me determina si los datos de agregarVeh son correctos o no.
		if resultadoVentanaAgregarVehiculo[0]: #pos que contiene True o False
			box=BoxLayout(orientation="horizontal")
			box.add_widget(BotonVehiculo(text=resultadoVentanaAgregarVehiculo[1])) #pos que tiene nombre del vehiculo.
			box.add_widget(BotonUbicacion(text="ubicacion")) #Los ids son iguales y corresponden al nombre del vehiculo
			box.add_widget(BotonEliminar(text="Eliminar"))
			self.ids.contenedorFilas.add_widget(box)
			self.popup.dismiss()
		else:
			pass

	def scrollVehiculos(self): 
		# CONSULTA BASE DE DATOS PARA LISTAR TODOS LOS VEHICULOS

		for i in range(5): 
			#self.l.append(BoxLayout(orientation="horizontal"))
			#self.ids.contenedorFilas.add_widget(self.l[-1]) #al gridlayout le agrego lo boxlayout necesarios, en cada boxlayout puedo posicionar
															 #mis tres botones.
			self.ids.contenedorFilas.add_widget(BoxLayout(orientation="horizontal"))
		for i, n in enumerate(self.ids.contenedorFilas.children):									   
			n.add_widget(BotonVehiculo(text="vehiculo"+str(i)))
			n.add_widget(BotonUbicacion(text="ubicacion"+str(i))) #Los ids son iguales y corresponden al nombre del vehiculo
			n.add_widget(BotonEliminar(text="Eliminar"+str(i)))


			#l.append(n)
		#l.append(self.ids.contenedorFilas)
		#print(l) #No entiendo porque se imprimen dos listas

	"""
	#Esta funcion la dejo por si algo, no funciono para eliminar los botones, pero fue un intento que depronto me sirva en el futuro.
	def eliminarVehiculo(self, idBoton): #esto es para eliminar los botones asociados a un boxL pero sale raro, creo que es porque meto los 
										 #boxLayout a una lista, o porque el parametr idBoton me lo pasan desde otra clase.
		#print(idBoton)
		#self.l[int(idBoton)].clear_widgets()
		#self.ids.contenedorFilas.remove_widget(self.l[int(idBoton)])
		#self.l.pop(int(idBoton))
	"""