import copy

class DepthFirst:
    def __init__(self, network, max_time):
        self.network = copy.deepcopy(network)
        self.max_time = max_time
        self.states = [(self.network, self.network.create_traject())]
        self.best_solution = None
        self.best_value = float('-inf')

    def next_state(self):
        return self.states.pop()

    def generate_state(self, network, traject):
        current_station = traject.get_last_station()
        possible_connections = [connect for connect in network.connections if current_station.name in (connect.station1.name, connect.station2.name)]

        for connection in possible_connections:
            new_network = copy.deepcopy(network)
            new_traject = copy.deepcopy(traject)

            if connection.time + new_traject.total_time > self.max_time:
                continue

            if current_station.name == connection.station1.name:
                new_traject.add_station(connection.station2)
            else:
                new_traject.add_station(connection.station1)

            new_traject.update_time(connection.time)
            new_network.connections.remove(connection)

            self.states.append((new_network, new_traject))

    def evaluate(self, network):
        value = network.score()
        if value > self.best_value:
            self.best_solution = copy.deepcopy(network)
            self.best_value = value

    def search(self):
        while self.states:
            new_network, new_traject = self.next_state()

            if new_traject.total_time <= self.max_time:
                self.generate_state(new_network, new_traject)

            new_network.add_traject(new_traject)
            self.evaluate(new_network)

        return self.best_solution, self.best_value
