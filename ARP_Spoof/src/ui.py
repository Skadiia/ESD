#!/usr/bin/env python
#__*__coding:utf:8__*__

RED, GREEN, YELLOW, END = '\033[31m', '\033[32m', '\033[33m', '\033[0m'

from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()