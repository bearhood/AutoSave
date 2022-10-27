import os
from os import path
import pylnk3

#Create a path into "recent" folder
path_recent = path.expandvars(r'%APPDATA%\Microsoft\Windows\Recent')

class FileLnk(object):
    def __init__(self , lnk_obj = None , path = None):
        # path is pointed to the path of the file !!!!
        if( lnk_obj ):
            self.lnk_obj = lnk_obj
        if( path ):
            self.path = path
        self.file_name = None
        self.file_type = None
        self.set_file_info( path )
    def set_file_info(self,path):
        self.file_name = str( os.path.basename( path ) )
        self.file_type = str( os.path.splitext( path )[-1] )
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
        lnk_obj = pylnk3.parse( lnk_filepath )
        file_path = os.path.join( lnk_obj._work_dir , os.path.basename( lnk_obj.path ) )
    except: 
        continue
    obj_lnk_list_0[ file_path ] = FileLnk(lnk_obj, file_path ) 
print( obj_lnk_list_0.keys() )

#file = pylnk3.open( filename )


#complete while(1):





''' Garbage zone
# %APPDATA%/Microsoft/Windows/Recent
#
# os.path.join(basepath, fname)

os.path.basename(obj.path) 輸出末端的檔案
 os.path.splitext(obj.path) ) ) 分離 檔案類型
'''
