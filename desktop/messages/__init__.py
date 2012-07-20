#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam messages module
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 10/Jul/2012

import Message_Storage
import User_Storage

# Main
def main(CONF, INTERFACE, CONTROLLER):
    module_name=__name__

    user_storage=User_Storage.storage(CONF["USERS"]["data_path"])
    message_storage=Message_Storage.storage(CONF["MODULES"]["messages"]["data_path"], user_storage)
    new_messages=message_storage.list("received")

# Main loop
    index=0

    while True:
      INTERFACE.clean()
      
      m=new_messages[index]
      
      INTERFACE.show_messages(message_storage.get("received",m))
      
      action=CONTROLLER.wait_for_user_action()
      if action == "UP" and index > 0: 
        index -=1
      if action == "DOWN": 
        index +=1
      if action == "END": 
        return
      if action == "OK": 
        print "OK"

if __name__ == '__main__':
  main()
  
