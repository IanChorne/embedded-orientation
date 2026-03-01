import serial
import time

PORT = "/dev/ttyACM0"
BAUDRATE = 115200

def main():
    print("Opening serial port...")
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    time.sleep(2)  # allow Arduino reset

    print("Reading IMU data. Press Ctrl+C to stop.\n")

    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if not line:
                continue

            values = line.split(",")

            if len(values) != 7:
                continue  # skip malformed lines

            ax, ay, az, gx, gy, gz, temp = map(float, values)

            print(
                f"Accel (m/s^2): x={ax:.2f}, y={ay:.2f}, z={az:.2f} | "
                f"Gyro (rad/s): x={gx:.2f}, y={gy:.2f}, z={gz:.2f} | "
                f"Temp: {temp:.1f} C"
            )

    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
