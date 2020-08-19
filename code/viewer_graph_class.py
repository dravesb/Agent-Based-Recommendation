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
        P = np.full((K, K), .025)
        np.fill_diagonal(P, .3)
        
        #get G 
        self.groups = np.repeat(list(range(K)), group_sizes)
        self.adj_matrix = sbm(n = group_sizes, p = P)
    
