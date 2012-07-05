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

        self.font_big = pygame.font.Font(CONF["font_name"], int(CONF["font_size_big"]) )
        self.font = pygame.font.Font(CONF["font_name"], int(CONF["font_size"]) )
        self.font_small = pygame.font.Font(CONF["font_name"], int(CONF["font_size_small"]) )
        self.back_color=pygame.color.Color(CONF["back_color"])
        self.front_color_active=pygame.color.Color(CONF["front_color_active"])
        self.front_color=pygame.color.Color(CONF["front_color"])
        self.font_color=pygame.color.Color(CONF["font_color"])

        pygame.mouse.set_visible(0)

    def clean(self):
        self.screen.fill(self.back_color)
        pygame.display.flip()

    def draw_box(self,rectangle,active):
        if active:
            pygame.draw.rect(self.screen, self.front_color_active, rectangle, 0)
        else:
            pygame.draw.rect(self.screen, self.front_color, rectangle, 0)


    def show_main_menu(self):
        text = self.font_big.render("TeleFam", 1, self.font_color)
        width,height=text.get_size()
        x=self.width/2-width/2
        self.draw_box((x,10,width,height),False)
        self.draw_box((x,100,width,height),True)
        pygame.draw.rect(self.screen, self.front_color, (x,10,width,height), 0)
        self.screen.blit(text, (x,10))
        pygame.display.flip()
        
#        pygame.time.delay(3000)

    def wait_for_user(self):
      while True:
        for event in pygame.event.get() :
          if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE:
              sys.exit(0)
            if event.key == pygame.K_SPACE :
              return "OK"
            if event.key == pygame.K_UP :
              return "UP"
            if event.key == pygame.K_DOWN :
              return "DOWN"
            if event.key == pygame.K_UP :
              return "UP"
            if event.key == pygame.K_DOWN :
              return "DOWN"
            if event.key == pygame.K_RIGH :
              return "RIGHT"
            if event.key == pygame.K_LEFT :
              return "LEFT"


