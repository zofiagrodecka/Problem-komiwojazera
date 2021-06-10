import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, root, manager):
        super().__init__(root)
        self.root = root
        self.manager = manager
        self.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.info = "długość drogi: "
        self.iterate_button = tk.Button(self, text = "iterate", command = self.iterate)
        self.entry = tk.Entry(self)
        self.display_label = tk.Label(self)
        self.show_result()

        #place objects
        self.entry.grid(row = 0, column = 0)
        self.iterate_button.grid(row = 1, column = 0, pady = 20)
        self.display_label.grid(row = 2, column = 0)

    def iterate(self):
        n = 1
        e = self.entry.get()
        if isinstance(e, int):
            n = e
        for i in range(n):
            self.manager.iterate()
        self.show_result()

    def show_result(self):
        self.manager.show()
        self.display_label.configure(text = str(self.manager.get_length()))