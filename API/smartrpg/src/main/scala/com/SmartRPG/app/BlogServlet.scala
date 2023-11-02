package com.SmartRPG.app

import org.scalatra._

class BlogServlet extends ScalatraServlet {

  get("/") {
    views.html.hello()
  }

}
