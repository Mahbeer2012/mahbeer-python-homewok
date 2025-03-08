import turtle
turtle.Screen().bgcolor("light blue")
turtle.Screen().setup(300,300)

polygon = turtle.Turtle()

num_sides = int(input("enter number of sides: "))
side_length = 56
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.color('purple')
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()