#-------------------------------------------------------------------------------
# Name: plotSaver.py
# Purpose: Works with SerCom to get plot data from the serial port and
#           save the plot data to the disk.
#           Use plotSaver.py to view the data at the same time.
#
#
# Author: eeAlchemist - http://eealchemy.wordpress.com
#
# Created: 15SEP11
#
# Licence: This work is licensed under a
#          Creative Commons Attribution-ShareAlike 3.0 Unported License.
#
# ToDo: More error trapping
# ToDo: use argv's to set port attributes
# ToDo: more commands to alter plot apperance, title, axes, ect.
# ToDo: make into class
# ToDo: quit after a time of no new data
# ToDo: more comments
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import SerCom
import re
import sys
import plotHelper
import time

def sendRate(secStr):
    try:
        com.recvRate = float(secStr)
        print 'recvRate was set to',secStr
    except:
        print 'could not set sendRate',secs



def setLegend(legendStr):
    try:
        ph.legend=tuple(legendStr.split(','))
        print 'legend is now',legendStr
        outF=open('lastPlot.csv', 'r')
        allStr = outF.read()
        outF.close()
        lineLst=allStr.split('\r\n')
        #print lineLst
        lineLst[0]=legendStr
        outF = open('lastPlot.csv', 'w')
        outF.write('\r\n'.join(lineLst))
        outF.close()
    except:
        print 'could not set legend to',legendStr


def readCommands():
    ''' This grabs the next thing in the recieved stack and either plots the
    point or calls a method'''
    while 1:
        processed = False
        raw_line = com.next()
        time.sleep(com.recvRate/4.0)
        if raw_line != '':
            if '(' in raw_line:
                #looking for method(argument)
                cmd = raw_line.split("(")
                print cmd
                m=re.search("[^);]*",cmd[1])
                if m!=None:
                    getattr(me,cmd[0].strip())(m.group(0))
                    processed =True

            elif ',' in raw_line:
                #looking for x,y0,y1,y2
                writeIt(raw_line)
                processed =True

            elif '=' in raw_line:
                #looking for property = value
                cmd = raw_line.split('=')
                if len(cmd) > 1:
                   getattr(me,cmd[0].strip())(cmd[1].strip())
                   processed = True

			#could not understand so report it
            if not processed:
                print 'WTF  is',raw_line

def clearFile():
    outF = open('lastPlot.csv', 'w')
    outF.write(','.join(ph.legend)+'\r\n')
    outF.close()
    print'lastPlot.csv has been cleared'

def writeIt(plotStr):
    outF=open('lastPlot.csv', 'r+')
    outF.seek(0,2)
    outF.write(plotStr+'\n')
    outF.close
    print plotStr

def setTitle(titleStr):
    pass

com = SerCom.SerCom()
me=sys.modules[__name__]
ph=plotHelper.PlotHelper()
clearFile()
readCommands()
