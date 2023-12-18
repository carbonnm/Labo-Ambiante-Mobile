import com.pi4j.io.gpio.{GpioFactory, GpioPinDigitalOutput, RaspiPin, PinState}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future
import scala.concurrent.duration._

object BlinkLedScala extends App {

  // create gpio controller instance
  val gpio = GpioFactory.getInstance()

  // provision gpio pin #04 as an output pin and make sure it is set to LOW at startup
  val myLed: GpioPinDigitalOutput = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_04, "My LED", PinState.LOW)

  // schedule a task to toggle the state of the LED every 1 second
  val blinkTask: Future[Unit] = Future {
    while (true) {
      myLed.toggle()
      Thread.sleep(1000)
    }
  }

  // stop the blinking after 10 seconds
  val stopBlinkingTask: Future[Unit] = Future {
    Thread.sleep(10000)
    blinkTask.foreach(_ => println("Stopping blinking..."))
    gpio.shutdown()
  }

  // Wait for the blinking to stop
  stopBlinkingTask.onComplete(_ => println("Blinking stopped."))

  // Keep the application running
  while (true) {
    Thread.sleep(1000)
  }

}
