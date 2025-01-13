from pyfirmata import Arduino, util
import time

# Create a connection to the Arduino board
board = Arduino('COM3')  # replace '/dev/ttyACM0' with the port to which your Arduino board is connected

# Loop to blink the built-in LED
while True:
    board.digital[13].write(1)  # turn the LED on
    time.sleep(5)  # wait for 1 second
    board.digital[13].write(0)  # turn the LED off
    time.sleep(1)  # wait for 1 second