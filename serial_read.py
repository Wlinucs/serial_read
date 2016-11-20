import serial
import winsound

try:
	ser=serial.Serial("com2",9600, 8, "N", 1, timeout=10)
	x=ser.read(1)
	ser.close()
	print(x)
except serial.serialutil.SerialException:
	print("porta non usabile")