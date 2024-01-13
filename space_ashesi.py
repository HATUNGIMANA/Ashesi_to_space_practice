import turtle
wn = turtle.Screen()
wn.bgpic('campus.gif') 
wn.addshape('rockets.gif')
sp_ship = turtle.Turtle()
sp_ship.speed(5)
sp_ship.shape('rockets.gif')

def text_position (): #to position the text 
    sp_ship.goto(200, -100)
    
def rockets_mvt(): #to give the picture with rockets a good position
    sp_ship.backward(200)
    
sp_ship.penup()
sp_ship.goto(-300, 245)
sp_ship.write("#Space_Exploration_Is_Worth_It!", font=('Verdana', 25, 'bold'))

text_position()
rockets_mvt()

wn.exitonclick()
