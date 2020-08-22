from code.viewer_class import Viewer
from code.viewer_graph_class import ViewerGraph
from code.movie_class import Movie
from mesa import Model
from mesa.time import RandomActivation
import numpy as np
from mesa.space import MultiGrid


class RatingModel(Model):
    """A model with some number of viewers."""
    def __init__(self, N, M, K):
        
        #Unpack arguments
        self.num_viewers = N
        self.num_movies = M
        self.num_categories = K
        self.grid = MultiGrid(1, N, True)

        #Initialize viewer graph
        self.viewer_graph = ViewerGraph(N)
        
        #create movies and movie list
        self.movies = []
        for i in range(self.num_movies):
            self.movies.append(Movie(i, self.num_categories))
            
        # Create viewers and add to schedule        
        self.schedule = RandomActivation(self)
        for i in range(self.num_viewers):
            a = Viewer(i, self.num_viewers, self.num_movies, 
                       np.nonzero(self.viewer_graph.adj_matrix[i, :]), self)
            self.schedule.add(a)

            # Add the agent to a grid cell
            self.grid.place_agent(a, (0, i))
        
            
    def get_current_ratings(self):
        return [a.ratings for a in self.schedule.agents]
        
    def step(self):
        self.schedule.step()

    def run_model(self):
    	for i in range(self.run_time):
    		self.step()
        
