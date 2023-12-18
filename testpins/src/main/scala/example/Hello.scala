//usr/bin/env jbang "$0" "$@" ; exit $?

//DEPS org.slf4j:slf4j-api:1.7.35
//DEPS org.slf4j:slf4j-simple:1.7.35
//DEPS com.pi4j:pi4j-core:2.3.0
//DEPS com.pi4j:pi4j-plugin-raspberrypi:2.3.0
//DEPS com.pi4j:pi4j-plugin-pigpio:2.3.0

import com.pi4j.Pi4J
import com.pi4j.io.gpio.digital.{DigitalInput, DigitalOutput, DigitalState, PullResistance}
import com.pi4j.util.Console

object Pi4JMinimalExample {
  // Connect a button to PIN 18 = BCM 24
  private val PIN_BUTTON = 24
  // Connect a LED to PIN 15 = BCM 22
  private val PIN_LED = 22

  private var pressCount = 0

  @throws[Exception]
  def main(args: Array[String]): Unit = {
    val console = new Console
    val pi4j = Pi4J.newAutoContext

    val ledConfig = DigitalOutput.newConfigBuilder(pi4j)
      .id("led")
      .name("LED Flasher")
      .address(PIN_LED)
      .shutdown(DigitalState.LOW)
      .initial(DigitalState.LOW)
      .provider("pigpio-digital-output")
    val led = pi4j.create(ledConfig)

    val buttonConfig = DigitalInput.newConfigBuilder(pi4j)
      .id("button")
      .name("Press button")
      .address(PIN_BUTTON)
      .pull(PullResistance.PULL_DOWN)
      .debounce(3000L)
      .provider("pigpio-digital-input")
    val button = pi4j.create(buttonConfig)
    button.addListener(e => {
      if (e.state() == DigitalState.LOW) {
        pressCount += 1
        console.println("Button was pressed for the " + pressCount + "th time")
      }
    })

    while (pressCount < 5) {
      if (led.getState == DigitalState.HIGH) {
        console.println("LED low")
        led.low()
      } else {
        console.println("LED high")
        led.high()
      }
      Thread.sleep(500 / (pressCount + 1))
    }

    pi4j.shutdown()
  }
}