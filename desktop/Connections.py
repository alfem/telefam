#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 23/Jun/2012

import urllib2
import json
from configobj import ConfigObj

class Connection:
    '''
    Link betweeen a Telefam desktop and the management web server
    '''
    def __init__(self,CONF):

      self.base_url=CONF["base_url"]
      self.key=CONF["key"]
      self.data_path=CONF["data_path"]

      DATA = ConfigObj(self.data_path+"/connection.dat")
      
      if "last_connection" not in DATA:
          DATA["last_connection"]="2011-10-30 00:00:00"
          DATA.write()
 
      return

    def call(self, function, params={}):
      url="%s%s?key=%s" % (self.base_url, function, self.key)

      for param, value in params.iteritems():
        print param, value
        url+="&%s=%s" % (param, value)

      print url
      remote_file_handler=urllib2.urlopen(url)
      remote_data=json.load(remote_file_handler)
      remote_file_handler.close()

      return remote_data


      


