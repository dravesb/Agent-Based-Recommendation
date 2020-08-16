from viewer_class import Viewer
from viewer_graph_class import ViewerGraph
from mesa import Model
from mesa.time import RandomActivation


class RatingModel(Model):
    """A model with some number of viewers."""
    def __init__(self, N, M):
        
        #Unpack arguments
        self.num_viewers = N
        self.num_movies = M
        self.step_count = 0 
        
        #Initialize viewer graph
        self.G = ViewerGraph(N)
        
        # Create agents and add to schedule        
        self.schedule = RandomActivation(self)
        for i in range(self.num_viewers):
            a = Viewer(i, self.num_viewers, self.num_movies, self.G)
            self.schedule.add(a)
        
            
    def get_current_ratings(self):
        print([a.ratings for a in self.schedule.agents])
        
    def step(self):
        #update Graph G
        self.G.update()
        self.step_count += 1
        #make the model take a step
        self.schedule.step()
        
