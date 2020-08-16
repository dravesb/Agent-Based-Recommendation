# Actually Running the Model

import os
os.chdir('/Users/benjamindraves/Desktop/Agent-Based-Recommendation/code')

from model_class import RatingModel


#
test_run = RatingModel(10, 20)
test_run.step()
