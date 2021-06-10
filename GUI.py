import tkinter as tk
from PIL import Image,ImageTk

class GUI(tk.Frame):
    def __init__(self, root, manager):
        super().__init__(root)
        self.root = root
        self.manager = manager
        self.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.info = "długość drogi: "
        self.iterate_button = tk.Button(self, text = "iterate", command = self.iterate)
        self.entry = tk.Entry(self)
        self.graph_label = tk.Label(self)
        self.graph_image = None
        self.display_label = tk.Label(self)

        #place objects
        self.entry.grid(row = 0, column = 0)
        self.iterate_button.grid(row = 1, column = 0, pady = 20)
        self.display_label.grid(row = 2, column = 0)
        self.graph_label.grid(row = 3, column = 0)

        self.show_result()

    def iterate(self):
        n = 1
        try:
            e = self.entry.get()
            if len(e) > 0:
                e = int(e)
                if e > 0:
                    n = e
        except ValueError:
            print("Number of iterations must be integer!")
        for i in range(n):
            self.manager.iterate()
        self.show_result()

    def show_result(self):
        path = self.manager.get_graph_path()
        graph_image = Image.open(path)
        display = ImageTk.PhotoImage(graph_image)
        self.graph_label.configure(image = display)
        self.graph_image = display
        self.display_label.configure(text = self.info + str(self.manager.get_length()))