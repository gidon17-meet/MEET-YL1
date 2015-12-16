from meet import *
import meet
import math
import random
cells=[]
for i in range(0,20):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    radius= random.randint(10,40)
    xdirection= random.randint(0,1)
    ydirection= random.randint(2,3)
    speed = 25
    if xdirection== 0:
        _dx= -radius/ speed
    if xdirection==1:
        _dx= radius/ speed
    if ydirection==2:
        _dy= radius/ speed
    if ydirection==3:
        _dy= -radius/ speed

        
    cell1={'x':meet.get_random_x(),'y':meet.get_random_y(),'radius':radius,'dx':_dx,'dy':_dy, 'color':random_color}
    a= create_cell(cell1)
    cells.append(a)
user= {"x":meet.get_x_mouse(), "y":meet.get_y_mouse(),"radius":25, "dx":_dx,"dy":_dy}
user= create_cell(user)
cells.append(user)
def border():
    right= meet.get_screen_width()
    left= -meet.get_screen_width()
    up= meet.get_screen_height()
    down= -meet.get_screen_height()
    for cell in cells:
        if cell.xcor() + cell.get_radius() >= right:
            cell.set_dx(-cell.get_dx())
        if cell.xcor() - cell.get_radius() <= left:
            cell.set_dx(-cell.get_dx())
        if cell.ycor() + cell.get_radius() >= up:
            cell.set_dy(-cell.get_dy())
        if cell.ycor() - cell.get_radius() <= down:
            cell.set_dy(-cell.get_dy())

alive = True
while alive:
    
    move_cells(cells)
    border()
    dx,dy=meet.get_user_direction(user)
    user.set_dx(dx)
    user.set_dy(dy)

    for cell in cells:
        for other in cells:
            distance = ((cell.xcor() - other.xcor())**2 + (cell.ycor() - other.ycor())**2)**0.5
            if distance <= cell.get_radius():
                if cell.get_radius() > other.get_radius():
                    if other == user:
                        alive = False
                    else:
                        cell.set_radius(cell.get_radius()+other.get_radius()/10)
                        other.goto(get_random_x(),get_random_y())
