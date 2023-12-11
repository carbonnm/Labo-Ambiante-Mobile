package main.scala

import akka.actor.typed.ActorRef
import akka.actor.typed.Behavior
import akka.actor.typed.PostStop
import akka.actor.typed.Signal
import akka.actor.typed.scaladsl.AbstractBehavior
import akka.actor.typed.scaladsl.ActorContext
import akka.actor.typed.scaladsl.Behaviors
import akka.actor.typed.scaladsl.LoggerOps

object Leds {
    def apply(groupId: String, deviceId: String): Behavior[Command] = {
        Behaviors.setup(context => new Leds(context, groupId, deviceId))
    }
    // Ici on définit les différentes commandes (et réponses)
    sealed trait Command
}

class Leds(context: ActorContext[Leds.Command], groupId: String, deviceId: String) extends AbstractBehavior[Leds.Command](context) {
    import Leds._

    //Log start
    context.log.info2("Leds actor {}-{} started", groupId, deviceId)

    override def onMessage(msg: Command): Behavior[Command] = {
        msg match {
            //Différents cas de messages
        }
    }

    override def onSignal: PartialFunction[Signal, Behavior[Command]] = {
        case PostStop => {
            context.log.info2("Leds actor {}-{} stopped", groupId, deviceId)
            this
        }
    }
}