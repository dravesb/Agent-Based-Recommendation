from mesa import Agent
import numpy as np
import random


class Viewer(Agent):
    """A movie viewer."""
    def __init__(self, unique_id, num_agents, num_movies, model):
        super().__init__(unique_id, model)
        self.ratings = np.zeros(num_movies)
        self.is_rated = np.full([num_movies], False, dtype=bool)
        self.neighbors = random.sample(range(num_agents), 1)
        
        
    def update_neighbors(self, graph):
         return   
    
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
        
        #rate movie based on friends recommendation
        movie_id = self.get_movie_recommendation(non_rated_ind)
        #print(self.ratings)
        self.ratings[movie_id] = self.make_rating(movie_id)
        #print(self.ratings)
        self.is_rated[movie_id] = True
        #print('Viewer {} has rated movie {} a {}/100.'.format(self.unique_id, 
        #                                                 movie_id, 
        #                                                 int(round(100 * self.ratings[movie_id]))))
        