void setup(){
  size(2000, 2000);
  boardSetup();
}
void draw(){
  stop();
}

void boardSetup(){
  int widthDiv = width/20;
  int heightDiv = height/3;
  stroke(255);
  strokeWeight(2);
  for(int i = 5; i < 15; i++){
    line(widthDiv*i, 0, widthDiv*i, height);
  }
}
