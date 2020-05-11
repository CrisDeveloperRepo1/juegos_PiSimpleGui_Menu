import PySimpleGUI as sg   
import json
"""
  DESIGN PATTERN 2 - Multi-read window. Reads and updates fields in a window
"""

sg.ChangeLookAndFeel('Dark Blue')    # Add some color for fun

# 1- the layout
layout =[[sg.Text('Menu', size=(0, 0), font=("Helvetica", 25))],
[sg.Image(r'C:\Users\Criatian\Desktop\Python\Practica 4/img.png')],

[sg.Text('ingrese el nombre del jugador :'), sg.Input(key='nombre')],
[sg.Text('seleccione un juego')],
[sg.Radio('ahorcado!     ', "RADIO1", default=False), sg.Radio('tateti!', "RADIO1"), sg.Radio('otello!', "RADIO1")],  
#[sg.Listbox(values =[], key='datos', size=(60,10))], ### consultar el uso de values
[sg.Button('Jugar'), sg.Button('Salir')]] ##

# 2 - the window
window = sg.Window('Juegos', layout)
window.Finalize() 
event, values = window.Read()          
# layout = [[sg.Image(r'C:\Users\Criatian\Desktop\Python\Practica 4/img.png')],

# [sg.Listbox(values =[], key='datos', size=(60,10))], ### consultar el uso de values
# [sg.Button('Añadir'), sg.Button('Guardar')]]          
          
          
          
# window = sg.Window('JUEGOS', default_element_size=(10, 0)).Layout(layout)

# # # 3 - the event loop

# event, values = window.read()
print(values)
