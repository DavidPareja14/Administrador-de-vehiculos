# ADMINISTRADOR DE VEHÍCULOS :blue_car: :tractor: :bus: :motorcycle:
Con el fin de desarrollar el proyecto del curso Laboratorio de Software impartido en la Universidad Tecnológica de Pereira, se procede a realizar el administrador de vehículos, el cual, es un aplicativo móvil que le permite a un usuario realizar varias operaciones como:

* Registrar varios vehículos. Al registrar un vehículo, también se permitirá eliminarlo o guardar la ubicación actual en donde se encuentra por medio de GPS.
* Al seleccionar un vehículo, se pueden realizar:
    * Recargas, en donde se debe ingrasar el precio pagado por combustible y los kilómetros que el vehículo ha recorrido. La fecha de la recarga se grabará automáticamente. 
    * Se permite llevar un registro de los mantenimientos que el vehículo haya necesitado.
    * Los reportes se generan de a cuerdo a las recargas, los mantenimientos y la huella de carbono (este último no fue completado), además, se puede ingresar la fecha de inicio y fin para tomar en ese intervalo la información deseada. Luego, se debe ingresar un correo electrónico al cual se enviará el reporte.
    * Finalmente, las alarmas que un usuario necesite, las puede realizar de acuerdo a si es una alarma para las recargas o para mantenimientos, además, existe la posibilidad de que la alarma sea fija o periódica, si es fija, solo se activará en una fecha específica, si es periódica, se deben ingresar la cantidad de días en los cuales se debe activar.
* Cuando se desee, los lugares cercanos a los que se encuentre un usuario pueden ser visualizados en un mapa que geográficamente cubre todo el mundo, para estar con la posición actualizada, se debe seleccionar el botón actualizar vehículos.

## Preparando el entorno de desarrollo
La versión de python es >3.5. 
Es una buena práctica crear un entorno virtual para python. Siguiendo la documentación para [Instalar Kivy](https://kivy.org/doc/stable/gettingstarted/installation.html#kivy-source-install) se ejecuta primero:
>python -m pip install --upgrade pip setuptools virtualenv

Luego se crea un entorno virtual con el nombre Kivy_venv (Puede ser el nombre que desee):
>python -m virtualenv kivy_venv (Esto es para Windows)

Luego, se procede con la activación del entorno virtual:
>kivy_venv\Scripts\activate

Por último, se realiza la instalación de Kivy:
>python -m pip install kivy[base]

Con lo anterior kivy quedará instalado, para el proyecto también se necesita importar pandas, por eso debe estar instalado:
>pip install pandas
## Ejecución
El archivo principal es main.py
>python main.py

## Atención
Este proyecto fue realizado en equipo, Diana Batero y Felipe Marin contribuyeron significativamente. Todo lo que está en este repositorio yo lo he realizado, pero esto es solo la parte visual, se pueden agregar datos, pero es solo como una prueba. Para tener el proyecto completo, recomiendo visitar a [Jofemago](https://github.com/Jofemago/Administrador_Vehiculos). Felipe se ha encargado de realizar la conexión con la base de datos y también, que el aplicativo pueda ser funcional en un teléfono móvil.

En el archivo ventanaGPS.py se deben poner las credenciales para utilizar Foursquare, el cual me ha brindado acceso a su servicio con el fin de mostrar los lugares cercanos en donde me encuentro, los lugares pueden ser restaurantes, parqueaderos, hoteles, etc. Las credenciales se ubican en la línea 136 y 137.