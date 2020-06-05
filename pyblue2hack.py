#this script that advertises a bluetooth low energy beacon for 15 seconds

import time #<--- first part class module

from bluetooth.ble import BeaconService #<----3rd part module

#create isntantiation of object from 3rd party module

service = BeaconService()

service.start_advertising ("11111111-2222-3333-4444-555555555555",1, 1,1,200)

time.sleep(15)

service.stop_advertising()

print("Done.")