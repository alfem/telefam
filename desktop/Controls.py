#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 23/Jun/2012

import pygame
from pygame.locals import *
import sys

class Control:
    '''
    User interaction class. Simple actions for up, down, left, right and ok can be activated with joystick, keyboard or any other device.
    '''
    def __init__(self,CONF):
      return
      
    def wait_for_user_action(self):
      while True:
        for event in pygame.event.get() :
# KEYBOARD
          if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE:
              sys.exit(0)
            if event.key == pygame.K_SPACE :
              return "OK"
            if event.key == pygame.K_UP :
              return "UP"
            if event.key == pygame.K_DOWN :
              return "DOWN"
            if event.key == pygame.K_RIGHT:
              return "RIGHT"
            if event.key == pygame.K_LEFT :
              return "LEFT"


