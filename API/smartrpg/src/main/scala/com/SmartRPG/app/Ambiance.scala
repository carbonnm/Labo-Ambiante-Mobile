package com.SmartRPG.app
import org.scalatra._

case class Ambiance(id : Int, name : String, musicName : String, couleurLed : String)

object AmbianceData {
    var ambiances = List(
        Ambiance(0, "forest", "", "green"),
        Ambiance(1, "volcano", "", "red"),
        Ambiance(2, "desert", "", "yellow"),
        Ambiance(3, "snow", "", "white")
    )
}