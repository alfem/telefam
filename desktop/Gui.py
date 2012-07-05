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
       
# Pygame modules initialization. Avoid general initialization because in some hardware you have no sound'
        pygame.font.init()
        pygame.display.init()
        
        if CONF["full_screen"] == "True":
            self.screen=pygame.display.set_mode((self.width,self.height),pygame.FULLSCREEN)
        else:
            self.screen=pygame.display.set_mode((self.width,self.height))
            
        self.font = pygame.font.Font(CONF["font_name"], int(CONF["font_size"]) )
        self.back_color=pygame.color.Color(CONF["back_color"])
        self.front_color=pygame.color.Color(CONF["front_color"])
        self.font_color=pygame.color.Color(CONF["font_color"])

        pygame.mouse.set_visible(0)
        self.screen.fill(self.back_color)

        text = self.font.render("TeleFam", 1, self.font_color)
        width,height=text.get_size()
        x=self.width/2-width/2
        self.screen.blit(text, (x,10))
        pygame.display.flip()
        
        pygame.time.delay(3000)
         
