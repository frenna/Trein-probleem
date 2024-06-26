from .depth_first import DepthFirst
import copy

class BreadthFirst(DepthFirst):
    def __init__(self, network, max_time):
        super().__init__(network, max_time)
        self.states = [(self.network, self.network.create_traject())]

    def next_state(self):
        return self.states.pop(0)
