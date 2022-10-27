import os
from os import path
import pylnk3

#Create a path into "recent" folder
path_recent = path.expandvars(r'%APPDATA%\Microsoft\Windows\Recent')

file_lnk = os.path.join( path_recent , '簡報1.lnk' )
obj = pylnk3.parse( file_lnk )
print( file_lnk )
print( str( os.path.basename(obj.path) ) );
#print( )
