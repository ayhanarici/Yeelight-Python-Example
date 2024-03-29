#This example shows how to create a bulb and make its basic settings.
import yeelight
import time
from yeelight.main import Bulb, discover_bulbs

bulb = Bulb('192.168.1.100', effect="smooth")
#The sample code below will create a new lamp and turn it on.
#After 2 seconds, the lamp will be turned off.
bulb.turn_on()
time.sleep(5)
bulb.turn_off()

#Toggle the bulb's power
time.sleep(5)
bulb.toggle()

#Adjusting the bulb brightness
bulb.set_brightness(100)
for i in range(100,0,-20):
    bulb.set_brightness(i)
    time.sleep(5)
