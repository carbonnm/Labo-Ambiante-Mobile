async function openConnectionDialog() {
  const goDice = new GoDice();
  try {
    await goDice.requestDevice();
  } catch {
    console.log("Error on connecting dice");
  }
}

GoDice.prototype.onDiceConnected = (diceId, diceInstance) => {
  //const socket = io();
  // dice identifier
  let diceIdentifier = diceId;

  // dice instance
  let diceClass = diceInstance;
  console.log("ID dice connected: ", diceIdentifier);
  console.log("Class dice connected: ", diceClass);

  //socket.emit("godice_message", { message: "dice++" });

  // socket.on("godice_message", (message) => {
  //   console.log(`Received message from Godice: ${message}`);
  // });
};

GoDice.prototype.onDiceDisconnected = (diceId, diceInstance) => {
  let dieIdentifier = diceId;
  let dieClass = diceInstance;
  console.log(" die disconnected: ", dieIdentifier);
  console.log(" class die : ", dieClass);
};

GoDice.prototype.onRollStart = (diceId) => {
  let diceIdentifier = diceId;
  console.log("rolling dice : ", diceIdentifier);
};

GoDice.prototype.onStable = (diceId, value, xyzAccRaw) => {
  let dieIdentifier = diceId;

  let dieValue = value;

  let accX = xyzAccRaw[0];
  let accY = xyzAccRaw[1];
  let accZ = xyzAccRaw[2];

  console.log(" dice  ID: ", dieIdentifier);
  console.log("die value : ", dieValue);
  console.log("accX : ", accX);
  console.log("accY : ", accY);
  console.log("accZ : ", accZ);
};

GoDice.prototype.onTiltStable = (diceId, xyzAccRaw, value) => {
  let dieIdentifier = diceId;

  let dieValue = value;

  let accX = xyzAccRaw[0];
  let accY = xyzAccRaw[1];
  let accZ = xyzAccRaw[2];

  console.log("tilt dice ID: ", dieIdentifier);
  console.log("tilt die value : ", dieValue);
  console.log("tilt accX : ", accX);
  console.log("tilt accY : ", accY);
  console.log("tilt accZ : ", accZ);
};

GoDice.prototype.onFakeStable = (diceId, value, xyzAccRaw) => {
  let dieIdentifier = diceId;

  let dieValue = value;

  let accX = xyzAccRaw[0];
  let accY = xyzAccRaw[1];
  let accZ = xyzAccRaw[2];

  console.log("fake dice ID: ", dieIdentifier);
  console.log("fake die value : ", dieValue);
  console.log("fake accX : ", accX);
  console.log("fake accY : ", accY);
  console.log("fake accZ : ", accZ);
};

GoDice.prototype.onMoveStable = (diceId, value, xyzAccRaw) => {
  let dieIdentifier = diceId;

  let dieValue = value;

  let accX = xyzAccRaw[0];
  let accY = xyzAccRaw[1];
  let accZ = xyzAccRaw[2];

  console.log("move dice ID: ", dieIdentifier);
  console.log("move die value : ", dieValue);
  console.log("move accX : ", accX);
  console.log("move accY : ", accY);
  console.log("move accZ : ", accZ);
};
