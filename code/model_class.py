from viewer_class import Viewer
from viewer_graph_class import ViewerGraph
from mesa import Model
from mesa.time import RandomActivation


class RatingModel(Model):
    """A model with some number of viewers."""
    def __init__(self, N, M):
        #Initialize viewer graph
        self.G = ViewerGraph(N)
        
        # Create agents and add to schedule        
        self.num_agents = N
        self.schedule = RandomActivation(self)
        for i in range(self.num_agents):
            a = Viewer(i, N, M, self.G)
            self.schedule.add(a)
    
        
    def step(self):
        #update Graph G
        self.G.update()
        
        #make the model take a step
        self.schedule.step()
        
