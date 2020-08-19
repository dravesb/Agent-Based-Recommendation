from viewer_class import Viewer
from viewer_graph_class import ViewerGraph
from movie_class import Movie
from mesa import Model
from mesa.time import RandomActivation
import numpy as np

class RatingModel(Model):
    """A model with some number of viewers."""
    def __init__(self, N, M):
        
        #Unpack arguments
        self.num_viewers = N
        self.num_movies = M
        self.num_categories = 10
        
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
        
            
    def get_current_ratings(self):
        print([a.ratings for a in self.schedule.agents])
        
    def step(self):
        self.schedule.step()
        
