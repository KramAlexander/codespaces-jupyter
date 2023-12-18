import colorsys
import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("white")
skk.speed(10000)
col = ['violet', 'indigo', 'blue', 
       'green', 'yellow', 'orange', 'red']

def generate_colors(num_colors):
    colors = []
    for i in range(num_colors):
        hue = i / num_colors  # Vary the hue from 0 to 1
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        colors.append(tuple(int(c * 255) for c in rgb))
    return colors
num_colors = 50
color_array = generate_colors(num_colors)
turl
for i in range(10):
    
    skk.forward(100)
    for i in range(7):
        skk.color(col[i])
        skk.forward(100)
        skk.right(60)

def sqrfunc(size):
    for i in range(8):
        skk.fd(size)
        skk.left(90)
        size = size +5
skk.goto(-50,100)
for i in range (8):
    sqrfunc(6+i*20)

turtle.done()