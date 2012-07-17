#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam messages module
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 10/Jul/2012

import message_base

# Main
def main(CONF, INTERFACE, CONTROLLER):
    module_name=__name__
    print "Module " + module_name

    messages=message_base.message(CONF["MODULES"][module_name]["data_path"])
    new_messages=messages.list("received")

# Main loop
    index=0
    while True:
      INTERFACE.clean()
      INTERFACE.messages.show_list(new_messages)
      action=CONTROLLER.wait_for_user_action()
      if action == "UP" and option > 0: 
        index -=1
      if action == "DOWN": 
        index +=1
      if action == "END": 
        return
      if action == "OK": 
        print "OK"

if __name__ == '__main__':
  main()
  
