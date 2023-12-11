package main.scala

import akka.actor.typed.ActorRef
import akka.actor.typed.Behavior
import akka.actor.typed.PostStop
import akka.actor.typed.Signal
import akka.actor.typed.scaladsl.AbstractBehavior
import akka.actor.typed.scaladsl.ActorContext
import akka.actor.typed.scaladsl.Behaviors
import akka.actor.typed.scaladsl.LoggerOps

object Book {
    def apply(groupId: String, deviceId: String): Behavior[Command] = {
        Behaviors.setup(context => new Book(context, groupId, deviceId))
    }
    // Ici on définit les différentes commandes (et réponses)
    sealed trait Command
    case object Passivate extends Command
}

class Book(context: ActorContext[Book.Command], groupId: String, deviceId: String) extends AbstractBehavior[Book.Command](context) {
    import Book._

    //Log start
    context.log.info2("Book actor {}-{} started", groupId, deviceId)

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
            context.log.info2("Book actor {}-{} stopped", groupId, deviceId)
            this
        }
    }
}