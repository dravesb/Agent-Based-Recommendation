# Executing the Model
import os 
os.chdir('/Users/benjamindraves/Desktop/Agent-Based-Recommendation/code')
from model_class import RatingModel
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Run the model for a certain number of steps
N = 100
M = 200
test_model = RatingModel(N, M)
for i in range(int(M/1.1)):
    test_model.step()

#cast as DataFrame for visualizations
data = np.array([
    [a.ratings[i] if a.ratings[i] != 0  else np.nan for i in range(M)] 
                          for a in test_model.schedule.agents])
df = pd.DataFrame(data = data,
                  index = ['User' + str(i) for i in range(N)],
                  columns = ['Movie' + str(j) for j in range(M)])

#Plot User and Movie Ratings
plt.hist(df.loc['User1'], bins = 10, alpha = .5)
plt.title('User1\'s ratings')
plt.show()

plt.hist(df['Movie1'], bins = 10, color = 'orange', alpha = .5)
plt.title('Movie1\'s ratings')
plt.show()

#make Heatmap of R = n x m ratings matrix 
R = df.to_numpy()
plt.figure(figsize = (int(10 * N/(N + M)), int(10 * M/(N + M))))
plt.imshow(R)
#plt.colorbar()
plt.title('Rating Matrix')
plt.xlabel('Movies')
plt.ylabel('Viewers')
plt.savefig('../figures/example_ratings_matrix.png')
#save for demo

