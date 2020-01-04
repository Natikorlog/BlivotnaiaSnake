from tkinter import *
import random


WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True



def create_block():
  
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy,
                          posx+SEG_SIZE, posy+SEG_SIZE,
                          fill="red")


def main():
   
    global IN_GAME
    if IN_GAME:
        s.move()
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
       
        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            create_block()
       
        else:
            for index in range(len(s.segments)-1):
                if head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False
        root.after(100, main)
   
    else:
        c.create_text(WIDTH/2, HEIGHT/2,
                      text="GAME OVER",
                      font="Arial 46",
                      fill="red")

class Segment(object):
   
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x+SEG_SIZE, y+SEG_SIZE,
                                           fill="white")


class Snake(object):
    
    def __init__(self, segments):
        self.segments = segments
       
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
       
        self.vector = self.mapping["Right"]

    def move(self):
        
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)

    def add_segment(self):
      
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
   
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
# мы циклом вводим игру в бесконечное самовоспроизведение.
while IN_GAME == True or IN_GAME == False:
	IN_GAME = True
	root = Tk()
	root.title("PythonicWay Snake")


	c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#AAAD2F")
	c.grid()

	c.focus_set()

	segments = [Segment(SEG_SIZE, SEG_SIZE),
	            Segment(SEG_SIZE*2, SEG_SIZE),
	            Segment(SEG_SIZE*3, SEG_SIZE)]
	s = Snake(segments)

	c.bind("<KeyPress>", s.change_direction)

	create_block()
	main()
	root.mainloop()
#Хотя нет, фича)