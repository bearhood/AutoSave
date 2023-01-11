
#saving_dir = './backup_folder/'
saving_dir = 'C:/Users/Hebearo/OneDrive/backup/'
data_type = {
    'type':{'.pptx':'repl',
            '.png':'hist' ,
            '.db':'hist'},
    'name':{'null':'repl'},
    'path':{'null':'repl'}
    
}
time_itv = 3

'''
example:
data_type = {
    'type':{'.pptx':'repl',
            '.png':'hist'},
    'name':{'null':'repl'},
    'path':{'null':'repl'}}


'hist' is to save every time saving: ex.small item
'repl' is just replace the already backup one ex.large item
'''