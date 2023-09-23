import tkinter

class Paint():
    # Things that run on class creation
    def __init__(self):
        # Displaying info to user
        print("To draw, hold down the left mouse button and move the cursor.")
        print("To change the brush colour, click on one of the colours.")

        # Creating Tkinter window
        self.window = tkinter.Tk()

        # Creating a canvas for the Tkinter window
        self.canvas = tkinter.Canvas(self.window, width = 800, height = 600, bg = "white")
        self.canvas.pack()

        self.lastX = 0
        self.lastY = 0

        # Setting default paint colour to black
        self.paint_colour = "black"


        # Binding mouse click to on_click
        self.canvas.bind("<Button-1>", self.on_click)

        # Binding mouse drag to on_drag
        self.canvas.bind("<B1-Motion>", self.on_drag)

        # Creating colour selection squares
        red_id = self.canvas.create_rectangle(10, 10, 30, 30, fill = "red")
        blue_id = self.canvas.create_rectangle(10, 35, 30, 55, fill = "blue")
        black_id = self.canvas.create_rectangle(10, 60, 30, 80, fill = "black")
        white_id = self.canvas.create_rectangle(10, 85, 30, 105, fill = "white")
        cyan_id = self.canvas.create_rectangle(10, 110, 30, 130, fill = "cyan")
        yellow_id = self.canvas.create_rectangle(10, 135, 30, 155, fill = "yellow")
        green_id = self.canvas.create_rectangle(10, 160, 30, 180, fill = "green")

        # Binding the colour selection buttons so when you click on them, the colour actually changes
        # This lambda stuff basically allows for an argument (or arguments) to be passed to the function set_colour
        self.canvas.tag_bind(red_id, "<Button-1>", lambda event, colour = "red": self.set_colour(colour))
        self.canvas.tag_bind(blue_id, "<Button-1>", lambda event, colour = "blue": self.set_colour(colour))
        self.canvas.tag_bind(black_id, "<Button-1>", lambda event, colour = "black": self.set_colour(colour))
        self.canvas.tag_bind(white_id, "<Button-1>", lambda event, colour = "white": self.set_colour(colour))
        self.canvas.tag_bind(cyan_id, "<Button-1>", lambda event, colour = "cyan": self.set_colour(colour))
        self.canvas.tag_bind(yellow_id, "<Button-1>", lambda event, colour = "yellow": self.set_colour(colour))
        self.canvas.tag_bind(green_id, "<Button-1>", lambda event, colour = "green": self.set_colour(colour))


        # Starting the Tkinter mainloop
        self.window.mainloop()


    def set_colour(self, colour):
        # Sets the class paint_colour variable to the function parameter
        self.paint_colour = colour

    def on_click(self, event):
        self.lastX = event.x
        self.lastY = event.y

    def on_drag(self, event):
        # If the drawn line would be over the colour selection areas:
        if (event.x <= 40 and event.y <= 190) or (self.lastX <= 40 and event.y <= 190):
            # Set new lastX and lastY values
            self.lastX = event.x
            self.lastY = event.y
            # But don't draw anything
            return
        else:
            # Actually draw a line
            self.canvas.create_line(self.lastX, self.lastY, event.x, event.y, fill = self.paint_colour, width = 3)

        # Set new lastX and lastY values
        self.lastX = event.x
        self.lastY = event.y


# Calling the Paint class
paint_window = Paint()