from tkinter import *

# index 0, 1, 2 of this list line up directly with the value each radio
# button will carry, that's the trick that lets order() know which was picked
food = ["pizza", "hamburger", "hotdog"]


def order():
    # x.get() returns whichever value the currently selected radio button has
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("huh?")


window = Tk()

# PhotoImage loads a png and keeps it alive as long as something references it.
# These files need to sit in the same folder as this script, or you pass a full path.
pizzaImage = PhotoImage(file='C:\\Users\\T4WSIF\\Desktop\\PyNotes\\Tutorials\\profile_pic.jpg')
hamburgerImage = PhotoImage(file='C:\\Users\\T4WSIF\\Desktop\\PyNotes\\Tutorials\\profile_pic.jpg')
hotdogImage = PhotoImage(file='C:\\Users\\T4WSIF\\Desktop\\PyNotes\\Tutorials\\profile_pic.jpg')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

# IntVar is a Tkinter variable type that widgets can bind to directly.
# Every radio button below shares this same variable, that shared link is
# exactly what makes them behave as one group instead of three separate buttons.
x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[index],          # label shown next to the image
        variable=x,                 # shared variable, this is what groups the buttons
        value=index,                 # when this button is picked, x becomes this number
        padx=25,                     # horizontal breathing room inside the button
        font=("Impact", 50),
        image=foodImages[index],    # picture shown on the button
        compound='left',            # image on the left, text on the right of it
        indicatoron=0,               # turns off the little circle, button itself becomes the toggle
        width=375,
        command=order                # runs order() automatically on every click, no need to call it yourself
    )
    radiobutton.pack(anchor=W)
    # note: radiobutton gets reassigned each loop pass, but that's fine since
    # pack() already handed the widget over to the window, it doesn't depend
    # on this Python variable still pointing at it

window.mainloop()