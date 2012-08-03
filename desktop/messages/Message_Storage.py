
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

    def list(self, folder):
        dir_list=os.listdir(os.path.join(self.data_path,folder))
        return dir_list

    def get(self,folder, index):
        filename=os.path.join(self.data_path , folder ,index)
        f = open(filename, 'r')
        content=f.readlines()
        f.close()

        timestamp=time.strptime(content.pop(0).rstrip() ,"%Y/%m/%d %H:%M:%S")
        username=content.pop(0).rstrip()
        user=self.user_storage.get(username)
        
        return Message(timestamp, user, content)

    def delete(self,folder, index):
        filename=os.path.join(self.data_path , folder ,index)
        if os.path.exists(filename):
             os.remove(filename)
        return 

class Message:
    '''
    A simple short message
    '''
    def __init__(self,timestamp,user,text):
        self.timestamp=timestamp
        self.user=user
        self.text=text
        
    def set_read(self):
        return
