
import pygame
import os

class storage:
    '''
    Abstraction for user persistance
    '''
    def __init__(self,data_path):
        self.data_path=data_path

    def get(self, username):
        filename=os.path.join(self.data_path, username+".jpg")
        photo=pygame.image.load(filename)

        filename=os.path.join(self.data_path, username+".txt")
        f = open(filename, 'r')
        content=f.readlines()
        f.close()

        name=content.pop(0).rstrip()
        relation=content.pop(0).rstrip()
        return User(photo, name, relation)

    def create(self, user):
        filename=os.path.join(self.data_path, username+".txt")
        if os.path.exists(filename):
            return "ERROR"
        f = open(filename, 'w')
        f.write(user.name+"\n")
        f.write(user.relation+"\n")
        f.close()
        return
        

class User:
    '''
    An user with photo and properties (name)
    '''
    def __init__(self, photo, name, relation):
        self.photo=photo
        self.name=name
        self.relation=relation
        

