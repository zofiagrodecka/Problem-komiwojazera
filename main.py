from GeneticsManager import GeneticsManager
from Graph import Graph
import tkinter as tk
from GUI import GUI

g = GeneticsManager()
root = tk.Tk()
gui = GUI(root, g)
root.mainloop()
