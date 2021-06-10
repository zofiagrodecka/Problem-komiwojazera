import tkinter as tk
from PIL import Image,ImageTk

stats_dict = {0:'before_operations',
              1:'selected_to_interbreeding',
              2:'after_interbreeding',
              3:'selected_to_mutation',
              4:'after_mutation',
              5:'after_sort',
              6:'after_deletion'}

headers = {'before_operations':'Stan przed operacjami',
            'selected_to_interbreeding':'Wybrane do krzyżówek',
            'after_interbreeding':'Stan po operacjach',
            'selected_to_mutation':'Wybrane do mutacji',
            'after_mutation':'Stan po mutacji',
            'after_sort':'Stan po sortowaniu',
            'after_deletion':'Stan końcowy'}

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
        self.actions_frame = tk.Frame(self)
        self.actions_label = tk.Label(self.actions_frame, text = "Kroki algorytmu")
        self.left_page = tk.Button(self.actions_frame, text = "Poprzedni", command = self.previous_page)
        self.right_page = tk.Button(self.actions_frame, text = "Następny", command = self.next_page)
        self.output_frame = tk.Frame(self.actions_frame)
        self.actions = tk.Text(self.output_frame, width=50)
        self.scrollbar = tk.Scrollbar(self.output_frame, command = self.actions.yview)
        self.actions['yscrollcommand'] = self.scrollbar.set
        self.output_frame.rowconfigure(0, weight = 1)
        self.actions_frame.rowconfigure(1, weight = 1)
        self.left_page.grid(row = 0, column = 0)
        self.actions_label.grid(row = 0, column = 1)
        self.right_page.grid(row = 0, column = 2)
        self.output_frame.grid(row = 1, column = 0, columnspan = 3, pady = (20, 0), sticky = 'nswe')
        self.actions.grid(row = 0, column = 0, sticky = 'nswe')
        self.scrollbar.grid(row = 0, column = 1, sticky = 'nswe')
        self.scrollbar.grid()
        self.current_page = 0

        #place objects
        self.entry.grid(row = 0, column = 0)
        self.iterate_button.grid(row = 1, column = 0, pady = 20)
        self.display_label.grid(row = 2, column = 0)
        self.graph_label.grid(row = 3, column = 0, pady = (20,0))
        self.actions_frame.grid(row = 0, column = 1, rowspan = 4, padx = (20,0), sticky = 'nswe')

        self.statistics = None
        self.show_result()

    def get_n_pages(self):
        return len(self.statistics)

    def load_text(self):
        self.clear_text()
        self.actions.insert('end', headers[stats_dict.get(self.current_page)]+'\n\n')
        for information in self.statistics[stats_dict.get(self.current_page)]:
            self.actions.insert('end', information+'\n')

    def clear_text(self):
        self.actions.delete('1.0', 'end')

    def previous_page(self):
        prev_page = self.current_page - 1
        while prev_page >= 0 and stats_dict[prev_page] not in self.statistics.keys():
            prev_page -= 1
        if prev_page >= 0:
            self.current_page = prev_page
            self.load_text()

    def next_page(self):
        next_page = self.current_page + 1
        while next_page < self.get_n_pages() and stats_dict[next_page] not in self.statistics.keys():
            next_page += 1
        if next_page < self.get_n_pages():
            self.current_page = next_page
            self.load_text()

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
        self.current_page = 0
        self.show_result()

    def show_result(self):
        path = self.manager.get_graph_path()
        graph_image = Image.open(path)
        display = ImageTk.PhotoImage(graph_image)
        self.graph_label.configure(image = display)
        self.graph_image = display
        self.display_label.configure(text = self.info + str(self.manager.get_length()))
        self.statistics = self.manager.get_statistics()
        self.load_text()