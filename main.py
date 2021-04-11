import machine, time
led = machine.Pin(29, machine.Pin.OUT)
while True:
  led.high()
  time.sleep(1)
  led.low()
  time.sleep(1)
