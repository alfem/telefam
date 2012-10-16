
import pygame
import os
import urllib2

class storage:
    '''
    Abstraction for user persistance
    '''
    def __init__(self,data_path):
        self.data_path=data_path

    def get(self, user_id):
        filename=os.path.join(self.data_path, user_id+".jpg")
        photo=pygame.image.load(filename)

        filename=os.path.join(self.data_path, user_id+".txt")
        f = open(filename, 'r')
        content=f.readlines()
        f.close()

        name=content.pop(0).rstrip()
        return User(user_id, name, photo)

    def store(self, user):
        filename=os.path.join(self.data_path, user.id+".txt")
        if os.path.exists(filename):
            return False
        f = open(filename, 'w')
        f.write(user.name+"\n")
        f.close()
        return True

    def update_photo(self, userid, filename):
        user_filename=os.path.join(self.data_path, userid+".jpg")
        os.rename(filename, user_filename)

        return True
        

class User:
    '''
    An user with photo and properties (name)
    '''
    def __init__(self, id, name, photo):
        self.id=id
        self.name=name
        self.photo=photo
        

