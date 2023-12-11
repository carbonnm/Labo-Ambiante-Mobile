package main.scala

import akka.actor.typed.ActorRef
import akka.actor.typed.Behavior
import akka.actor.typed.PostStop
import akka.actor.typed.Signal
import akka.actor.typed.scaladsl.AbstractBehavior
import akka.actor.typed.scaladsl.ActorContext
import akka.actor.typed.scaladsl.Behaviors
import akka.actor.typed.scaladsl.LoggerOps

object Map {
    def apply(groupId: String, deviceId: String): Behavior[Command] = {
        Behaviors.setup(context => new Map(context, groupId, deviceId))
    }
    // Ici on définit les différentes commandes (et réponses)
    sealed trait Command
    case object Passivate extends Command
}

class Map(context: ActorContext[Map.Command], groupId: String, deviceId: String) extends AbstractBehavior[Map.Command](context) {
    import Map._

    //Log start
    context.log.info2("Map actor {}-{} started", groupId, deviceId)

    override def onMessage(msg: Command): Behavior[Command] = {
        msg match {
            //Différents cas de messages
            case Passivate => {
                Behaviors.stopped
            }
        }
    }

    override def onSignal: PartialFunction[Signal, Behavior[Command]] = {
        case PostStop => {
            context.log.info2("Map actor {}-{} stopped", groupId, deviceId)
            this
        }
    }
}