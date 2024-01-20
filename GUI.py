import tkinter as tk
from tkinter import ttk,filedialog

def Verschlüsseln():
    print('Verschlüsselt')
    Hauptfenster.iconify()
    global Verschlüsselnfester
    Verschlüsselnfester = tk.Tk()
    tk.Button(Verschlüsselnfester,command=Fenster).pack()
    Verschlüsselnfester.mainloop()
def Fenster():
    global Hauptfenster
    Hauptfenster = tk.Tk()
    Hauptfenster.geometry('400x300')
    Hauptfenster.resizable('False','False')
    Hauptfenster.title('Ligma')
    tk.Label(Hauptfenster,text='Willkommen').place(x='50',y='50')
    tk.Button(Hauptfenster,text='Verschlüsseln',command=Verschlüsseln).place(x='230',y='150')
    tk.Button(Hauptfenster,text='Entschlüsseln',command=Entschlüsseln).place(x='50',y='150')

def Entschlüsseln():
    print('Entschlüsselt')
def open():
    print(filedialog.askopenfilename())






Hauptfenster.mainloop()