import framboos.OutPin

object LEDController extends App {
  // Replace 0 with the actual GPIO pin number to which the LED is connected
  val ledPin = OutPin(0)

  try {
    while (true) {
      // Turn on the LED
      ledPin.setValue(true)
      Thread.sleep(1000) // Wait for 1 second

      // Turn off the LED
      ledPin.setValue(false)
      Thread.sleep(1000) // Wait for 1 second
    }
  } finally {
    // Make sure to close the pin when done
    ledPin.close()
  }
}
