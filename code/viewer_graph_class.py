from graspy.simulations import sbm
import numpy as np
import math

class ViewerGraph():
    """A graph of the viewers in the rating system."""
    def __init__(self, N):
        #split in log(N) groups 
        K = math.floor(math.log(N))
        group_sizes = [math.floor(N / K)] * K
        group_sizes[0] += N - sum(group_sizes)
        
        #Make P 
        P = np.full((K, K), .05)
        np.fill_diagonal(P, .25)
        
        #get G 
        self.Graph = sbm(n = group_sizes, p = P)
    
    def update(self):
        return 
