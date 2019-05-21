import sys, random, argparse
import numpy as np
import math
import turtle
from math import gcd


class Spiro:
        def __init__(self, xc, yc, col, R, r, l):
                self.t = turtle.Turtle()
                self.t.shape('classic')
                self.step = 5
                self.drawingComplete = False

                self.xc = xc
                self.yc = yc
                self.R = int(R)
                self.r = int(r)
                self.l = l
                self.col = col

                gcdVal = gcd(self.r, self.R)
                self.nRot = self.r//gcdVal
                self.k = r/float(R)
                self.t.color(*col)
                self.a = 0

                self.start()                

        def start(self):
                self.drawingComplete = False
                self.t.showturtle()
                self.t.up()
                R, k, l = self.R, self.k, self.l
                a = 0.0
                x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
                y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
                self.t.setpos(self.xc + x, self.yc + y)
                self.t.down()

        def update(self):
                if self.drawingComplete:
                        return
                self.a += self.step
                R, k, l = self.R, self.k, self.l
                a = math.radians(self.a)
                x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
                y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
                self.t.setpos(self.xc + x, self.yc + y)
                if self.a >= 360*self.nRot:
                        self.drawingComplete = True
                        self.t.hideturtle()

        def clear(self):
                self.t.clear()
                
class SpiroAnimator:
        def __init__(self):
                self.deltaT = 10
                self.width = turtle.window_width()
                self.height = turtle.window_height()
                rparams = self.genRandomParams()
                self.spiro = Spiro(*rparams)
                turtle.ontimer(self.update, self.deltaT)

        def genRandomParams(self):
                width, height = self.width, self.height
                R = height//2
                r = random.randint(10, 9*R//10)
                l = random.uniform(0.1, 0.9)
                xc = 0
                yc = 0
                col = (random.random(),
                        random.random(),
                        random.random())
                return (xc, yc, col, R, r, l)

        def update(self):
                self.spiro.update()
                if not self.spiro.drawingComplete:
                        turtle.ontimer(self.update, self.deltaT)
                

def main():
        turtle.setup(width=0.8)
        turtle.title('Spirographs')
        spiroAnim = SpiroAnimator()
        turtle.exitonclick()
        turtle.mainloop()

if __name__ == '__main__':
        main()
