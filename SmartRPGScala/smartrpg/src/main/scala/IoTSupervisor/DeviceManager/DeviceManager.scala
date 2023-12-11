package main.scala

import akka.actor.typed.ActorRef
import akka.actor.typed.Behavior
import akka.actor.typed.PostStop
import akka.actor.typed.Signal
import akka.actor.typed.scaladsl.AbstractBehavior
import akka.actor.typed.scaladsl.ActorContext
import akka.actor.typed.scaladsl.Behaviors
import akka.actor.typed.scaladsl.LoggerOps

object DeviceManager {
    def apply(): Behavior[Command] = {
        Behaviors.setup(context => new DeviceManager(context))
    }

    sealed trait Command
    //a définir
}

class DeviceManager(context: ActorContext[DeviceManager.Command]) extends AbstractBehavior[DeviceManager.Command](context) {
    import DeviceManager._

    //Log start
    context.log.info("DeviceManager started")

    override def onSignal: PartialFunction[Signal, Behavior[Command]] = {
        case PostStop => {
            context.log.info("DeviceManager stopped")
            this
        }
    }
}