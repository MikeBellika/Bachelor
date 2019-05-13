import serial
import time

PORT = "/dev/ttyUSB0"
SER = serial.Serial(port = PORT, baudrate = 1, timeout = 1)

def my_write(b):
    b = bytearray.fromhex(b)
    print("WRITING " + str(b))
    print("SER WRITE: " + str(SER.write(b)))

# while True:
my_write("2F3F210D0A")
    # time.sleep(0.2)
# while True:
a = SER.read(1)
    # if len(a) == 0:
    #     print("nothing")
    #     continue
    # print("------------SOMETHING--------")
    # print(a)
