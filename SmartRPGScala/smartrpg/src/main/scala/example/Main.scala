import com.pi4j.io.gpio.{GpioController, GpioFactory}
import com.pi4j.io.gpio.{GpioPinDigitalOutput, PinState, RaspiPin}

object Main extends App {
  // Initialiser le contrôleur GPIO
  val gpio: GpioController = GpioFactory.getInstance()

  // Créer une sortie GPIO pour la broche GPIO 1
  val pin: GpioPinDigitalOutput = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_01, "MyLED", PinState.HIGH)

  // Allumer la LED
  pin.high()

  // Attendre quelques secondes
  Thread.sleep(5000)

  // Éteindre la LED
  pin.low()

  // Libérer les ressources GPIO
  gpio.shutdown()
}