
import RPi.GPIO as GPIO
import time
import adafruit_dht
import board
from urllib.request import urlopen

flamepin = 25
RELAY_PIN_1 = 6
TRIG = 23
ECHO = 24

dhtDevice = adafruit_dht.DHT11(board.D18, use_pulseio=False)

while True:
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(flamepin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(RELAY_PIN_1, GPIO.OUT)

        temp_c = dhtDevice.temperature
        humid = dhtDevice.humidity
        print(f"Temperature (°C): {temp_c}, Humidity (%): {humid}")

        time.sleep(4)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.output(TRIG, False)
        time.sleep(5)

        GPIO.output(TRIG, True)
        time.sleep(1)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        print(f"Distance: {distance} cm")

        baseURL = 'https://api.thingspeak.com/update?api_key=D3XVWO0K1K136EE2'
        f = urlopen(baseURL + f"&field1={temp_c}&field2={humid}&field3={distance}&field4={GPIO.input(flamepin)}")
        print(f"Data sent: {f}")
        time.sleep(3.0)

        GPIO.cleanup()

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
