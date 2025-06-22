from machine import Pin
from time import sleep

m_2 = Pin(2,Pin.OUT)
m_3 = Pin(3,Pin.OUT)
m_4 = Pin(4,Pin.OUT)
m_5 = Pin(5,Pin.OUT)

m_2.value(1)#前
m_3.value(0)
m_4.value(1)
m_5.value(0)
sleep(1)
m_2.value(0)#停
m_3.value(0)
m_4.value(0)
m_5.value(0)
sleep(1)
m_2.value(0)#后
m_3.value(1)
m_4.value(0)
m_5.value(1)
sleep(1)
m_2.value(0)#停
m_3.value(0)
m_4.value(0)
m_5.value(0)