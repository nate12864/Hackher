from machine import I2C, Pin
import utime
import math

# Initialize I2C
i2c = I2C(1, scl=Pin(1), sda=Pin(0), freq=400000)

# MPU-6050 addresses and commands 
MPU6050_ADDR = 0x68
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
PWR_MGMT_1 = 0x6B

# Function to initialize the MPU-6050
def mpu6050_init():
    i2c.writeto_mem(MPU6050_ADDR, PWR_MGMT_1, bytearray([0]))

# Function to read raw values
def read_raw_values(addr):
    high = i2c.readfrom_mem(MPU6050_ADDR, addr, 1)[0]
    low = i2c.readfrom_mem(MPU6050_ADDR, addr+1, 1)[0]
    value = (high << 8) + low
    
    if value > 32768:
        value -= 65536
    return value

# Function to read acceleration
def read_acceleration():
    x = read_raw_values(ACCEL_XOUT_H)
    y = read_raw_values(ACCEL_YOUT_H)
    z = read_raw_values(ACCEL_ZOUT_H)
    
    return (x, y, z)

# Step detection setup
step_count = 0
threshold = 15000  
last_z = 0

mpu6050_init()

while True:
    x, y, z = read_acceleration()
    # Simple step detection algorithm 
    if abs(z - last_z) > threshold:
        step_count += 1
        print("Step detected. Total steps:", step_count)
    
    last_z = z
    utime.sleep(0.1)  # Delay to prevent too frequent readings
