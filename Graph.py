import networkx as nx
import matplotlib.pyplot as plt
from random import randrange


class Graph:
    def __init__(self):
        self.n_nodes = 10  # wielkosc populacji
        self.graph = nx.Graph()
        self.edges = []
        self.nodes = []
        self.set_graph()
        self.pos = nx.spring_layout(self.graph, 10)

    def set_graph(self):
        for i in range(self.n_nodes):
            for j in range(self.n_nodes):
                if i != j:
                    self.graph.add_edge(i+1, j+1, weight=randrange(1, 20))
            self.nodes.append(i+1)
        print(self.nodes)

    def edges_from_list(self, path):
        edges = []
        for i in range(len(path)-1):
            edges.append((path[i], path[i+1], ))
        edges.append((path[len(path)-1], 1, ))
        return edges

    def show_graph(self, res):
        edges = self.edges_from_list(res)
        nx.draw(self.graph, self.pos, with_labels=True)
        # nx.draw_networkx_nodes(self.graph, self.pos, nodelist=self.nodes, node_color="b")
        nx.draw_networkx_edges(self.graph, self.pos, edgelist=edges, edge_color="r",)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=labels)
        # print(nx.info(self.graph))
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.show()


