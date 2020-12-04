import machine
from time import sleep
p4 = machine.Pin(4)
servo = machine.PWM(p4,freq=50)
# duty for servo is between 40 - 115
servo.duty(100)
while(1):
  servo.duty(50)
  sleep(2)
  servo.duty(100)
  sleep(2)
  
