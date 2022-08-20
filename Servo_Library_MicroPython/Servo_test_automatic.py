import machine, time
from machine import Pin
from servo import*
#ESP8266: servoPin=5 (D1), ESP32: servoPin=16, Pico servoPin=0
servoPin = 0
#myServo = SERVO_ESP(servoPin)
myServo = SERVO_PICO(servoPin)

while True:
    myServo.angle(0)
    print("Angle = 0 degree");
    time.sleep(1)
    myServo.angle(90)
    print("Angle = 90 degrees");
    time.sleep(1)
    myServo.angle(180)
    print("Angle = 180 degrees");
    time.sleep(1)
    myServo.angle(0)
    print("Angle = 0 degree");
    time.sleep(1)
    for x in range(0, 181):
        myServo.angle(x)
        print("Angle =", x, "degrees")
        time.sleep_ms(10)
    time.sleep(1)
    for x in range(180, -1, -1):
        myServo.angle(x)
        print("Angle =", x, "degrees")
        time.sleep_ms(10)
    time.sleep(1)
