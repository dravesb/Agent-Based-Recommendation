var MatrixModule = function(matrix, canvas_width, canvas_height) {
    // Set up canvas
    var canvas_tag = "<canvas width='" + canvas_width + "' height='" + canvas_height + "' ";
    canvas_tag += "style='border:1px dotted'></canvas>";
    var canvas = $(canvas_tag)[0];
    $("#elements").append(canvas);
    var context = canvas.getContext("2d");

    //set matrix 
    var mat = math.matrix(matrix)

    //set up render and reset
    this.render = function(data) {
        for(var i = 0; i < math.size(mat)[0]; i++){
            for(var j = 0; j < math.size(mat)[1]; j++){
                var x = i * 30; var y = j * 30; 
                stroke(0);
                fill(mat[i][j])
                rect(x, y, 30, 30)
        }
    };

    this.reset = function() {
        
    };
};




