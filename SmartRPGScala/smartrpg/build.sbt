import Dependencies._

ThisBuild / scalaVersion     := "2.13.12"
ThisBuild / version          := "0.1.0-SNAPSHOT"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"

resolvers += "Akka library repository".at("https://repo.akka.io/maven")

val AkkaVersion = "2.9.0"

lazy val root = (project in file("."))
  .settings(
    name := "SmartRPG",
    libraryDependencies += munit % Test,
    libraryDependencies += "com.typesafe.akka" %% "akka-remote" % AkkaVersion,
    libraryDependencies += "com.typesafe.akka" %% "akka-actor-typed" % AkkaVersion,
    libraryDependencies += "ch.qos.logback" % "logback-classic" % "1.2.6"
  )

// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
