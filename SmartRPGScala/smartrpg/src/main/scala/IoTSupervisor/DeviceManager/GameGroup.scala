package main.scala

import akka.actor.typed.ActorRef
import akka.actor.typed.Behavior
import akka.actor.typed.PostStop
import akka.actor.typed.Signal
import akka.actor.typed.scaladsl.AbstractBehavior
import akka.actor.typed.scaladsl.ActorContext
import akka.actor.typed.scaladsl.Behaviors
import akka.actor.typed.scaladsl.LoggerOps

object GameGroup {
    def apply(groupId: String) : Behavior[Command] = {
        Behaviors.setup(context => new GameGroup(context, groupId))
    }
    // Ici on définit les différentes commandes (et réponses)
    sealed trait Command
}

class GameGroup(context: ActorContext[GameGroup.Command], groupId: String) extends AbstractBehavior[GameGroup.Command](context) {
    import GameGroup._
    //Ici j'import ce dont j'ai besoin du DeviceManager
    //import DeviceManager.{ DeviceRegistered, ReplyDeviceList, RequestDeviceList, RequestTrackDevice }

    //Utilisation d'un map pour chercher les enfants acteurs (sera soit un lecteur RFID soit un moteur pour nous)
    //private var gameIdToActor = Map.empty[String, ActorRef[_]]


    //Log start
    context.log.info("GameGroup {} started", groupId)
    
    override def onMessage(msg: Command): Behavior[Command] = {
        /*
        msg match {
            //groupID à définir mieux en string
            case trackMsg @ RequestTrackDevice("groupId", deviceId, replyTo) =>
                gameIdToActor.get(deviceId) match {
                    //Existe déjà
                    case Some(deviceActor) => {
                        replyTo ! DeviceRegistered(deviceActor)
                    }
                    //Il faut le créer
                    case None => {
                        context.log.info("Creating device actor for {}", trackMsg.deviceId)
                        //Ici au lieu d'avoir Device on aura RfidChest et Motor ensemble
                        val deviceActor = context.spawn(Device(groupId, deviceId), s"device-$deviceId")
                        gameIdToActor += deviceId -> deviceActor
                        replyTo ! DeviceRegistered(deviceActor)
                    }
                }
                this

            case RequestTrackDevice(gId, _, _) => {
                context.log.warn2("Ignoring TrackDevice request for {}. This actor is responsible for {}.", gId, groupId)
                this
            }
        }
        */
    }

    override def onSignal: PartialFunction[Signal, Behavior[Command]] = {
        case PostStop => {
            context.log.info("GamereGroup {} stopped", groupId)
            this
        }
    }
}