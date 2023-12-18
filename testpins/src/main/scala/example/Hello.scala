import com.pi4j.Pi4J
import com.pi4j.io.gpio.digital.{DigitalInput, DigitalOutput, DigitalState, PullResistance}
import com.pi4j.util.Console

object Pi4JMinimalExample {
  private val PIN_BUTTON = 24
  private val PIN_LED = 22
  private var pressCount = 0

  def main(args: Array[String]): Unit = {
    val console = new Console()
    val pi4j = Pi4J.newAutoContext()
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
      if (led.equals(DigitalState.HIGH)) {
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