import tkinter as tk
import random

LARG=400; ALT=300

def colisao(x1,y1,x2,y2,dist=20):
    return abs(x1-x2)<dist and abs(y1-y2)<dist

class Jogo:
    def __init__(self,root):
        self.c=tk.Canvas(root,width=LARG,height=ALT); self.c.pack()
        self.jx=200; self.bala=None
        self.ex=random.randint(20,380); self.ey=40
        root.bind("<Left>",lambda e:self.mover(-10))
        root.bind("<Right>",lambda e:self.mover(10))
        root.bind("<space>",lambda e:self.atirar())
        self.loop()

    def mover(self,d):
        self.jx=max(10,min(LARG-10,self.jx+d))

    def atirar(self):
        if not self.bala: self.bala=[self.jx,ALT-30]

    def loop(self):
        self.c.delete("all")
        self.c.create_rectangle(self.jx-10,ALT-20,self.jx+10,ALT,fill="blue")
        self.c.create_oval(self.ex-10,self.ey-10,self.ex+10,self.ey+10,fill="red")
        if self.bala:
            self.bala[1]-=10
            self.c.create_rectangle(self.bala[0]-2,self.bala[1]-10,self.bala[0]+2,self.bala[1],fill="black")
            if colisao(self.bala[0],self.bala[1],self.ex,self.ey):
                self.ex=random.randint(20,380); self.bala=None
        self.c.after(30,self.loop)

if __name__=="__main__":
    r=tk.Tk(); r.title("Mini Shooter"); Jogo(r); r.mainloop()
