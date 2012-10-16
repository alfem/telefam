#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 23/Jun/2012

# In order to use Festival instead of espeak:
#  install festival, speech-dispatcher, python-speechd, and some voices (festvox-palpc16k for Spanish)
#  edit /etc/speech-dispatcher/modules/festival.conf to start festival daemon
#  edit /etc/festival.scm and add default voice: (set! voice_default 'voice_JuntaDeAndalucia_es_pa_diphone)
#  start festival --server   
    
import speechd

class Synthesizer:
    '''
    Speech Synthesizer for notifications (when no screen available) and user interface
    '''
    def __init__(self,active,CONF):

      self.active = active
      if not self.active:
          return

      self.client=speechd.SSIPClient('telefam')

# print client.list_output_modules()
# print client.list_synthesis_voices()

      self.client.set_output_module(CONF["module"])
      self.client.set_language(CONF["language"])
      self.client.set_pitch(int(CONF["pitch"]))
      self.client.set_rate(int(CONF["rate"]))
      self.client.set_synthesis_voice(CONF["voice"])
      self.client.set_punctuation(speechd.PunctuationMode.SOME)


    def say(self,text):
      if not self.active:
          return
      self.client.speak(text)

    def close(self):
      if not self.active:
          return
      self.client.close()
   
