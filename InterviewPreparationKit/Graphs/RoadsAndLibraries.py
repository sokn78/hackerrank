c_lib = 2
c_road = 5

cities = [
    [1, 3],
    [2, 4],
    [1, 2],
    [2, 3],
    [3, 4],
    [5, 6]]

n = 6

def roadsAndLibraries(n, c_lib, c_road, cities):
    roads = cities
    cities = range(1, n + 1)
    neighbors = dict()

    for dep, arrival in roads + [(b, a) for a, b in roads]:
        neighbors.setdefault(arrival, set()).add(dep)

    city_cliques = dict()


    def add_element(city, clique_id):
        if city not in city_cliques:
            city_cliques[city] = clique_id
            if city in neighbors:
                for nbghd in neighbors[city]:
                    add_element(nbghd, clique_id)


    add_element(cities[0], 0)

    clique_id = 0
    for city in cities:
        add_element(city, clique_id)
        clique_id += 1

    cliques_population = dict()

    for _, clique_id in city_cliques.items():
        cliques_population[clique_id] = cliques_population.get(clique_id, 0) + 1


    def cost_function(nb, c_lib, c_road):
        if c_road > c_lib:
            return nb * c_lib
        else:
            return c_lib + (nb - 1) * c_road


    return sum([cost_function(clique_population, c_lib, c_road) for _, clique_population in cliques_population.items()])

print(roadsAndLibraries(n, c_lib, c_road, cities))