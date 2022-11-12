from package import FileLnk, HiddenPrints,FileLnk_dict
import os
import time

data_type = ['.pptx',
            '.png']
obj =  FileLnk_dict( data_type= data_type)
for i in range(5):
    time.sleep(1)
    obj.update_about_time()
    print(i)
    pass


print(obj.obj_lnk_list_0)