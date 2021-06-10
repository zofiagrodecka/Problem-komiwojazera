
class Statistics:
    def __init__(self):
        self.statistics = {}

    def to_text_population(self, population):
        result = ""
        for id, (path, length) in enumerate(population):
            path_str = ''.join(str(e)+"-" for e in path[:-1])
            path_str += str(path[-1])
            result += f"{id} {path_str} ({length})\n"
        return result

    def mutation_to_text(self, path_id, indices_pair):
        return f"Do mutacji wybrano ścieżkę {path_id} i wierzchołki {indices_pair}"

    def interbreeding_to_text(self, paths_id):
        return f"Do krzyżówki wybrano ścieżki {paths_id}"

    def clear(self):
        self.statistics = {}