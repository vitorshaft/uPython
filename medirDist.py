import machine
from hcsr04 import HCSR04

sensor = HCSR04(tp = 8, ep = 7)
dist = sensor.distance_cm()
print('Distancia: ',dist, 'cm')
