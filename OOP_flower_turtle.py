#Loosley following this tutorial:
#https://www.youtube.com/watch?v=VuUcgNSnIMM

import turtle

class Flower_Drawer():
    def __init__(self, name_of_flower, radius, angle):
        self.turtle = turtle.Turtle()
        self.name_of_flower = name_of_flower
        self.radius = radius
        self.angle = angle

    def draw_an_arc(self):
        arc_length = 2* 3.14159 * self.radius * (self.angle/360)
        n = int(arc_length/3) + 1
        step_length = arc_length/n
        step_angle = self.angle/n

        self.turtle.color("Black", "Yellow")
        self.turtle.begin_fill()

        for iterations in range(n):
            self.turtle.fd(step_length)
            self.turtle.lt(step_angle)

        self.turtle.end_fill()

    def draw_a_petal(self):
        for iteration in range(2):
            self.draw_an_arc()
            self.turtle.lt(180-self.angle)

    def draw_a_flower(self):
        number_of_petals = 10
        for each_iteration in range(number_of_petals):
            self.draw_a_petal()
            self.turtle.lt(360/number_of_petals)
        turtle.mainloop()

Daisy = Flower_Drawer("Daisy", 300, 50)
print(Daisy.draw_a_flower())