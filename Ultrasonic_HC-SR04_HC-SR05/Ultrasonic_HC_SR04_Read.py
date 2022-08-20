import machine, time
from machine import Pin

#ESP8266
#trigPin = 12 #D6
#echoPin = 13 #D7

#ESP32
#trigPin = 16
#echoPin = 17

#Raspberry Pi Pico
trigPin = 0 #label 1
echoPin = 1 #lable 2

trigger = Pin(trigPin, mode = Pin.OUT)
echo = Pin(echoPin, mode = Pin.IN)

while True:
    trigger.off() #off trig pin 5 microseconds
    time.sleep_us(5)
    trigger.on() #on trig pin 10 microseconds
    time.sleep_us(10)
    trigger.off()
    #use, machine.time_pulse_us(pin, pulse_level, timeout_us=1000000)
    timeWaiting = machine.time_pulse_us(echo, 1, 10_000)
    distance = int(timeWaiting / 2 * 0.0343)
    print(distance,"cm")
    time.sleep_ms(100)
