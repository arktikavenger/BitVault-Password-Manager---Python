# This is the current GUI in which is in testing phase I

import PySimpleGUI as sg
import tkinter as tk

font1 = ("Helvetica", 24)
font2 = ("Bauhaus 93", 14)

layout = [[sg.Text("Hello from TestGUI", size=(20,1), key='-text-', font=font1)], [sg.Text("(C) 1987 Sun Microsystems Inc", font=font2)], [sg.Button("OK")]]

window = sg.Window("TEST", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()