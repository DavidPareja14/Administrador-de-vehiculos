import ingresarCorreo
import administradorVentanas
import ventanaAdministradorVehiculos 
import tableroPrincipal 
import ventanaGPS
from kivy.lang import Builder
from kivy.app import App


class VistasApp(App):
	def build(self):
		k=Builder.load_file("vistas.kv")
		return k

if __name__=="__main__":
	VistasApp().run()