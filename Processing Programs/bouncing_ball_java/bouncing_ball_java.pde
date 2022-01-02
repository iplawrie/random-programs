int objectAmount = 10000;
int index;

Ball[] balls;

void setup() {
  size(1500, 1500);
  index = 0;
  balls = new Ball[objectAmount];
}

void draw() {
  if(index > 0){
    background(10);
    for (int i = 0; i < index; i++) {
      balls[i].update();
      balls[i].display();
      balls[i].checkBoundaryCollision();
      for (int j = 0; j < index; j++){
        if (balls[i] != balls[j]){
          balls[i].checkCollision(balls[j]);
        }
      }
    }
  }
}

void mouseClicked(){
  if(mouseButton == RIGHT){
    createBall();
  }else if (mouseButton == LEFT){
    deleteBall();
  }else{
    print("unknown button");
  }
}

void deleteBall(){
  print("right mouse click");
  int x = mouseX;
  int y = mouseY;
  for(int i = 0; i < index; i ++){
    if(balls[i].overlap(new PVector(x, y), 0)){
      for(int j = i; j < index; j++){
        balls[j] = balls[j+1];
      }
      index--;
      break;
    }
  }
}

void createBall(){
  boolean temp = true;
  do{
    int r = int(random(30, 100));
    int x = int(random(r, width-r));
    int y = int(random(r, height-r));
    
    if(balls[0] == null && index == 0){
      balls[index] = new Ball(x, y, r);
      index++;
      break;
    }
    for(int i = 0; i < index; i++){
      if(balls[i] != null){
        if(balls[i].overlap(new PVector(x, y), r)){
          break;
        }
      }
      if(i == index-1){
        balls[index] = new Ball(x, y, r);
        index++;
        temp = false;
      }
    }
  }while(temp);
}
