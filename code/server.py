from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from code.model import RatingModel 

#set up model paramters
model_params = {
	'N':UserSettableParameter(
        "slider", 'Viewers', 25, 1, 500, description="Number of Viewers"
    ),
    'M':UserSettableParameter(
        "slider", 'Movies', 25, 1, 500, description="Number of Movies"
    ),
    'K':UserSettableParameter(
        "slider", 'Categories', 1, 1, 10, description="Number of Movie Categories"
    ),
}

# add ratings matrix here
def viewer_portrayal(viewer):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}
    return portrayal

grid = CanvasGrid(viewer_portrayal, 10, model_params['N'], 500, 500)

# create instance of ModularServer 
server = ModularServer(
	RatingModel, 
	[grid],
	'Movie Rating Model', 
	model_params=model_params,
	)
