import math

listOfBalls = []
r = 50
colors = [0, 255]
boxWidth = 1500
boxHeight = 1500

def setup():
    size(boxWidth, boxHeight)
    noStroke()
    background(255)
    listOfBalls.append(Ball(int(random(boxWidth-r)), int(random(boxHeight-r)), r))
    
def draw():
    for i in range(100):
        ranX = int(random(boxWidth))
        ranY = int(random(boxHeight))
        for index in range(len(listOfBalls)):
            if listOfBalls[index].overlap(ranX, ranY, r) or not withinBox(ranX, ranY, r):
                break    
            if index == len(listOfBalls)-1:
                listOfBalls.append(Ball(ranX, ranY, r))
                print(len(listOfBalls))
               
def withinBox(x, y, radius):
    if x >= radius/2 and x <= boxWidth-(radius/2) and y >= radius/2 and y <= boxHeight-(radius/2):
        return True
    return False

class Ball():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.display()
        
    def display(self):
        c1 = colors[int(random(2))]
        c2 = colors[int(random(2))]
        c3 = colors[int(random(2))]
        stroke(0)
        fill(c1, c2, c3)
        b = createShape(ELLIPSE, self.x, self.y, self.radius, self.radius)
        shape(b)
        

    def overlap(self, x, y, radius):
        if math.sqrt(((x - self.x)**2) + ((y - self.y)**2)) <= r:
            return True
        return False
