
import os

class message:
    '''
    A simple short message
    '''
    def __init__(self,data_path):

        self.data_path=data_path
        self.date=""
        self.time=""
        self.user=""
        self.text=""
        
    def list(self, type):
        dir_list=os.listdir(os.path.join(self.data_path,type))
        for fname in dir_list:
            print fname

    
    def load(self,):
        return
    def set_read(self):
        return
