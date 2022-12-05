# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:56:26 2022

@author: JHOSSBACH
"""
import tkinter as tk


# Ein Fenster erstellen
root = tk.Tk()
# Den Fenstertitle erstellen
root.title("Nur ein Fenster")


text_variable = tk.IntVar()
text_variable.set(6000)


#Konstruktor für den ersten Container, in diesem können weiter Container/Fenster angezeigt werden
Fenster=tk.Label(root,textvariable=text_variable,
                  foreground="white",  # Set the text color to white
                  background="black",
                  width= 90,
                  height= 30)  # Set the background color to black



Fenster.pack()

print(text_variable.get())


#Ein Test hier
#------------------------------------------------------------------------------

Button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",)


Button.pack()

'''
fill="x" Button über die gesamte X-Achse
fill="y" Button über die gesamte Y-Achse
padding=10 Abstand des Buttons von oberer Kante
'''


'''
#------------------------------------------------------------------------------

entry = tk.Entry(root, fg="yellow", bg="blue", width=50)

entry.pack()

#------------------------------------------------------------------------------


# In der Ereignisschleife auf Eingabe des Benutzers warten.

'''

root.mainloop()