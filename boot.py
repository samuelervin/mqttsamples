import gc
import network
import esp


esp.osdebug(None)
gc.collect()

ssid = 'xxxxxxxxx'
password = 'xxxxxxxxxxxx'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass    

print('Connection successful')
print(station.ifconfig())
