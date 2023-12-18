import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPin;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinDirection;
import com.pi4j.io.gpio.PinMode;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;
import com.pi4j.io.gpio.trigger.GpioCallbackTrigger;
import com.pi4j.io.gpio.trigger.GpioPulseStateTrigger;
import com.pi4j.io.gpio.trigger.GpioSetStateTrigger;
import com.pi4j.io.gpio.trigger.GpioSyncStateTrigger;
import com.pi4j.io.gpio.event.GpioPinListener;
import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
import com.pi4j.io.gpio.event.GpioPinEvent;
import com.pi4j.io.gpio.event.GpioPinListenerDigital;
import com.pi4j.io.gpio.event.PinEventType;
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
