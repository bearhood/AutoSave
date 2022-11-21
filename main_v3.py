
import os
import time
import threading

#data_type is related to whether to record history
#or just replace with the one

'''
'hist' is to save every time saving: ex.small item
'repl' is just replace the already backup one ex.large item
'''

saving_dir = './backup_folder/'
saving_dir = 'C:/Users/Hebearo/OneDrive/backup/'
data_type = {
    'type':{'.pptx':'repl',
            '.png':'hist'},
    'name':{'null':'repl'},
    'path':{'null':'repl'}
    
}
'''
example:
data_type = {
    'type':['.pptx'],
    'name':['筆記 2022年10月19日.pdf']}
    '''
from package import *
try:
    while(1):
        obj =  FileLnk_dict( data_type= data_type )
        for i in range(10):
            time.sleep(1)
            obj.update_about_time()
except KeyboardInterrupt:
    print( 'ending accepted')
    print( 'the end')
    