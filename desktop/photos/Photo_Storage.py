
import os
import time
import pygame
import User_Storage

class storage:
    '''
    Abstraction for message persistance
    '''
    def __init__(self,data_path, user_storage):
        self.data_path=data_path
        self.user_storage=user_storage

    def list_galleries(self):
        dir_list=os.listdir(os.path.join(self.data_path))
        return dir_list
    
    def get_gallery(self,gallery):
        filename=os.path.join(self.data_path , gallery, "info")
        f = open(filename, 'r')
        content=f.readlines()
        f.close()
        timestamp=time.strptime(content.pop(0).rstrip() ,"%Y/%m/%d %H:%M:%S")
        username=content.pop(0).rstrip()
        user=self.user_storage.get(username)
        description=content.pop(0).rstrip()        

        filename=os.path.join(self.data_path, gallery, "thumbnail.jpg")
        cover=pygame.image.load(filename)
        return Gallery(timestamp,user,description,cover)

        
    def list_photos(self, gallery):
        dir_list=os.listdir(os.path.join(self.data_path,gallery))
        dir_list.remove("info")
        dir_list.remove("thumbnail.jpg")
        return dir_list

    def get_photo(self,gallery, name):
        filename=os.path.join(self.data_path ,gallery ,name)
        photo=pygame.image.load(filename)
        return photo

    def delete(self,folder, index):
        filename=os.path.join(self.data_path , folder ,index)
        if os.path.exists(filename):
             os.remove(filename)
        return 

class Gallery:
    '''
    A collection of photos with some metadata
    '''
    def __init__(self,timestamp,user,description,cover):
        self.timestamp=timestamp
        self.user=user
        self.description=description
        self.cover=cover
        self.thumbnail=pygame.transform.scale(cover,(200,200))
 
