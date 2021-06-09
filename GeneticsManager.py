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
        self.n_mutations = 1
        self.n_mutated_elements = 2  # musi byc parzyste!
        self.n_selected_animals = 2
        self.n_habitants = 5
        self.population = []
        self.graph = Graph()

    def generate_initial_population(self):
        nodes = list(self.graph.graph.nodes)
        for i in range(self.n_habitants):
            middle = nodes[1:self.graph.n_nodes - 1]
            shuffle(middle)
            nodes[1:self.graph.n_nodes - 1] = middle
            copy = deepcopy(nodes)
            element = [copy, self.length(copy)]
            self.population.append(element)
            print(self.population[i])
        # self.graph.show_graph()

    def length(self, path):
        l = 0
        for j in range(0, len(path) - 1):
            l += self.graph.graph[path[j]][path[j + 1]]['weight']
        return l

    def interbreed(self, path1, path2):
        result = np.zeros(len(path1))
        first_half = len(path1)//2
        second_half = len(path1)//2
        result[:first_half] = path1[:first_half]
        result[second_half:] = path2[second_half:]
        print(result)
        return result

    def mutate(self, path):
        for i in range(0, self.n_mutated_elements, 2):
            ind1 = randrange(0, len(path))
            ind2 = randrange(0, len(path))
            while ind1 == ind2:
                ind2 = randrange(0, len(path))
            print(f'To be mutated: {ind1}, {ind2}')
            path[ind1], path[ind2] = path[ind2], path[ind1]

    def iterate(self):
        self.generate_initial_population()

        # krzyzowanie
        for i in range(self.n_interbreeds):
            n1 = randrange(0, self.n_habitants)
            n2 = randrange(0, self.n_habitants)
            while n1 == n2:
                n2 = randrange(0, self.n_habitants)
            print(f'Random indexes: {n1}, {n2}')
            path1 = self.population[n1][0]
            path2 = self.population[n2][0]
            res_interbreed = self.interbreed(path1, path2)
            # trzeba dodac obsluge, gdy elementy w nowej sciezce beda sie powtarzaly i dodac je do populacji
            # self.population.append((res_interbreed, self.length(res_interbreed), ))

        # mutacje
        for i in range(self.n_mutations):
            n3 = randrange(0, self.n_habitants)
            print(f'Random: {n3}')
            path = self.population[n3][0]
            self.mutate(path)
            self.population[n3][0] = [path, self.length(path)]

        self.population.sort(key=sorting_key)
        print(self.population)

        # selekcja - usuwanie najgorszych rozwiazan
        for i in range(self.n_selected_animals):
            self.population.pop()
        print(self.population)

        self.graph.show_graph()