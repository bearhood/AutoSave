"""
The version has been already abandomed for it's saved for all class into a new python file package.py

Now Let's moveto main_v2
"""



import os
from os import path
import pylnk3
import time
import sys

#Create a path into "recent" folder
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
class FileLnk(object):
    def __init__(self , lnk_name ):
        # path is pointed to the path of the file !!!!
        self.lnk_name = lnk_name
        self.lnk_obj = None
        self.file_path = None
        self.file_name = None
        self.file_type = None
        self.edit_time_last = None
        self.set_path_and_lnkobj
    def set_default( self ):
        self.set_path_and_lnkobj()
        self.set_file_info( self.path )
    def check_if_exist( self ):
        return os.path.exists('readme.txt')
    def set_path_and_lnkobj( self ):
        try:
            lnk_filepath = os.path.join( path_recent , lnk_name )
            with HiddenPrints():
                lnk_obj = pylnk3.parse( lnk_filepath )
            self.file_path = os.path.join( lnk_obj._work_dir , os.path.basename( lnk_obj.path ) )
        except: 
            pass
            
    def set_file_info(self,path):
        try:
            self.file_name = str( os.path.basename( path ) )
            self.file_type = str( os.path.splitext( path )[-1] )
            self.edit_time_last = time.ctime( os.path.getmtime(  self.path ) )
            return 1
        except FileNotFoundError:
            return 0
        pass
    def get_file_path(self):
        pass
    def get_info(self):
        print( self.__dict__ )
        return self.__dict__


obj_lnk_list_0 = {}
for lnk_name in os.listdir( path_recent):


    obj_lnk_list_0[ file_path ] = FileLnk( lnk_obj, file_path ) 
    del lnk_obj



'''
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
                # 若檔案以存在
                obj_lnk_list_1[ file_path ] = FileLnk( lnk_obj , file_path)
                if( obj_lnk_list_1[ file_path ].edit_time_last == obj_lnk_list_0[file_path].edit_time_last):
                    pass
                else:
                    #更新檔案
                    
                    print( file_path )
                    print(lnk_obj.modification_time)
                    print( (obj_lnk_list_1[ file_path ].edit_time_last -
                            obj_lnk_list_0[file_path].edit_time_last).total_seconds()  )

                    obj_lnk_list_1[ file_path ] = FileLnk( lnk_obj , file_path ) 

                    pass
            else:
                obj_lnk_list_1[ file_path ] = FileLnk( lnk_obj , file_path ) 
            del lnk_obj
        except: 

            continue
    obj_lnk_list_0 = obj_lnk_list_1    
'''        


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
