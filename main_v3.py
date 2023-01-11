from coefficient import *
from package import *
import os
import time
import threading

#data_type is related to whether to record history
#or just replace with the one


os.startfile( saving_dir )
print( 'start working in '+ saving_dir)

try:
    while(1):
        obj =  FileLnk_dict( data_type= data_type )
        for i in range(10):
            time.sleep(time_itv)
            obj.update_about_time()
        del obj
except KeyboardInterrupt:
    print( 'ending accepted')
    print( 'the end')
    