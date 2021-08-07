#Loosley following this tutorial:
#https://www.youtube.com/watch?v=VuUcgNSnIMM

import turtle

class Flower_Drawer():
    def __init__(self, radius, angel):
        self.radius = radius
        self.angle = angel

    def get_dimentions_of_a_petal(self):
        radius = self.radius
        angle = self.angle

    def draw_an_arc(self, name_of_arc, radius, angle):
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

#Daisy = turtle.Turtle()
#draw_a_flower(Daisy, 300, 50)
#Flower_Drawer(300, 50)
