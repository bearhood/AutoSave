from package import FileLnk, HiddenPrints,FileLnk_dict
import os
import time

obj =  FileLnk_dict()
for i in range(10000):
    time.sleep(1)
    obj.update_about_time()
    print(i)
    pass


