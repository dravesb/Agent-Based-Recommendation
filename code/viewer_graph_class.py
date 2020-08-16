from graspy.simulations import sbm
import math

class ViewerGraph():
    """A graph of the viewers in the rating system."""
    def __init__(self, N):
        self.Graph = sbm(n = [math.ceil(N/2), math.floor(N/2)], p = [[.25, .05], [.05, .25]])
    
    def update(self):
        return 
