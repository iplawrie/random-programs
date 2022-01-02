import java.util.Arrays;
import java.lang.Math.*;

int arraySize = 10000;
Ball ballList[] = new Ball[arraySize];
int arrayIndex = 1;
int r = 20;
int colors[] = {0, 255};
int boxWidth = 1500;
int boxHeight = 1400;

void setup(){
  size(1500, 1400);
  noStroke();
  background(255);
}

void draw(){
  for(int x = 0; x < 10000; x++){
    int r1 = int(random(boxWidth));
    int r2 = int(random(boxHeight));
    for( int i = 0; i < arraySize; i++){
      if(ballList[i] != null){
        if (ballList[i].within(r1, r2) || !withinBox(r1, r2)){
          break;
        }
      }
      if(i == arraySize-1){
        if (arrayIndex < arraySize){
          print(arrayIndex + "\n");
          ballList[arrayIndex] = new Ball(r1, r2);
          arrayIndex += 1;
        }else{
          print("limit reached");
          stop();
        }
      }
    }
  }
}

boolean withinBox(int x, int y){
  if(x >= r/2+1 && x <= boxWidth-(r/2+1) && y >= r/2+1 && y <= boxHeight-(r/2+1)){
    return true;
  }
  return false;
}

class Ball{
  int x, y;
  Ball(int mx, int my){
    x = mx;
    y = my;
    color c1 = colors[int(random(2))];
    color c2 = colors[int(random(2))];
    color c3 = colors[int(random(2))];
    PShape ball = createShape(ELLIPSE, x, y, r, r);
    stroke(0);
    fill(c1, c2, c3);
    strokeWeight(1);
    //stroke(colors[int(random(3))],colors[int(random(3))],colors[int(random(3))]);
    shape(ball);
  }
  
  boolean within(int checkX, int checkY){
    if( Math.sqrt((x-checkX)*(x-checkX) + (y-checkY)*(y-checkY)) <= r){
      return true;
    }
    return false;
  }
  
}
