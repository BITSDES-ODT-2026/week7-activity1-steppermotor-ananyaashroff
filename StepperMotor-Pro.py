from machine import Pin
import time

in1 = Pin(5, Pin.OUT)
in2 = Pin(12, Pin.OUT)
in3 = Pin(25, Pin.OUT)
in4 = Pin(19, Pin.OUT)

steps = 500

while True:
    for i in range(steps):
        in1.value(1)
        in2.value(0)
        in3.value(0)
        in4.value(0)
        time.sleep(0.005)
        
        in1.value(0)
        in2.value(1)
        in3.value(0)
        in4.value(0)
        time.sleep(0.005)
        
        in1.value(0)
        in2.value(0)
        in3.value(1)
        in4.value(0)
        time.sleep(0.005)
        
        in1.value(0)
        in2.value(0)
        in3.value(0)
        in4.value(1)
        time.sleep(0.005)
    
    for i in range(steps):
        in1.value(0)
        in2.value(0)
        in3.value(0)
        in4.value(1)
        time.sleep(0.005)
        
        in1.value(0)
        in2.value(0)
        in3.value(1)
        in4.value(0)
        time.sleep(0.005)
        
        in1.value(0)
        in2.value(1)
        in3.value(0)
        in4.value(0)
        time.sleep(0.005)
        
        in1.value(1)
        in2.value(0)
        in3.value(0)
        in4.value(0)
        time.sleep(0.005)







OR 








from machine import Pin
import time

in1 = Pin(5, Pin.OUT)
in2 = Pin(12, Pin.OUT)
in3 = Pin(25, Pin.OUT)
in4 = Pin(19, Pin.OUT)

cw_steps = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

#acw_steps = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

steps = 500  

while True:
    for i in range(steps):
        for s in cw_steps:
            in1.value(s[0])
            in2.value(s[1])
            in3.value(s[2])
            in4.value(s[3])
            time.sleep(0.005)

    time.sleep(0.005)

    for i in range(steps):
        for s in cw_steps:
            in1.value(s[3])
            in2.value(s[2])
            in3.value(s[1])
            in4.value(s[0])
            time.sleep(0.005)

    time.sleep(0.005)
