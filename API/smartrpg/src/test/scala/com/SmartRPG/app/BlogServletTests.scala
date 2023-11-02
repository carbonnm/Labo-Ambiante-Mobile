package com.SmartRPG.app

import org.scalatra.test.scalatest._

class BlogServletTests extends ScalatraFunSuite {

  addServlet(classOf[BlogServlet], "/*")

  test("GET / on BlogServlet should return status 200") {
    get("/") {
      status should equal (200)
    }
  }

}
