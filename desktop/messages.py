#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam messages module
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 10/Jul/2012

from configobj import ConfigObj
import Gui
import Controls

# Main
def main():
    print "Module messages"
# Load main config file
    CONF = ConfigObj("telefam.conf")

# Load module specific config files
    for module in CONF["MODULES"]["active"]:
        CONF["MODULES"][module]=ConfigObj(module+".conf")
     
# Create a Graphic User Interface
    interface = Gui.Interface(CONF["INTERFACE"])

# Create a Controller (keyboard, joystick..)
    controller= Controls.Control(CONF["CONTROL"])

# Main loop
    option=0
    while True:
      interface.clean()
      key=controller.wait_for_user()
      if key == "LEFT" and option > 0: 
        option -=1
      if key == "RIGHT" and option < len(CONF["MODULES"]["active"]) - 1: 
        option +=1
      if key == "OK": 
        return

if __name__ == '__main__':
  main()
  