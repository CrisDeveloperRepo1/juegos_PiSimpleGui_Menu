import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg   
import json
from datetime import datetime
def iniciarArch():
	
	nombre={}  ### creo un archivo vacio y lo defino como un diccionario vacio , cada vez que ejecute el programa  el archivo se resetea , considere usar un (w) para crear el archivo y usar un (a) para agregar datos  , pero como elegi la notacion json usar el (a) para agregar datos al archivo me deformateaba el archivo ,el archivo solo mostrara los datos de los jugadores por ejecucion del programa.               
	archivo=open("registro.json","w")
	json.dump(nombre,archivo)

	archivo.close()
	
def cargarArch(nom,juego):
	
	dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	archivo=open("registro.json","r")
	nombre=json.load(archivo)
	archivo.close()
##
	archivo=open("registro.json","w")
	nombre[dt_string]={'nombre':nom,'juego':juego}
	json.dump(nombre,archivo)
	archivo.close()


def mostrarRegistro():
	archivo=open("registro.json","r")
	datos = json.load(archivo) 
	if datos == {}:
		print('no hay registros disponibles')
	
	else:
		print('#'*30,' Registro de juegos ','#'*30)
		print(json.dumps(datos, sort_keys=True, indent=4)) 
		archivo.close()

	
	
	
def main(args):
	
	
	iniciarArch()
	sg.ChangeLookAndFeel('Dark Blue')    # Add some color for fun

# 1- the layout

 
 
 
 
          
          

	t=True
	while t:
		
		
		dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		layout =[[sg.Text(dt_string,size=(0, 0),font=("Helvetica", 25))],
		[sg.Image(r'img.png')],

		[sg.Text('ingrese el nombre del jugador :'), sg.Input(key='nombre')],
		[sg.Text('seleccione un juego')],
		[sg.Radio('ahorcado!     ', "RADIO1", default=False), sg.Radio('tateti!', "RADIO1"), sg.Radio('otello!', "RADIO1")],  

		[sg.Button('Jugar'), sg.Button('Salir'),sg.Button('Ver Registro')]] ##

# 2 - the window
		window = sg.Window('Juegos', layout)
		window.Finalize() 
		
		event, values = window.Read()

		if event is None:
	
		
			 break
		if event is 'Jugar':
			 print(values['nombre'])			
			 
	
			 if values[1]:
				 cargarArch(values['nombre'],'ahorcado')
				 
		
				 hangman.main()
				 
			 if values[2]:
				 cargarArch(values['nombre'],'tateti')
				 tictactoeModificado.main()
			
				 
			 if values[3]:
				 cargarArch(values['nombre'],'otello')
				 reversegam.main()				 			 

		if event is 'Guardar':
			 print('guardar')

		if event is 'Salir':
			 print('salir')

			 window.close()
			 t=False
		if event is 'Ver Registro':
			mostrarRegistro()

		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
# elegi un diccinario de diccionarios como estructura para organizar los datos , me parecio mas conveniente por que usando la fecha y hora como clave  puedo tener una mejor organizacion del registro de juegos que se jugaron y de los jugadores
# elegi la notacion json como formato para guardar los datos por la estructura que elegi para organizar los datos , ademas json me permite mostrar los datos  de una manera mas organizada .
