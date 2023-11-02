val ScalatraVersion = "3.0.0"

ThisBuild / scalaVersion := "3.3.1"
ThisBuild / organization := "com.SmartRPG"

lazy val hello = (project in file("."))
  .settings(
    name := "SmartRPG",
    version := "semantic versioning",
    libraryDependencies ++= Seq(
      "org.scalatra" %% "scalatra-jakarta" % ScalatraVersion,
      "org.scalatra" %% "scalatra-scalatest-jakarta" % ScalatraVersion % "test",
      "ch.qos.logback" % "logback-classic" % "1.4.11" % "runtime",
      "org.eclipse.jetty" % "jetty-webapp" % "11.0.17" % "container",
      "jakarta.servlet" % "jakarta.servlet-api" % "5.0.0" % "provided"
    ),
  )

enablePlugins(SbtTwirl)
enablePlugins(JettyPlugin)

Jetty / containerLibs := Seq("org.eclipse.jetty" % "jetty-runner" % "11.0.17" intransitive())
