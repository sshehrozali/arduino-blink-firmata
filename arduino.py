import pyfirmata, time

board = pyfirmata.Arduino("COM5")   # Connect with Serial
led = board.get_pin("d:13:o")       # Define PIN number

while True:
    led.write(1)
    time.sleep(.5)

    led.write(0)
    time.sleep(.5)