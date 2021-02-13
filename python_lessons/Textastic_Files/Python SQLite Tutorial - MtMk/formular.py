from tkinter import *


def root():
    return Tk()


def form_body(root, name, geometry):
    with root:
    Tk.title(name)
    Tk.geometry(geometry)
