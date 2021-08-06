#Loosley following this tutorial:
#https://www.youtube.com/watch?v=VuUcgNSnIMM

import turtle

my_turtle = turtle.Turtle()

def draw_a_square():
    number_of_sides = 4
    for i in range(number_of_sides):
        my_turtle.fd(100)
        my_turtle.lt(90)
    turtle.mainloop()

def draw_a_polygon(name_of_polygon, angel, length):
    angle_of_each_turn = int(angel)
    length_of_each_side = int(length)
    number_of_iterations = int(360/angle_of_each_turn)
    for iteration in range(number_of_iterations):
        name_of_polygon.fd(length_of_each_side)
        name_of_polygon.lt(angle_of_each_turn)

#Square = turtle.Turtle()
#draw_a_polygon(Square, 90, 100)
#turtle.mainloop()

def draw_a_circle(radius):
    circle = turtle.Turtle()
    circle.circle(radius)
    turtle.mainloop()   

#draw_a_circle(60)

def draw_an_arc(name_of_arc, radius, angle):
    arc_length = 2* 3.14159 * radius * (angle/360)
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = angle/n

    name_of_arc.color("Black", "Yellow")
    name_of_arc.begin_fill()

    for iterations in range(n):
        name_of_arc.fd(step_length)
        name_of_arc.lt(step_angle)

    name_of_arc.end_fill()
    #turtle.mainloop()

#Half_Petal = turtle.Turtle()
#draw_an_arc(Half_Petal, 350, 50)

def draw_a_petal(name_of_petal, radius, angle):
    name_of_arc = name_of_petal
    for iteration in range(2):
        draw_an_arc(name_of_arc, radius, angle)
        name_of_petal.lt(180-angle)
    #turtle.mainloop() 

#Petal = turtle.Turtle()
#draw_a_petal(Petal, 300, 50)

def draw_a_flower(name_of_flower, radius, angle):
    name_of_petal = name_of_flower
    number_of_petals = 10
    for each_iteration in range(number_of_petals):
        draw_a_petal(name_of_petal, radius, angle)
        name_of_flower.lt(360/number_of_petals)
    turtle.mainloop()

Daisy = turtle.Turtle()
draw_a_flower(Daisy, 300, 50)