package com.SmartRPG.app

import org.scalatra._

class BlogServlet extends ScalatraServlet {

  get("/") {
    views.html.hello()
  }

  get("/ambiances") {
    AmbianceData.ambiances
  }

  get("/ambiances/:id") {
    val id = params("id").toInt

    val ambiance = AmbianceData.ambiances.find(_.id == id)

    ambiance match {
      case Some(ambiance) => Ok(ambiance) // Ambiance trouvée, renvoie la réponse
      case None => NotFound("Ambiance non trouvée") // Ambiance non trouvée, renvoie une réponse 404
    }
  }

}
