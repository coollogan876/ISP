import serial

arduino = serial.Serial('/dev/ttyACM0')
arduino.reset_input_buffer()

while True:
    if arduino.in_waiting > 0:
        print(arduino.readline().decode('utf-8').rstrip())
        print('\n')
        