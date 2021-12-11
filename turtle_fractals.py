import turtle as tl

def draw_fractal(scale):
    if scale >= 5:
        draw_fractal(scale / 3.0)
        tl.left(60)
        draw_fractal(scale / 3.0)
        tl.right(120)
        draw_fractal(scale / 3.0)
        tl.left(60)
        draw_fractal(scale / 3.0)
        tl.left(60)
        draw_fractal(scale / 3.0)
        tl.right(120)
        draw_fractal(scale / 3.0)
        tl.left(60)
        draw_fractal(scale / 3.0)
        tl.left(60)
        draw_fractal(scale / 3.0)
        tl.right(120)
        draw_fractal(scale / 3.0)
        tl.left(60)
        draw_fractal(scale / 3.0)
    else:
        tl.forward(scale)

scale = 250
tl.pensize(1)
tl.penup()
tl.color('green')
tl.goto(-scale, -scale/5)
tl.pendown()

draw_fractal(scale)
tl.done()