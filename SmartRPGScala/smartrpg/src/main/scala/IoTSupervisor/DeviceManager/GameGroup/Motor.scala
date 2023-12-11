package main.scala

import akka.actor.typed.ActorRef
import akka.actor.typed.Behavior
import akka.actor.typed.PostStop
import akka.actor.typed.Signal
import akka.actor.typed.scaladsl.AbstractBehavior
import akka.actor.typed.scaladsl.ActorContext
import akka.actor.typed.scaladsl.Behaviors
import akka.actor.typed.scaladsl.LoggerOps

object Motor {
    def apply(groupId: String, deviceId: String): Behavior[Command] = {
        Behaviors.setup(context => new Motor(context, groupId, deviceId))

        // Ici on définit les différentes commandes (et réponses)
        sealed trait Command
    }
}

class Motor(context: ActorContext[Motor.Command], groupId: String, deviceId: String) extends AbstractBehavior[Motor.Command](context) {
    import Motor._

    //Log start
    context.log.info2("Motor actor {}-{} started", groupId, deviceId)

    override def onMessage(msg: Command): Behavior[Command] = {
        msg match {
            //Différents cas de messages
        }
    }

    override def onSignal: PartialFunction[Signal, Behavior[Command]] = {
        case PostStop => {
            context.log.info2("Motor actor {}-{} stopped", groupId, deviceId)
            this
        }
    }
}