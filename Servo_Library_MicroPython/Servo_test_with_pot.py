import machine, time
from machine import Pin, ADC
from servo import*
#ESP8266: servoPin=5 (D1), ESP32: servoPin=16, Pico servoPin=0
servoPin = 0
#myServo = SERVO_ESP(servoPin)
myServo = SERVO_PICO(servoPin)

pot = ADC(0) #A0, ESP8266
myServo.angle(0)
time.sleep(1)
while True:
    #ESP
    #x = pot.read()
    #x = int(x/1024 * 180)
    
    #for Raspberry Pico
    x = pot.read_u16()
    x = int(x/65535 * 180)
    print(x)
    myServo.angle(x)
    time.sleep_ms(100)