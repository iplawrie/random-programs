import math

listBalls = []
c = 50
r = int(c/2)

def setup():
    size(1000, 1000)
    noStroke()
    background(255)
    createBalls(5)
    
def draw():
    background(255)
    for ball in listBalls:
        ball.display()
        ball.move()
    
def createBalls(numBall):
    num = 0
    if not listBalls:
        listBalls.append( Ball(int(random(r, width-r)), int(random(r, height-r)), c,  int(random(0,5)), int(random(0,5)), num) )
        num += 1
        numBall -= 1
    
    for i in range(numBall):
        loopBreak = True
        while loopBreak:
            x = int(random(r,width-r))
            y = int(random(r, height-r))
            xVel = int(random(0, 5))
            yVel = int(random(0, 5))
            for index in range(len(listBalls)):
                if listBalls[index].overlap(x, y, r):
                    break
                if index == len(listBalls)-1:
                    listBalls.append(Ball(x, y, c, xVel, yVel, num))
                    num += 1
                    loopBreak = False
    print("ball creation completed")

class Ball():
    def __init__(self, x, y, r, xVel, yVel, num):
        self.x = x
        self.y = y
        self.c = c
        self.xVel = xVel
        self.yVel = yVel
        self.ballnum = num
        
    def display(self):
        stroke(0)
        textSize(25)
        fill(0)
        b = createShape(ELLIPSE, self.x, self.y, self.c, self.c)
        shape(b)
        fill(255)
        textAlign(CENTER)
        text(str(self.ballnum), self.x, self.y+10)
        
    def move(self):
        self.x += self.xVel
        self.y += self.yVel
        if self.x > width-r or self.x < r:
            self.xVel = -self.xVel
        if self.y > height-r or self.y < r:
            self.yVel = -self.yVel
    
    def overlap(self, x, y, r):
        if math.sqrt(((x - self.x)**2) + ((y - self.y)**2)) <= r:
            return True
        return False
