#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 23/Jun/2012

import pygame
from pygame.locals import *
import Voice
import Sound


class Interface:
    '''
    Screen graphics and other media are embedded in this class
    '''
    def __init__(self,CONF):
        self.width=int(CONF["width"])
        self.height=int(CONF["height"])
        self.centerx=self.width/2
        self.centery=self.height/2
        
# Pygame modules initialization. Avoid general initialization because in some hardware you have no sound'
        pygame.font.init()
        pygame.display.init()
        
        if CONF["full_screen"] == "True":
            self.screen=pygame.display.set_mode((self.width,self.height),pygame.FULLSCREEN)
        else:
            self.screen=pygame.display.set_mode((self.width,self.height))

        self.font_big = pygame.font.Font(CONF["font_name"], int(CONF["font_size_big"]) )
        self.font = pygame.font.Font(CONF["font_name"], int(CONF["font_size"]) )
        self.font_small = pygame.font.Font(CONF["font_name"], int(CONF["font_size_small"]) )
        self.back_color=pygame.color.Color(CONF["back_color"])
        self.front_color_active=pygame.color.Color(CONF["front_color_active"])
        self.front_color=pygame.color.Color(CONF["front_color"])
        self.decoration_color=pygame.color.Color(CONF["decoration_color"])
        self.decoration_color_active=pygame.color.Color(CONF["decoration_color_active"])
        self.font_color=pygame.color.Color(CONF["font_color"])

        pygame.mouse.set_visible(0)

    def clean(self):
        self.screen.fill(self.back_color)
        pygame.display.flip()

    def draw_box(self,coords,active):
        rectangle=pygame.Rect(coords)
        if active:
            self.screen.fill(self.decoration_color_active,rectangle)
            rectangle.inflate_ip(-15, -15)
            self.screen.fill(self.front_color_active,rectangle)
        else:
            self.screen.fill(self.decoration_color,rectangle)
            rectangle.inflate_ip(-15, -15)
            self.screen.fill(self.front_color,rectangle)

    def load_menu_icons(self,modules):
        icons={}
        for module in modules["active"]:
            icons[module]=pygame.image.load("icons/"+modules[module]["icon"])
        return icons
        
    def show_main_menu(self,modules,option):
        icons=self.load_menu_icons(modules)

        text = self.font_small.render("TeleFam", 1, self.font_color)
        self.screen.blit(text, (1,1))

        module=modules['active'][option]
        title=modules[module]["title"]
        icon=icons[module]
        description=modules[module]["description"]

        self.draw_box((self.centerx-250,self.centery-250,500,500),True)
        self.screen.blit(icon, (self.centerx-250,self.centery-250))
        text = self.font_big.render(title, 1, self.font_color)
        width,height=text.get_size()
        x=self.centerx-width/2
        self.screen.blit(text, (x, self.centery-300))
        text = self.font.render(description, 1, self.font_color)
        width,height=text.get_size()
        x=self.centerx-width/2
        self.screen.blit(text, (x, self.centery+300))

        pygame.display.flip()



