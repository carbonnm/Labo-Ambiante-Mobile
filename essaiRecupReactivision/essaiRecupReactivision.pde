import TUIO.*;

//Creation of an instance of the tuioClient
TuioProcessing tuioClient;

//Variables we want to get
float pos_x, pos_y, rotation;

void setup() {
  size(640, 480);
  stroke(240);
  tuioClient = new TuioProcessing(this);
}

void draw() {
  ArrayList<TuioObject> listObjects = tuioClient.getTuioObjectList();
  background(0);
  
  for( int i = 0; i < listObjects.size(); i++) {
    
  } 
}

//Fonctions à implémenter
void addTuioObject(TuioObject tobject) {
  println("ID : " + tobject.getSymbolID() + "Session ID : (" + tobject.getSessionID() + ") " + "Position x : " + tobject.getX() + "Position y : " + tobject.getY() + "Rotation : " + tobject.getAngle());
}

void updateTuioObject(TuioObject tobject) {
  println("ID : " + tobject.getSymbolID() + "Session ID : (" + tobject.getSessionID() + ") " + "Position x : " + tobject.getX() + "Position y : " + tobject.getY() + "Rotation : " + tobject.getAngle());
}

void removeTuioObject(TuioObject tobject) {
  println("ID : " + tobject.getSymbolID() + "Session ID : (" + tobject.getSessionID() + ") ");
}
