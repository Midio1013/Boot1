from machine import Pin
from servo import Servo
from time import sleep

s_0 = Servo(pin=0)
s_1 = Servo(pin=1)
l_1 = Pin(25,Pin.OUT)
m_2 = Pin(2,Pin.OUT)
m_3 = Pin(3,Pin.OUT)
m_4 = Pin(4,Pin.OUT)
m_5 = Pin(5,Pin.OUT)

l_1.value(1)

m_2.value(1)#前
m_3.value(0)
m_4.value(1)
m_5.value(0)
sleep(1)
m_2.value(0)#停
m_3.value(0)
m_4.value(0)
m_5.value(0)

s_0.move(90)
s_1.move(90)
sleep(1)
s_1.move(155)
sleep(1)
s_1.move(25)
sleep(1)
s_0.move(90)
s_1.move(90)
sleep(1)
s_0.move(155)
sleep(1)
s_0.move(25)
sleep(1)
s_0.move(90)
s_1.move(90)