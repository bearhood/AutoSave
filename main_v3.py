from package import FileLnk, HiddenPrints,FileLnk_dict
import os
import time
import threading
data_type = ['.pptx']

try:
    while(1):
        obj =  FileLnk_dict( data_type= data_type)
        for i in range(10):
            time.sleep(1)
            obj.update_about_time()
            print(i)
except KeyboardInterrupt:
    print( 'ending accepted')
    print( 'the end')