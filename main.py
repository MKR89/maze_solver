from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.__root = Tk()
        self.__root.title("Window")
        self.__canvas = Canvas(width=self.w, height=self.h)
        self.__canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            
    def close(self):
        self.running = False
        
    def draw_line(self, line, fill_colour="black"):
        line.draw(self.__canvas, fill_colour)
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        
    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.point_1.x, self.point_1.y, 
            self.point_2.x, self.point_2.y, 
            fill=fill_colour, width=2
        )
        canvas.pack(fill=BOTH, expand=1)
        
def main():
    win = Window(800, 600)
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, "red")
    win.wait_for_close()
    
if __name__ == "__main__":
    main()
        