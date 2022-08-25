import machine, time
from machine import Pin

__version__ = '1.0'
__date__ = '21/8/2022'
__author__ = 'Dang Trung Hieu'
__license__ = "www.gvhieu.com, www.toituhoc.edu.vn"

class SERVO_ESP:
    def __init__(self, servo_Pin, freqServoDefault = 50, dutyMinDefault=29, dutyMaxDefault=150):
        self.servoPin = machine.PWM(Pin(servo_Pin, Pin.OUT), freq = freqServoDefault, duty = dutyMinDefault)
        self.dutyMin = dutyMinDefault
        self.dutyMax = dutyMaxDefault
    def map(self, x, inputMin, inputMax, outMin, outMax):
        return int((x - inputMin) * (outMax - outMin) / (inputMax - inputMin) + outMin);
    def angle(self, Angle):
        if Angle<0 : Angle = 0
        if Angle >180 : Angle = 180
        Angle = self.map(Angle, 0, 180, self.dutyMin, self.dutyMax);
        self.servoPin.duty(Angle)

class SERVO_PICO:
    def __init__(self, servo_Pin, freqServoDefault = 50, dutyMinDefault=1600, dutyMaxDefault=8320):
        self.servoPin = machine.PWM(Pin(servo_Pin, Pin.OUT))
        self.servoPin.freq(freqServoDefault)
        self.servoPin.duty_u16(dutyMinDefault)
        self.dutyMin = dutyMinDefault
        self.dutyMax = dutyMaxDefault
    def map(self, x, inputMin, inputMax, outMin, outMax):
        return int((x - inputMin) * (outMax - outMin) / (inputMax - inputMin) + outMin);
    def angle(self, Angle):
        if Angle<0 : Angle = 0
        if Angle >180 : Angle = 180
        Angle = self.map(Angle, 0, 180, self.dutyMin, self.dutyMax);
        self.servoPin.duty_u16(Angle)
