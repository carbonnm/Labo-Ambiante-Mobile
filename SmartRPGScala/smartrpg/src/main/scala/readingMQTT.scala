//Créer une source qui se connecte à un serveur MQTT et reçoit les messages des topics abonnés
//Future[Done] est complété quand l'abonnement au MQTT broker est établie

val mqttSource: Source[MqttMessage, Future[Done]] = {
    MqttSource.atMostOnce(
        connectionSettings
            .withClientId(clientId = "source-spec/source"),
            .withCleanSession(false),
        MqttSubscriptions(topic, MqttQoS.AtLeastOnce),
        //Exemple avec plusieurs topics
        //MqttSubscriptions(Map(topic1 -> MqttQoS.AtLeastOnce, topic2 -> MqttQoS.AtLeastOnce)),
        //Nombre de message max lus avant qu'ils ne s'effacent
        bufferSize = 8
  )
}

val result = mqttSource
  .via(businessLogic)
  //Les ACKs
  .mapAsync(1)(messageWithAck => messageWithAck.ack().map(_ => messageWithAck.message))
  .take(input.size)
  .runWith(Sink.seq)