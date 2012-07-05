#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 23/Jun/2012

import pygame
from pygame.locals import *

class Controller:
    '''
    Screen graphics and other media are embedded in this class
    '''
    def __init__(self,CONF):
      return
      
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


