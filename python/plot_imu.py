import serial
import time
import matplotlib.pyplot as plt
from collections import deque

PORT = "/dev/ttyACM0"
BAUDRATE = 115200

MAX_POINTS = 200  # rolling window size

def main():
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    time.sleep(2)  # allow Arduino reset

    # Rolling buffers
    ax_buf = deque(maxlen=MAX_POINTS)
    ay_buf = deque(maxlen=MAX_POINTS)
    az_buf = deque(maxlen=MAX_POINTS)

    # Setup plot
    plt.ion()
    fig, ax = plt.subplots()
    line_ax, = ax.plot([], [], label="Accel X")
    line_ay, = ax.plot([], [], label="Accel Y")
    line_az, = ax.plot([], [], label="Accel Z")

    ax.set_title("MPU6050 Accelerometer (m/s^2)")
    ax.set_xlabel("Samples")
    ax.set_ylabel("Acceleration")
    ax.legend()
    ax.grid(True)

    print("Live plot running. Close the window or Ctrl+C to stop.")

    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if not line:
                continue

            values = line.split(",")
            if len(values) != 7:
                continue

            ax_val, ay_val, az_val = map(float, values[:3])

            ax_buf.append(ax_val)
            ay_buf.append(ay_val)
            az_buf.append(az_val)

            x = range(len(ax_buf))

            line_ax.set_data(x, ax_buf)
            line_ay.set_data(x, ay_buf)
            line_az.set_data(x, az_buf)

            ax.relim()
            ax.autoscale_view()

            plt.pause(0.01)

    except KeyboardInterrupt:
        print("Stopping plot...")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
