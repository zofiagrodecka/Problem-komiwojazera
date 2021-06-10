from Graph import Graph
from random import shuffle, randrange
from copy import deepcopy
import numpy as np


def sorting_key(element):
    return element[1]


class GeneticsManager:
    def __init__(self):
        self.iterations = 5
        self.n_interbreeds = 3
        self.n_mutations = 2
        self.n_mutated_elements = 2  # musi byc parzyste!
        self.n_selected_animals = 3
        self.n_habitants = 5
        self.population = []
        self.graph = Graph()
        self.generate_initial_population()

    def generate_initial_population(self):
        nodes = list(self.graph.graph.nodes)
        for i in range(self.n_habitants):
            middle = nodes[1:]
            shuffle(middle)
            nodes[1:] = middle
            copy = deepcopy(nodes)
            element = [copy, self.length(copy)]
            self.population.append(element)
            # print(self.population[i])
        # self.graph.show_graph()

    def length(self, path):
        l = 0
        for j in range(0, len(path) - 1):
            l += self.graph.graph[path[j]][path[j + 1]]['weight']
        return l

    def interbreed(self, path1, path2):  # krzyzowanie
        result = [0 for _ in range(len(path1))]
        first_half = len(path1)//2
        # second_half = len(path1)//2
        result[:first_half] = path1[:first_half]
        result[first_half:] = [x for x in path2 if x not in result[:first_half]]
        return result

    def mutate(self, path):
        for i in range(0, self.n_mutated_elements, 2):
            ind1 = randrange(1, len(path))
            ind2 = randrange(1, len(path))
            while ind1 == ind2:
                ind2 = randrange(1, len(path))
            path[ind1], path[ind2] = path[ind2], path[ind1]

    def iterate(self):
        # krzyzowanie
        for i in range(self.n_interbreeds):
            n1 = randrange(0, self.n_habitants)
            n2 = randrange(0, self.n_habitants)
            while n1 == n2:
                n2 = randrange(0, self.n_habitants)
            path1 = self.population[n1][0]
            path2 = self.population[n2][0]
            res_interbreed = self.interbreed(path1, path2)
            # trzeba dodac obsluge, gdy elementy w nowej sciezce beda sie powtarzaly i dodac je do populacji
            self.population.append([res_interbreed, self.length(res_interbreed)])

        # mutacje
        for i in range(self.n_mutations):
            n3 = randrange(0, len(self.population))
            path = self.population[n3][0]
            self.mutate(path)
            self.population[n3] = [path, self.length(path)]

        self.population.sort(key=sorting_key)
        # print(self.population)

        # selekcja - usuwanie najgorszych rozwiazan
        for i in range(self.n_selected_animals):
            self.population.pop()
        # print(self.population)
        self.get_length()
        # self.show()

    # def show(self):
    #     self.graph.show_graph(self.population[0][0])

    def get_graph_path(self):
        return self.graph.get_graph_image(self.population[0][0])

    def get_length(self):
        # print(self.population[0][1])
        return self.population[0][1]
