#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam photos module
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 1/Aug/2012

import Photo_Storage
from users import *

# Function called by telefam-daemon in order to trigger automatic download of new items
def daemon(CONF, CONNECTION, VOICE):
    return "OK"

# Main
def main(CONF, INTERFACE, CONTROLLER ):
    module_name=__name__

    user_storage=User_Storage.storage(CONF["USERS"]["data_path"])
    photo_storage=Photo_Storage.storage(CONF["MODULES"]["photos"]["data_path"], user_storage)

    galleries=photo_storage.list_galleries()

# Main loop
    indexg=0

    while True:
        INTERFACE.clean()

        if len(galleries) == 0:
            INTERFACE.show_warning("No hay fotos\nVuelva al menú")
            subaction=INTERFACE.show_actions_menu(CONTROLLER,["Volver al MENU"], 0)
            if subaction==0:
                break;
        else:          
            page=[]
            if indexg - 1 >= 0:
                page.append(photo_storage.get_gallery(galleries[indexg - 1]))
            else:
                page.append(False)
            page.append(photo_storage.get_gallery(galleries[indexg]))
            if indexg + 1 < len(galleries):
                page.append(photo_storage.get_gallery(galleries[indexg + 1]))
            else:
                page.append(False)

# Show a list of galleries and select one
        INTERFACE.show_galleries(page)
        action=CONTROLLER.wait_for_user_action()
        print action
        if (action == "UP") and indexg > 0: 
            indexg -=1
        if (action == "DOWN") and indexg < len(galleries) - 1: 
            indexg +=1
        if action == "END":
            break
        if action == "OK": 
            indexp=0
            photos=photo_storage.list_photos(galleries[indexg])
            while True:
                INTERFACE.clean()
# Show every photo in the selected gallery
                INTERFACE.show_photo(photo_storage.get_photo(galleries[indexg],photos[indexp]))
                action=CONTROLLER.wait_for_user_action()
                if (action == "LEFT") and indexp > 0: 
                    indexp -=1
                if (action == "RIGHT") and indexp < len(photos) - 1: 
                    indexp +=1
                if action == "END":
                    break
                if action == "OK": 
                    break
    return
  
if __name__ == '__main__':
  main()
  
