import TUIO.*;

TuioProcessing tuioClient;

void setup() {
  size(1425, 825);
  tuioClient = new TuioProcessing(this);
}

void draw() {
  background(120);
  ArrayList<TuioObject> listObjects = tuioClient.getTuioObjectList();
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
