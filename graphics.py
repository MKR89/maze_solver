from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, w, h):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=h, width=w)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed.")
        
    def draw_line(self, line, fill_colour="black"):
        line.draw(self.__canvas, fill_colour)
            
    def close(self):
        self.__running = False
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        
    def draw(self, canvas, fill_colour="black"):
        canvas.create_line(
            self.point_1.x, self.point_1.y, 
            self.point_2.x, self.point_2.y, 
            fill=fill_colour, width=2
        )
        canvas.pack(fill=BOTH, expand=1)