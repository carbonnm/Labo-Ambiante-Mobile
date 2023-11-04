import TUIO.*;

TuioProcessing tuioClient;

int [] [] tilemap = {
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
};

int rows, cols ;
int cellWidth, cellHeight;

void setup() {
  size(1425, 825);
  tuioClient = new TuioProcessing(this);
  rows = tilemap.length;
  cols = tilemap[0].length;
  cellWidth = 110;
  cellHeight = 118;
  ellipseMode(CENTER);
}

void draw() {
  background(120);
  ArrayList<TuioObject> listObjects = tuioClient.getTuioObjectList();
  for(int i = 0; i < listObjects.size(); i++) {
    TuioObject patronAux = listObjects.get(i);
    pushMatrix();
    translate(patronAux.getScreenX(width), patronAux.getScreenY(width));
    ellipse(0, 0, 60, 60);
    popMatrix();
  }
  renderMap();
}

void renderMap() {
  for(int i = 0; i < rows; i++) {
    for(int j = 0; j < cols; j++) {
      switch(tilemap[i][j]) {
        case 0:
          fill(114, 188, 128);
          rect(j * cellWidth, i * cellHeight, cellWidth, cellHeight);
          break;
        case 1:
          fill(80);
          rect(j * cellWidth, i * cellHeight, cellWidth, cellHeight);
          break;
        default:
          break;
      }
    }
  }
}

//Code reactivision
void addTuioObject(TuioObject tobject) {
  println("ID : " + tobject.getSymbolID() + "Session ID : (" + tobject.getSessionID() + ") " + "Position x : " + tobject.getX() + "Position y : " + tobject.getY() + "Rotation : " + tobject.getAngle());
}

void updateTuioObject(TuioObject tobject) {
  println("ID : " + tobject.getSymbolID() + "Session ID : (" + tobject.getSessionID() + ") " + "Position x : " + tobject.getX() + "Position y : " + tobject.getY() + "Rotation : " + tobject.getAngle());
}

void removeTuioObject(TuioObject tobject) {
  println("ID : " + tobject.getSymbolID() + "Session ID : (" + tobject.getSessionID() + ") ");
}
