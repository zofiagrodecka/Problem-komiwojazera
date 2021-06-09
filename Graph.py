import networkx as nx
import matplotlib.pyplot as plt
from random import randrange


class Graph:
    def __init__(self):
        self.n_nodes = 5  # wielkosc populacji
        self.graph = nx.Graph()
        self.edges = []
        self.set_graph()
        self.pos = nx.spring_layout(self.graph, 10)

    def set_graph(self):
        for i in range(self.n_nodes):
            for j in range(self.n_nodes):
                if i != j:
                    self.graph.add_edge(i+1, j+1, weight=randrange(1, 10))
        self.edges = [(u, v) for (u, v, d) in self.graph.edges(data=True)]

    def show_graph(self):
        nx.draw(self.graph, self.pos, with_labels=True)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=labels)
        print(nx.info(self.graph))
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.show()


