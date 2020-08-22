from mesa.visualization.ModularVisualization import VisualizationElement

class MatrixModule(VisualizationElement):
    package_includes = ["math.js"]
    local_includes = ["MatrixModule.js"]

    def __init__(self, matrix, grid_width, grid_height):    
        self.matrix = matrix
        self.grid_width = grid_width
        self.grid_height = grid_height
        

        new_element = "new MatrixModule({}, {}, {})".format(self.matrix, self.grid_width, self.grid_height)
        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
    	return model.get_current_ratings()