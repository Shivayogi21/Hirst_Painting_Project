# import colorgram
#
# colors=colorgram.extract('hirstimg.jpg',30)
# rgb_colors=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as turtle_module
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(241, 232, 77), (186, 12, 40), (105, 180, 208), (193, 72, 31), (18, 122, 170), (219, 64, 103), (211, 152, 104), (190, 177, 16), (16, 140, 86), (240, 231, 2), (17, 31, 74), (189, 41, 67), (69, 172, 98), (14, 167, 212), (216, 130, 153), (216, 75, 55), (36, 46, 115), (127, 187, 132), (235, 166, 183), (5, 56, 33), (7, 104, 54), (147, 209, 222), (168, 21, 16), (233, 172, 165), (156, 213, 185), (93, 13, 57)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1,number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen=turtle_module.Screen()
screen.exitonclick()