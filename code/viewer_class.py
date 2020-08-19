from mesa import Agent
import numpy as np


class Viewer(Agent):
    """A movie viewer."""
    def __init__(self, unique_id, num_agents, num_movies, neighbor_ids, model):
        super().__init__(unique_id, model)
        self.ratings = np.zeros(num_movies)
        self.is_rated = np.full([num_movies], False, dtype=bool)
        self.neighbors = neighbor_ids
        self.preferences = np.random.dirichlet(np.full((model.num_categories), 
                                                       1/(model.num_categories)), 
                                               size = 1)
    
    def get_movie_recommendation(self, lst):
        #just choose a random movie in the list
        return(np.random.choice(lst, 1)[0])
    
    def make_rating(self, movie_id):
        #return random rating
        return(np.random.beta(1, 1))        
    
    def step(self):
        #check if all movies have been rated
        non_rated_ind = np.where(self.is_rated == False)[0]
        if len(non_rated_ind) == 0:
            print('Viewer ' + str(self.unique_id) + 'has seen all movies.')
            return
        
        #rate movie after choosing recommendations from friends
        movie_id = self.get_movie_recommendation(non_rated_ind)
        self.ratings[movie_id] = self.make_rating(movie_id)
        self.is_rated[movie_id] = True

        