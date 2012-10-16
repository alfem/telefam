#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam users module
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 10/Jul/2012

import User_Storage
import os

# Function called by telefam-daemon in order to trigger automatic download of new items
def daemon(CONF, CONNECTION, VOICE):
    user_storage=User_Storage.storage(CONF["USERS"]["data_path"])

    tmp_filename=os.path.join(CONF["DAEMON"]["data_path"],"user_photo.tmp" )

    items=CONNECTION.call("get_user_list")
    
    for item in items:
        remote_data=CONNECTION.call("get_user",item)
        photo=CONNECTION.get_file("get_user_photo",item, tmp_filename)

        print remote_data["first_name"]

        u=User_Storage.User(str(remote_data["id"]), remote_data["first_name"]+" "+remote_data["last_name"],"")
        result=user_storage.store(u)
        print result

        user_storage.update_photo(u.id, tmp_filename)

    return "OK"


  
