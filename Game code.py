import turtle

grid_size = int(turtle.numinput("Grid Size", "How big should the grid be? "))
# color_input = input("What color should it be? ")
   
# create screen object 
sc = turtle.Screen() 
   
# create turtle object 
pen = turtle.Turtle() 
   
# method to draw square 
def draw(): 
   
  for i in range(4): 
    pen.forward(30) 
    pen.left(90) 
   
  pen.forward(30) 
   

def drawGrid():  
     
# Driver Code 
    if __name__ == "__main__" : 
      
        # set screen 
        sc.setup(600, 600)

        sc.tracer(0) 
       
        # set turtle object speed 
        pen.speed(0) 
       
        # loops for board 
        for i in range(grid_size): 
       
          # not ready to draw
          pen.hideturtle()
          pen.up() 
       
          # set position for every row 
          pen.setpos(0, 30 * i) 
       
          # ready to draw 
          pen.down() 
       
          # row 
          for j in range(grid_size): 
       
            # call method 
            draw()  
       
        # hide the turtle 

        sc.update() 

        # Keep the window open
        sc.mainloop() 

drawGrid()
