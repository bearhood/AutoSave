'''import os
from os import path
import pylnk3
import time
#Create a path into "recent" folder
path_recent = path.expandvars(r'%APPDATA%\Microsoft\Windows\Recent')

file_lnk = os.path.join( path_recent , 'some result.lnk' )
obj = pylnk3.parse( file_lnk )

file_path = os.path.join( obj._work_dir , os.path.basename( obj.path ) )

timming = os.path.getmtime( file_path )
print( timming  )
print( time.ctime( timming ))'''
#print( )
'''
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
testt = 'C:\\Users\\Hebearo\\Downloads\\2021.12.10_2021.12.30_ main chamber 到 FFS 架設.html'
print(obj_lnk_list_0[testt].lnk_obj.__dict__)'''
'''import pylnk3
class lnkk( pylnk3.Lnk):
    def __init__(self, f = None):
        self.link_flags = None
        self.file = None
        if type(f) == str or type(f) == str:
            self.file = f
            try:
                f = open(self.file, 'rb')
            except IOError:
                self.file += ".lnk"
                f = open(self.file, 'rb')
        # defaults

        self.file_size = 0
        self.icon_index = 0
        self.hot_key = None
        self._link_info = None
        self.description = None
        self.relative_path = None
        self.work_dir = None
        self.arguments = None
        self.icon = None
        self.extra_data = None
        
        if f is not None:
            self._parse_lnk_file(f)
        if self.file:
            f.close()
import os
from os import path
import pylnk3
import time
#Create a path into "recent" folder
path_recent = path.expandvars(r'%APPDATA%\Microsoft\Windows\Recent')

file_lnk = os.path.join( path_recent , 'some result.lnk' )
obj = lnkk( file_lnk )

file_path = os.path.join( obj._work_dir , os.path.basename( obj.path ) )

timming = os.path.getmtime( file_path )
'''

from package import FileLnk, HiddenPrints
import os

path_recent = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Recent')
obj_lnk_list_0 = {}

lnkfile0 = 'some result'

a = FileLnk( lnkfile0 ) 

print( a.file_path )