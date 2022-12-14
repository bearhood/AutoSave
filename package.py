import os
from os import path
import pylnk3
import time
import sys
import struct
import shutil
from __main__ import *

path_recent = path.expandvars(r'%APPDATA%\Microsoft\Windows\Recent')
#Create a path into "recent" folder

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
class FileLnk_dict(object):
    def __init__(self,data_type = {'type':{'0':'repl'},
                                   'name':[ ]   } ):
        '''The variable tells which to backup'''
        global saving_dir
        self.data_type = data_type
        self.deled = []
        self.obj_lnk_list_0 = {}
        self.exception_list = ["AutomaticDestinations" ,
                  "CustomDestinations",] 
        self.create_dict()
    def set_backup_of_file(self,FileLnk='ww'):
        path = FileLnk.file_path
        if( FileLnk.saving_format == 'hist'):
            target_path = ( saving_dir+
                    FileLnk.file_name.split('.')[0]+
                    '/backed_by'+ 
                    str(FileLnk.edit_time_last).replace(':','_').replace(' ','_')+
                    '__'+
                    FileLnk.file_name)
        elif( FileLnk.saving_format=='repl'):
            target_path = ( saving_dir+
                    FileLnk.file_name.split('.')[0]+
                    '/backed_'+
                    FileLnk.file_name)     
        info_path = (os.path.dirname(target_path) +
                '/info_'+FileLnk.file_name.split('.')[0]+'.txt')
        try:
            shutil.copyfile(path, target_path)
            with open(info_path, 'a+',
                        encoding='utf-8-sig') as data:
                data.write('\n'+str(FileLnk.edit_time_last)+'\n')
        except IOError as io_err:
            os.makedirs(os.path.dirname(target_path))
            shutil.copyfile(path, target_path)
            with open(info_path, 'w',
                        encoding='utf-8-sig') as data:
                data.write(path+'\n')
                data.write(str(FileLnk.edit_time_last))
        pass
    def update_about_time(self):
        """This function will determine when did the file
         last edited"""
        for path in self.obj_lnk_list_0.keys():
            suc = self.obj_lnk_list_0[path].check_time()
            if( suc==1 ):
                self.set_backup_of_file( self.obj_lnk_list_0[path]
                                        , )
            elif(suc==-1):
                self.deled.append(path)
        for path in self.deled:
            del self.obj_lnk_list_0[path]
        self.deled = []

    def create_dict(self):
        for lnk_name in os.listdir( path_recent):
            if( lnk_name not in self.exception_list
                and 
                lnk_name.split('.')[-1] == 'lnk' ):
                temp = FileLnk( lnk_name ) 
                if( temp == None):
                    print( 'nono')
                elif(temp.file_type in list(self.data_type['type'].keys())):
                    temp.set_saving_format(self.data_type['type'][ temp.file_type])  
                    self.obj_lnk_list_0[ temp.file_path ] = temp
                elif(temp.file_name in list(self.data_type['name'].keys()) ):
                    temp.set_saving_format(self.data_type['name'][ temp.file_name])  
                    self.obj_lnk_list_0[ temp.file_path ] = temp
                else:
                    pass
        pass


class FileLnk(object):
    def __init__(self , lnk_name ):
        # path is pointed to the path of the file !!!!
        # lnk_name ???????????? recent
        #lnk object will locked the choice of file_...
        self.lnk_name = lnk_name
        self.lnk_obj = None
        self.file_path = None
        self.file_name = None
        self.file_type = None
        self.edit_time_last = None
        self.lnk_file_path =None
        self.saving_format = None
        suc = self.set_lnkobj( self.lnk_name )
        if( suc == 0 ):
            return None
        suc = self.set_file_path()
        if( suc == 0 ):
            # ???????????????
            return None
        suc = self.set_file_info()
        if( suc == 0 ):
            # ???????????????
            return None
        #self.check_if_file_exist( )
    def set_saving_format(self,text):
        self.saving_format = text
    def set_file_path( self ):
        try:
            self.file_path = os.path.join( self.lnk_obj._work_dir , os.path.basename( self.lnk_obj.path ) )
            if( saving_dir.replace('\\','/') in
             self.lnk_obj._work_dir.replace('\\','/')        ):
                raise TypeError
            return 1
        except TypeError:
            # if the file is not exist anymore
            return 0
        pass     
    def remove_lnk( self ):
        # ???????????????recent????????????
        os.remove( self.lnk_file_path  ) 
    def set_lnkobj(self, lnk_file_name):

        with HiddenPrints():
            try:
                self.lnk_file_path = os.path.join( path_recent , lnk_file_name )
                self.lnk_obj = pylnk3.parse( self.lnk_file_path )
            except :
                return 0
        pass

    def set_file_info(self):
        '''
        #info including:
        file name
        file type
        last edit time
        '''
        path = self.file_path
        try:
            self.file_name = str( os.path.basename( path ) )
            self.file_type = str( os.path.splitext( path )[-1] )
            self.edit_time_last = time.ctime( os.path.getmtime(  self.file_path ) )
            
            return 1
        except:
            return 0
        pass
    def get_file_path(self):
        pass
    def get_info(self):
        return self.__dict__
    def check_time(self):
        try:
            temp_time = time.ctime( os.path.getmtime(  self.file_path ) )
            if( temp_time != self.edit_time_last ):
                print(self.file_path)
                print( self.edit_time_last )
                print(temp_time)
                self.edit_time_last = temp_time
                return 1 # if it's edited
            else:
                return 0
        except :
            return -1
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
                # ??????????????????
                obj_lnk_list_1[ file_path ] = FileLnk( lnk_obj , file_path)
                if( obj_lnk_list_1[ file_path ].edit_time_last == obj_lnk_list_0[file_path].edit_time_last):
                    pass
                else:
                    #????????????
                    
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

os.path.basename(obj.path) ?????????????????????
 os.path.splitext(obj.path) ) ) ?????? ????????????

 #timee = obj_lnk_list_0['C:\\Users\\Hebearo\\Downloads\\hw2.pdf'].edit_time_last
'''
