import time
from machine import Pin

led_green = Pin("LED", Pin.OUT)
led_green.off()

time_led = 203
count = 0

while(True):
    count = count + 1
    print("Pi Pico W: " +str(count))
    time.sleep_ms(time_led)
    led_green.on()
    time.sleep_ms(time_led)
    led_green.off()