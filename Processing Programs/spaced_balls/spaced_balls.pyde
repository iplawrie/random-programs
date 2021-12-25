listOfBalls = []
r = 20
xtest = 0
ytest = 0

def setup():
    size(500, 500)
    noStroke()
    background(0)
    listOfBalls.append(Ball(50, 50, r))
    
    
def draw():
    for index, ball in enumerate(listOfBalls):
        if False:#ball.within(mouseX, mouseY, r):
            break
        else:
            if index == len(listOfBalls)-1:
               listOfBalls.append(Ball(xtest, ytest, r))

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
        b = createShape(ELLIPSE, x, y, radius, radius)
        fill(255)
        shape(b)
        
    """def within(self, x, y, radius):
        return False"""
