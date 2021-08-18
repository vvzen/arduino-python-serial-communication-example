import time

import serial

ARDUINO_URL = "/dev/tty.usbmodem142301"
MAX_WAIT = 32 # seconds
ARDUINO_RESET_WAIT_TIME = 5 # seconds
END_MESSAGE_DELIMITER = b">"

def hello_world():
    serial_device = serial.Serial(ARDUINO_URL, 9600, timeout=1)
    print("Will talk to ", serial_device.name)

    # This is fundamental! Give enough time to arduino to reset
    # before trying to write and read from the serial
    print("Waiting %i seconds for arduino to reset.. " % ARDUINO_RESET_WAIT_TIME)
    time.sleep(ARDUINO_RESET_WAIT_TIME)

    hello_world_message = b"<MoveX10Y10>"

    print("Sending  ", hello_world_message.decode("ascii"))
    serial_device.write(hello_world_message)

    current_message = []

    i = 0
    while True:
        current_char = serial_device.read(1)
        current_message.append(current_char)
        # print(current_char)
        if current_char == END_MESSAGE_DELIMITER:
            break

        i += 1
        if i > MAX_WAIT:
            print("Closing communication, timeout was reached without "
                  "finding end of message ", END_MESSAGE_DELIMITER)
            break

    # Read as bytes, decode them into ascii
    message_as_ascii = "".join([c.decode("ascii") for c in current_message])
    print("Received ", message_as_ascii)

    serial_device.close()

def main():
    hello_world()

if __name__ == '__main__':
    main()
