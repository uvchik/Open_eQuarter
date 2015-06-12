import time
import os
from qgis.core import QgsProject
from PyQt4.QtGui import QProgressBar
from PyQt4.QtCore import Qt
from qgis.utils import iface

global OeQ_project_path
def OeQ_project_path(): return os.path.normpath(QgsProject.instance().readPath(''))
global OeQ_plugin_path
def OeQ_plugin_path(): return os.path.dirname(os.path.realpath(__file__))
# the project path equals './' as long as the project has not been saved
global OeQ_project_saved 
def OeQ_project_saved(): return OeQ_project_path() != './' 

def OeQ_init_progressbar(title='Be patient!',message='Background calculations are going on...',timeout=0,maxcount=100):
  widget = iface.messageBar().createMessage(title,message)      

  #set a new message bar
  progressbarwidget = QProgressBar()
  progressbarwidget.setAlignment(Qt.AlignLeft)
  progressbarwidget.setMaximum(maxcount)           
  progressbarwidget.setValue(0)
  widget.layout().addWidget(progressbarwidget)

  #pass the progress bar to the message Bar
  iface.messageBar().pushWidget(widget,iface.messageBar().INFO)
  print "THIS IS NECESSARY TO TRIGGER THE MESSAGEBAR"
  time.sleep(0.1)
  iface.messageBar().update()
  print "THIS IS NECESSARY TO TRIGGER THE MESSAGEBAR"
  return progressbarwidget

def OeQ_push_progressbar(progressbarwidget,progress_counter):
  progress_counter = progress_counter + 1
  progressbarwidget.setValue(progress_counter)
  return progress_counter

def OeQ_kill_progressbar():
  iface.messageBar().clearWidgets() 

def OeQ_init_info(title='Be patient!',message='Background calculations are going on...'):
  print "INFO"
  widget = iface.messageBar().createMessage(title,message)
  #iface.messageBar().pushInfo(title,message)
  iface.messageBar().pushWidget(widget,iface.messageBar().INFO)
  print "THIS IS NECESSARY TO TRIGGER THE MESSAGEBAR"
  time.sleep(0.1)
  iface.messageBar().update()
  print "THIS IS NECESSARY TO TRIGGER THE MESSAGEBAR"

def OeQ_kill_info():
  iface.messageBar().clearWidgets() 

#title='Be patient!'
#message='Background calculations are going on...'
#OeQ_init_info(title)