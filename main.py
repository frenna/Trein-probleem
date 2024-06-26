from classes import network
from algorithms import random, greedy, hillclimber, depth_first, breadth_first
import visualisatie
import matplotlib.pyplot as plt

if __name__ == "__main__":
    netwerk_holland = network.Network("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    netwerk_nationaal = network.Network("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")
    
    # Random algorithm
    random_algoritme = random.random_traject(netwerk_nationaal, 7, 120)
    visualisatie.visualisatie(random_algoritme.trajects, "data/kaarten/netherlands_.geojson")

    # Greedy algorithm
    greedy_algoritme = greedy.greedy_traject(netwerk_nationaal, 7, 120)
    visualisatie.visualisatie(greedy_algoritme.trajects, "data/kaarten/netherlands_.geojson")

    # Hillclimber algorithm
    hillclimber_trajects, hillclimber_score = hillclimber.hill_climber(netwerk_nationaal, max_time=120)
    visualisatie.visualisatie(hillclimber_trajects, "data/kaarten/netherlands_.geojson")

    # Depth First Search algorithm
    dfs_algoritme = depth_first.DepthFirst(netwerk_nationaal, max_time=120)
    dfs_solution, dfs_score = dfs_algoritme.search()
    visualisatie.visualisatie(dfs_solution.trajects, "data/kaarten/netherlands.geojson")

    # Breadth First Search algorithm
    bfs_algoritme = breadth_first.BreadthFirst(netwerk_nationaal, max_time=120)
    bfs_solution, bfs_score = bfs_algoritme.search()
    visualisatie.visualisatie(bfs_solution.trajects, "data/kaarten/netherlands.geojson")

    # Scores
    random_scores = []
    for _ in range(100):
        test_random = random.random_traject(netwerk_nationaal, 7, 120)
        random_scores.append(test_random.score())
        test_random.clear_trajects()

    visualisatie.histogram(random_scores, 'random algorithm')

    hillclimber_scores = []
    for _ in range(100):
        hillclimber_trajects, hillclimber_score = hillclimber.hill_climber(netwerk_nationaal, max_time=120)
        hillclimber_scores.append(hillclimber_score)
    
    visualisatie.histogram(hillclimber_scores, 'hillclimber algorithm')
    
    depth_scores = []
    for _ in range(100):
        depth_algoritme = depth_first.DepthFirst(netwerk_nationaal, max_time=120)
        depth_solution, depth_score = depth_algoritme.search()
        depth_scores.append(depth_score)

    visualisatie.histogram(depth_scores, 'Depth First Algorithm')

    breadth_scores = []
    for _ in range(100):
        breadth_algoritme = breadth_first.BreadthFirst(netwerk_nationaal, max_time=120)
        breadth_solution, breadth_score = breadth_algoritme.search()
        breadth_scores.append(bfs_score)

    visualisatie.histogram(breadth_scores, 'Breadth First Algorithm')



