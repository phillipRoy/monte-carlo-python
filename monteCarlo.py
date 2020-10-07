import sys
import random
from graphics import *

win = GraphWin("Monte Carlo", 600, 600, autoflush=True)
arguments = sys.argv

def monteCarlo(pointsIn):
    x = random.randint(100, 499)
    y = random.randint(100, 499)
    if((pow((x - 300), 2) + pow((y - 300), 2)) <= pow(200, 2)):
        pointsIn = pointsIn + 1
    p = Point(x, y)
    p.draw(win)
    return pointsIn
    
def main():
    pointsIn = 0
    r = Rectangle(Point(100, 100), Point(500, 500))
    c = Circle(Point(300, 300), 200)
    r.draw(win)
    c.draw(win)
    for i in range(int(arguments[1])):
        pointsIn = monteCarlo(pointsIn)
    print(4 * (pointsIn/int(arguments[1])))
    win.getMouse() # pause for click in window
    win.close()

main()