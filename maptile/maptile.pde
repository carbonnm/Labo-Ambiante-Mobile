
int [] [] tilemap = {
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
};

int rows, cols ;
int cellWidth, cellHeight;

void setup() {
  size(640, 640);
  rows = tilemap.length;
  cols = tilemap[0].length;
  cellWidth = 64;
  cellHeight = 64;
}

void draw() {
  background(120);
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
