import numpy as np 
import random

class Movie():
    """A movie"""
    def __init__(self, unique_id, num_categories):
        self.id = unique_id
        self.quality = np.random.beta(2, 5)
        self.category = np.zeros(num_categories)
        self.category[random.randint(0, num_categories-1)] = 1
        