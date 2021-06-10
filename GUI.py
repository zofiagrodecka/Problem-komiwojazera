import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, root, manager):
        super().__init__(root)
        self.root = root
        self.manager = manager
        self.grid(row = 0, column = 0, padx = 20, pady = 20)

    def iterate(self, n = 1):
        for i in range(n):
            self.manager.iterate()

    def show_result(self):
        self.manager.show()