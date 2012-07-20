
import os
import time
import User_Storage

class storage:
    '''
    Abstraction for message persistance
    '''
    def __init__(self,data_path, user_storage):
        self.data_path=data_path
        self.user_storage=user_storage

    def list(self, queue):
        dir_list=os.listdir(os.path.join(self.data_path,queue))
        return dir_list

    def get(self,queue, index):
        filename=os.path.join(self.data_path, queue,index)
        print "Message:", filename
        f = open(filename, 'r')
        content=f.readlines()
        f.close()

        timestamp=time.strptime(content.pop(0).rstrip() ,"%Y/%m/%d %H:%M:%S")
        username=content.pop(0).rstrip()
        user=self.user_storage.get(username)
        
        return message(timestamp, user, content)

class message:
    '''
    A simple short message
    '''
    def __init__(self,timestamp,user,text):
        self.timestamp=timestamp
        self.user=user
        self.text=text
        
    def set_read(self):
        return
