from machine import Pin
import time

IN1 = Pin(5, Pin.OUT)
IN2 = Pin(12, Pin.OUT)
IN3 = Pin(25, Pin.OUT)
jIN4 = Pin(19, Pin.OUT)

#list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
x = 0.005

while True:
    IN1.on()
    time.sleep(x)
    IN2.on()
    time.sleep(x)
    IN3.off()
    time.sleep(x)
    IN4.off()
    time.sleep(x)
    
    IN1.off()
    time.sleep(x)
    IN2.on()
    time.sleep(x)
    IN3.off()
    time.sleep(x)
    IN4.off()
    time.sleep(x)
    
    IN1.off()
    time.sleep(x)
    IN2.on()
    time.sleep(x)
    IN3.on()
    time.sleep(x)
    IN4.on()
    time.sleep(x)
    
    IN1.off()
    time.sleep(x)
    IN2.off()
    time.sleep(x)
    IN3.on()
    time.sleep(x)
    IN4.off()
    time.sleep(x)
    IN4.off()
    time.sleep(x)
    
    IN1.off()
    time.sleep(x)
    IN2.off()
    time.sleep(x)
    IN3.on()
    time.sleep(x)
    IN4.on()
    time.sleep(x)
   
    IN1.off()
    time.sleep(x)
    IN2.off()
    time.sleep(x)
    IN3.off()
    time.sleep(x)
    IN4.on()
    time.sleep(x)
    
    IN1.on()
    time.sleep(x)
    IN2.off()
    time.sleep(x)
    IN3.off()
    time.sleep(x)
    IN4.on()
    time.sleep(x)
    
    IN1.on()
    time.sleep(x)
    IN2.off()
    time.sleep(x)
    IN3.off()
    time.sleep(x)
    IN4.off()
    time.sleep(x)
    IN1.off()
    time.sleep(x)
    
    

    
    

    
    



