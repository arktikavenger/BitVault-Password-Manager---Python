# This is the current GUI in which is in testing phase I

import PySimpleGUI as sg
import tkinter as tk

layout = [[sg.Text("Hello from TestGUI")], [sg.Text("(C) 1987 Sun Microsystems Inc")], [sg.Button("OK")]]

window = sg.Window("TEST", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()