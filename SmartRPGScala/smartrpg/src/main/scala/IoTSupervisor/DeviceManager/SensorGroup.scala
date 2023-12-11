package main.scala

import akka.actor.typed.ActorRef
import akka.actor.typed.Behavior
import akka.actor.typed.PostStop
import akka.actor.typed.Signal
import akka.actor.typed.scaladsl.AbstractBehavior
import akka.actor.typed.scaladsl.ActorContext
import akka.actor.typed.scaladsl.Behaviors
import akka.actor.typed.scaladsl.LoggerOps

object SensorGroup {
    def apply(groupId: String) : Behavior[Command] = {
        Behaviors.setup(context => new SensorGroup(context, groupId))
    }
    // Ici on définit les différentes commandes (et réponses)
    sealed trait Command
}

class SensorGroup(context: ActorContext[SensorGroup.Command], groupId: String) extends AbstractBehavior[SensorGroup.Command](context) {
    import SensorGroup._
    //Ici j'import ce dont j'ai besoin du DeviceManager
    import DeviceManager.{ DeviceRegistered, ReplyDeviceList, RequestDeviceList, RequestTrackDevice }

    //Utilisation d'un map pour chercher les enfants acteurs (à adapter pour nous donc)
    private var deviceIdToActor = Map.empty[String, ActorRef[Device.Command]]


    //Log start
    context.log.info("SensorGroup {} started", groupId)

    override def onMessage(msg: Command): Behavior[Command] = {
        msg match {
            case trackMsg @ RequestTrackDevice(`groupId`, deviceId, replyTo) =>
                deviceIdToActor.get(deviceId) match {
                    //Existe déjà
                    case Some(deviceActor) => {
                        replyTo ! DeviceRegistered(deviceActor)
                    }
                    //Il faut le créer
                    case None => {
                        context.log.info("Creating device actor for {}", trackMsg.deviceId)
                        val deviceActor = context.spawn(Device(groupId, deviceId), s"device-$deviceId")
                        deviceIdToActor += deviceId -> deviceActor
                        replyTo ! DeviceRegistered(deviceActor)
                    }
                }
                this

            //Wrong group
            case RequestTrackDevice(gId, _, _) => {
                context.log.warn2("Ignoring TrackDevice request for {}. This actor is responsible for {}.", gId, groupId)
                this
            }
        }
    }

    override def onSignal: PartialFunction[Signal, Behavior[Command]] = {
        case PostStop => {
            context.log.info("SensorGroup {} stopped", groupId)
            this
        }
    }
}