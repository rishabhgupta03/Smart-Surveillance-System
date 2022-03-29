from boltiot import Bolt
import time
api_key = "c01360ae-cfe4-4f1a-9931-5c614c5399ec"
device_id  = "BOLT7420942"
mybolt = Bolt(api_key, device_id)

check_device=mybolt.isOnline()
check_device=check_device.split(",")[0].split(":")[1]
def alarm():
    for x in range(5):
        mybolt.digitalWrite('0','HIGH')
        time.sleep(0.1)
        mybolt.digitalWrite('0','LOW')