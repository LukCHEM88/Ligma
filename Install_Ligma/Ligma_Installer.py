import tkinter
from tkinter import filedialog
import shutil
root = tk.Tk()
root.withdraw
AppPfad = filedialog.askdirectory
if AppPfad:
    shutil.copy('Ligma.exe','AppPfad')
    shutil.copy('Icon_Ligma.ico', 'C:Program_Files\\Ligma')