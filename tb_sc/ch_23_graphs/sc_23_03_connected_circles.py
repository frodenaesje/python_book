# file: sc_23_03_connected_circles.py
from tkinter import Canvas, Event, Tk
from sc_23_01_graph import Graph

Circle = tuple[int, int]

def add(event: Event):
    circles.append((event.x, event.y))
    repaint()

def distance(circle1: Circle, circle2: Circle) -> float:
    return ((circle1[0] - circle2[0]) ** 2 
            + (circle1[1] - circle2[1]) ** 2) ** 0.5

def repaint():
    canvas.delete("point")

    if len(circles) == 0:
        return  # Nothing to paint

    graph = Graph(directed=False)

    # Add all circle indices as vertices so isolated circles are included.
    for i in range(len(circles)):
        graph.add_vertex(str(i))

    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            if distance(circles[i], circles[j]) <= 2 * radius:
                graph.add_edge(str(i), str(j))

    isAllCirclesConnected = len(graph.connected_components()) == 1

    for [x, y] in circles:
        if isAllCirclesConnected: # All circles are connected
            canvas.create_oval(x - radius, y - radius, x + radius, 
                y + radius, fill = "red", tags = "point")
        else:
            canvas.create_oval(x - radius, y - radius, x + radius, 
                y + radius, tags = "point")            

window = Tk() # Create a window
window.title("ConnectedCircles") # Set title

width = 500
height = 400
radius = 15
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing circles
circles: list[Circle] = []

canvas.bind("<Button-1>", add)

window.mainloop() # Create an event loop