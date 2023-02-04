# This is the current GUI in which is in testing phase I

import PySimpleGUI as sg
import tkinter as tk

#font1 = ("Helvetica", 24)
#font2 = ("Bauhaus 93", 14)

#layout = [[sg.Text("Hello from TestGUI", size=(20,1), key='-text-', font=font1)], [sg.Text("(C) 1987 Sun Microsystems Inc", font=font2)], [sg.Button("Launch")]]

#window = sg.Window("PyGUI", layout, size=(290,125))

#while True:
    #event, values = window.read()
    #if event == "Launch" or event == sg.WIN_CLOSED:
        #break

#window.close()

 
# Devlopment Phase I
font1 = ("Helvetica", 24)
font3 = ("Helvetica", 12)
font2 = ("Bauhaus 93", 14)

layout = [[sg.Text("BitVault Password Manager", size=(30,1), key='-text-', font=font1)], 
          [sg.Text("Welcome! Please enter your credentials.", size=(30,1), key='-Welcome-', font=font3)], 
          [sg.Button("Login")], [sg.Text("(C) 2023 Steven Warren", font=font2)]]

window = sg.Window("Password Manager", layout, size=(500,250))

while True:
    event, values = window.read()
    if event == "Login" or event == sg.WIN_CLOSED:
        break

window.close()