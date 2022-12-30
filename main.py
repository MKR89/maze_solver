from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.__root = Tk()
        self.__root.title("Window")
        self.__canvas = Canvas(width=self.w, height=self.h)
        self.__canvas.pack()
        running = False
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            
    def close(self):
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
def main():
    win = Window(800, 600)
    win.wait_for_close()
    
if __name__ == "__main__":
    main()
        