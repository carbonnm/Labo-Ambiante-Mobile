val connectionSettings = MqttConnectionSettings(
  "tcp://localhost:1883", //L'adresse du broker MQTT
  "test-scala-client", //Un id unique pour le client
  new MemoryPersistence //La persistence du client qui permet de gérer la fiabilité
)