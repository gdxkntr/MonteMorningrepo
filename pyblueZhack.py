#this script that advertises a bluetooth low energy beacon for 15 seconds

import time #<--- first part class module

from bluetooth.ble import BeaconService #<----3rd part module

#create isntantiation of object from 3rd party module

service = BeaconService()

#calls beacons service function.starts advertising("UID"), parameters in which you recieve UID
service.start_advertising ("11111111-2222-3333-4444-555555555555",1, 1,1,200)#<-- TCP,UDP. port/channel
#                                                                port,port,chanel,range?
#advertising stops every 15 seconds
time.sleep(15)
#stops advertising
service.stop_advertising()
#prints "done."
print("Done.")