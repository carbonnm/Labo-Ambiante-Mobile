import Dependencies._

ThisBuild / scalaVersion     := "2.13.12"
ThisBuild / version          := "0.1.0-SNAPSHOT"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"

lazy val root = (project in file("."))
  .settings(
    name := "TestPins",
    libraryDependencies += munit % Test,
    libraryDependencies ++= Seq(
      "org.slf4j" % "slf4j-api" % "1.7.35",
      "org.slf4j" % "slf4j-simple" % "1.7.35",
      "com.pi4j" % "pi4j-core" % "2.3.0",
      "com.pi4j" % "pi4j-plugin-raspberrypi" % "2.3.0",
      "com.pi4j" % "pi4j-plugin-pigpio" % "2.3.0"
    )
  )

// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
