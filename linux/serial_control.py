import serial
import time

PORT = "/dev/ttyACM0"
BAUD = 9600

print("Opening serial port...")
ser = serial.Serial(PORT, BAUD, timeout=1)

# Arduino resets on serial open
time.sleep(2)

def send(cmd):
	ser.write(cmd.encode())
	time.sleep(0.1)
	resp = ser.readline().decode().strip()
	print(f"Sent: {cmd} | Received: {resp}")

send("1")
time.sleep(2)
send("0")

ser.close()
print("Serial closed.")
