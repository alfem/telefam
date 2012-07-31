#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 23/Jun/2012

import pygame
from pygame.locals import *
import time
import Voice
import Sound


class Interface:
    '''
    Screen graphics and other media are embedded in this class
    '''
    def __init__(self,CONF):

        self.CONF=CONF
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
        self.font_color_active=pygame.color.Color(CONF["font_color_active"])

        pygame.mouse.set_visible(0)

# Clear the screen
    def clean(self):
        self.screen.fill(self.back_color)
        pygame.display.flip()

# Draw a box with a frame
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
            icons[module]=pygame.image.load(self.CONF["icons_path"]+modules[module]["icon"])
        return icons
        
        
# Show a big icons main menu
    def show_main_menu(self,modules,option):
        icons=self.load_menu_icons(modules)

        text = self.font_small.render("TeleFam", 1, self.font_color)
        self.screen.blit(text, (1,1))

        module=modules['active'][option]
        title=modules[module]["title"]
        icon=icons[module]
        description=modules[module]["description"]

# Draw a box
        self.draw_box((self.centerx-250,self.centery-250,500,500), True)
# Paint module icon
        self.screen.blit(icon, (self.centerx-200,self.centery-200))
# Write module title
        text = self.font_big.render(title, 1, self.font_color)
        width,height=text.get_size()
        x=self.centerx-width/2
        self.screen.blit(text, (x, self.centery-250))
# Write module description
        text = self.font.render(description, 1, self.font_color)
        width,height=text.get_size()
        x=self.centerx-width/2
        self.screen.blit(text, (x, self.centery+190))
        pygame.display.flip()


# Draw a box with text wrapped
    def draw_textbox(self, surf, rect, font, color, text, maxlines=None):

      r,c,txt = rect,color,text
      tmp = font.render(" ", 1, c)
      sw,sh = tmp.get_size()
      y = r.top
      row = 1
      done = False
      for sentence in txt.split("\n"):
        usentence=sentence.decode("utf-8")
        x = r.left
        words = usentence.split(" ")
            
        for word in words:
            word += " "
            tmp = font.render(word, 1, c)
            (iw, ih) = tmp.get_size()
            if (x+iw > r.right):
                x = r.left
                y += sh
                row += 1
                if (maxlines != None and row > maxlines):
                    done = True
                    break
            surf.blit(tmp, (x, y))
            #x += iw+sw
            x += iw
        if done:
            break
        y += sh
        row += 1
        if (maxlines != None and row > maxlines):
            break

# Show a text menu in a box
    def show_actions_menu(self, CONTROLLER, actions, active):
        margin=20
        maxwidth=0
        menu=pygame.Surface((800,600))
        menu.fill((255,0,255))
        menu.set_colorkey((255,0,255))

        while True:
            maxheight=0
            option=0
            for action in actions:
                if option == active:
                  text=self.font.render(action,1,self.font_color_active)
                else:
                  text=self.font.render(action,1,self.font_color)
                menu.blit(text, (0, maxheight))
                w,h=text.get_size()
                if w> maxwidth:
                    maxwidth=w
                maxheight += h
                option += 1
                
            self.draw_box((self.centerx- maxwidth/2 -margin, self.centery - maxheight/2 -margin, maxwidth+2*margin,maxheight+2*margin),True)
            self.screen.blit(menu, (self.centerx - maxwidth/2 , self.centery - maxheight/2), (0 ,0 ,maxwidth,maxheight))
            pygame.display.flip()    

            action=CONTROLLER.wait_for_user_action()
            if action == "UP" and active > 0: 
              active -=1
            if action == "DOWN" and active < len(actions) - 1: 
              active +=1
            if action == "OK": 
              return active

# MESSAGES (FIX)
# Show message page
    def show_message(self,message):

        left_margin=self.centerx-400
        y=50

        self.draw_box((left_margin,y,800,200), False)

        y=y+10
        text=self.font.render(time.strftime("%d/%m/%Y %H:%M", message.timestamp),1,self.font_color)
        self.screen.blit(text, (left_margin+10, y))

        self.screen.blit(message.user.photo, (left_margin+480, y))

        w,h=text.get_size()
        y=y+h
        text = self.font.render(message.user.name+":", 1, self.font_color)
        self.screen.blit(text, (left_margin+10, y))

        text="\n".join(message.text)
        y=y+300
        self.draw_textbox(self.screen,pygame.Rect(left_margin+10,y ,780,150),self.font,self.font_color, text, 6) 
        
        pygame.display.flip()    
        return


    def show_warning(self,warning):
        left_margin=self.centerx-400
        y=50
        self.draw_box((left_margin,y,800,200), False)

        y=y+10
        self.draw_textbox(self.screen,pygame.Rect(left_margin+10,y ,780,150),self.font,self.font_color, warning, 6) 

        pygame.display.flip()    
        return

