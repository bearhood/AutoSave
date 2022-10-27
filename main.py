import os
from os import path
import pylnk3
import time
import sys



#Create a path into "recent" folder
path_recent = path.expandvars(r'%APPDATA%\Microsoft\Windows\Recent')

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
class FileLnk(object):
    def __init__(self , lnk_obj = None , path = None):
        # path is pointed to the path of the file !!!!
        if( lnk_obj ):
            self.lnk_obj = lnk_obj
        if( path ):
            self.path = path
        self.file_name = None
        self.file_type = None
        self.edit_time_last = None
        self.set_file_info( path )
        
    def set_file_info(self,path):
        self.file_name = str( os.path.basename( path ) )
        self.file_type = str( os.path.splitext( path )[-1] )
        self.edit_time_last = self.lnk_obj.modification_time
        pass
    def get_file_path(self):
        pass
    def get_info(self):
        print( self.__dict__ )
        return self.__dict__


obj_lnk_list_0 = {}
for lnk_name in os.listdir( path_recent):
    try:
        lnk_filepath = os.path.join( path_recent , lnk_name )
        with HiddenPrints():
            lnk_obj = pylnk3.parse( lnk_filepath )
        file_path = os.path.join( lnk_obj._work_dir , os.path.basename( lnk_obj.path ) )
    except: 
        continue
    obj_lnk_list_0[ file_path ] = FileLnk( lnk_obj, file_path ) 
    del lnk_obj




for counts in range( 100 ):
    time.sleep( 1 )
    print( 'now its {} round '.format( counts) )
    obj_lnk_list_1 = {}
    exist_file = obj_lnk_list_0.keys()
    # receive current data
    for lnk_name in os.listdir( path_recent):
        try:
            
            lnk_filepath = os.path.join( path_recent , lnk_name )
            with HiddenPrints():
                lnk_obj = pylnk3.parse( lnk_filepath )
            file_path = os.path.join( lnk_obj._work_dir , os.path.basename( lnk_obj.path ) )
            if( file_path in exist_file ):
                if( lnk_obj.modification_time == obj_lnk_list_0[file_path].edit_time_last):
                    obj_lnk_list_1[ file_path ] = obj_lnk_list_0[file_path]
                else:
                    #更新檔案
                    print( file_path )
                    print(lnk_obj.modification_time)
                    print( (lnk_obj.modification_time-obj_lnk_list_0[file_path].edit_time_last).total_seconds()  )

                    obj_lnk_list_1[ file_path ] = FileLnk( lnk_obj , file_path ) 

                    pass
            else:
                obj_lnk_list_1[ file_path ] = FileLnk( lnk_obj , file_path ) 
            del lnk_obj
        except: 

            continue
    obj_lnk_list_0 = obj_lnk_list_1    
        


#print( obj_lnk_list_0.keys() )

#complete while(1):





''' Garbage zone
# %APPDATA%/Microsoft/Windows/Recent
#
# os.path.join(basepath, fname)

os.path.basename(obj.path) 輸出末端的檔案
 os.path.splitext(obj.path) ) ) 分離 檔案類型

 #timee = obj_lnk_list_0['C:\\Users\\Hebearo\\Downloads\\hw2.pdf'].edit_time_last
'''
