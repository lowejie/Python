import turtle

screen = turtle.Screen()
screen.title("Malaysia States Game")
image = "blank_states_my_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coordinates(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coordinates)

turtle.mainloop()

screen.exitonclick()