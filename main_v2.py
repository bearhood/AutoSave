from package import FileLnk, HiddenPrints
import os

path_recent = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Recent')
obj_lnk_list_0 = {}
exception_list = ["AutomaticDestinations" ,
                  "CustomDestinations",
]
# 完成迴圈校正


for lnk_name in os.listdir( path_recent):
    print(lnk_name)
    if( lnk_name not in exception_list
        and 
        lnk_name.split('.')[-1] == 'lnk' ):
        temp = FileLnk( lnk_name ) 
        if( temp == None):
            print( 'nono')
        else:   
            obj_lnk_list_0[ temp.file_path ] = temp


print( obj_lnk_list_0 )

##
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