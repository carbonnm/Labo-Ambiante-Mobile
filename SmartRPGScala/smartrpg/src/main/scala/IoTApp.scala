package main.scala

import akka.actor.typed.ActorSystem

object IoTApp {
    def main(args: Array[String]): Unit = {
        //Crée l'actor system grâce à IoTSupervisor
        ActorSystem[Nothing](IoTSupervisor(), "iot-system")
    }
}