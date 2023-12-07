import turtle
import random

class Polygon:
    def __init__(self, size, x, y, vx, vy, color):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()


    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self):
        # specify a reduction ratio to draw a smaller polygon inside the one above
        reduction_ratio = 0.618

        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]

        # adjust the size according to the reduction ratio
        size *= reduction_ratio

        # draw the second polygon embedded inside the original
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()




class DrawPolygon:
    def __init__(self, choice):
        self.choice = choice
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        for i in range(self.choice):
            # draw a polygon at a random location, orientation, color, and border line thickness
            num_sides = random.randint(3, 5)  # triangle, square, or pentagon
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = Polygon.get_new_color()
            border_size = random.randint(1, 10)
            Polygon.draw_polygon(num_sides, size, orientation, location, color, border_size)


select = input('Which art do you want to generate? Enter a number between 1 to 8, inclusive: ')
my_generate = DrawPolygon(select)
my_generate.run()


