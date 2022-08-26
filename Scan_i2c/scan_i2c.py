#Scan địa chỉ các thiết bị i2c kết nối với Raspberry Pi Pico

#Raspberry pico hỗ trợ tối đa 2 kênh i2c

#Mặc định thì thiết bị giao tiếp qua GPIO8(SDA) chân thứ 11 và GPIO9(SCL) chân thứ 12

#Có thể sử dụng nhanh i2c=I2C(0), khi đó mặc định hiểu là SCL=Pin(9), SDA=Pin(8), freq=400000

#  * Connect ESP8266:

#  * option1: sda=12(D6), scl=14(D5)

#  * option2: sda=12(D6), scl=13(D7)

#  * Connect ESP32

#  * The ESP32 has two I2C channels and any pin can be set as SDA or SCL. When using the ESP32 with the Arduino IDE, the default I2C pins are

#  * GPIO21(SDA), GPIO22(SCL)


from machine import Pin, I2C

from time import sleep



i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq = 100_000) #freq tần số không bắt buộc



print("Đang scan i2c bus...");

devices = i2c.scan()

sleep(1)


if len(devices) == 0 :
    print("Không có thiết bị i2c được tìm thấy !")
else:
    print("Thiết bị i2c tìm được: ", len(devices)) 
    for element in devices:
        print("Địa chỉ theo số thập phân: ", element, " | Địa chỉ Hex (thập lục phân): ", hex(element))