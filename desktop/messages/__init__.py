#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam messages module
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 10/Jul/2012

import Message_Storage
from users import *


# Function called by telefam-daemon in order to trigger automatic download of new items
def daemon(CONF, CONNECTION, VOICE):
    user_storage=User_Storage.storage(CONF["USERS"]["data_path"])
    message_storage=Message_Storage.storage(CONF["MODULES"]["messages"]["data_path"], user_storage)
    folder="received"

    items=CONNECTION.call("get_message_list")
    
    for item in items:
        message_data=CONNECTION.call("get_message",item)
        print message_data["text"]
        m=Message_Storage.Message(str(message_data["id"]), message_data["created_on"],str(message_data["user_id"]),message_data["text"])
        result=message_storage.create("received",m)
        print result

    VOICE.say("Tiene %i mensajes nuevos, por favor, conecte la tele para leerlos." % len(items))    

    return "OK"


# Main
def main(CONF, INTERFACE, CONTROLLER):
    module_name=__name__

    user_storage=User_Storage.storage(CONF["USERS"]["data_path"])
    message_storage=Message_Storage.storage(CONF["MODULES"]["messages"]["data_path"], user_storage)
    folder="received"
    messages=message_storage.list(folder)

# Main loop
    index=0

    while True:
      INTERFACE.clean()
      
      if len(messages) == 0:
          INTERFACE.show_warning("No hay mensajes\nVuelva al menú o cambie de carpeta")
          if folder == "received":
            change_folder_text="Ver mensajes antiguos"
          else: 
            change_folder_text="Ver mensajes nuevos"   
          subaction=INTERFACE.show_actions_menu(CONTROLLER,["Volver al MENU", change_folder_text], 0)
          if subaction==0:
              break;
          if subaction==1:
               if folder == "received":
                  folder="old"
               else:
                  folder="received" 
               messages=message_storage.list(folder)
               index=0

      else:
          m=messages[index]
          INTERFACE.show_message(message_storage.get(folder, m))
      
          action=CONTROLLER.wait_for_user_action()
          if (action == "UP" or action == "LEFT") and index > 0: 
            index -=1
          if (action == "DOWN" or action == "RIGHT") and index < len(messages) - 1: 
            index +=1
          if action == "END":
            break
          if action == "OK": 
              if folder == "received":
                change_folder_text="Ver mensajes antiguos"
              else: 
                change_folder_text="Ver mensajes nuevos"   
              subaction=INTERFACE.show_actions_menu(CONTROLLER,["Volver al MENU", change_folder_text,"Borrar este mensaje"], 0)
              if subaction==0:
                  break;
              if subaction==1:
                   if folder == "received":
                      folder="old"
                   else:
                      folder="received" 
                   messages=message_storage.list(folder)
                   index=0
              if subaction==2:
                   message_storage.delete(folder, m)
                   del messages[index]
                   index -=1
                   if index < 0:
                       index = 0
        
if __name__ == '__main__':
  main()
  
