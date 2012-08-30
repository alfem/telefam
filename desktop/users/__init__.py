#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam users module
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 10/Jul/2012

import User_Storage

# Function called by telefam-daemon in order to trigger automatic download of new items
def daemon(CONF, CONNECTION):
    user_storage=User_Storage.storage(CONF["USERS"]["data_path"])

    items=CONNECTION.call("get_user_list")
    
    for item in items:
        message_data=CONNECTION.call("get_message",item)
        print message_data["text"]
        m=Message_Storage.Message(str(message_data["id"]), message_data["created_on"],str(message_data["user_id"]),message_data["text"])
        result=message_storage.create("received",m)
        print result
    return "OK"


  
