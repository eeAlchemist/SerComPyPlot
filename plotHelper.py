#-------------------------------------------------------------------------------
# Name: plotHelper.py
# Purpose: A helper class that is used for creating the args for pyplot.
#
# Author: eeAlchemist - http://eealchemy.wordpress.com
#
# Created: 15SEP11
#
# Licence: This work is licensed under a
#          Creative Commons Attribution-ShareAlike 3.0 Unported License.
#
# ToDo: More error trapping
# ToDo: More commenting
# ToDo:
# ToDo:
# ToDo:
# ToDo:
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

class PlotHelper(object):
    def __init__(self):
        self.traceLst =[]
        self.legend =tuple('y1,y2,y3,y4,y5'.split(','))
        self.colorLst ='w-,r-,g-,b-,y-,c-,m-,w-'.split(',')
        self.lastPnt =[]

    def plotArgs(self,pntStr):
        print pntStr
        thePnts=pntStr.split(',')
        if self.lastPnt ==[]:
            self.lastPnt = thePnts
        theArgs=[]
        for i in range(1,len(thePnts)):
            pnt=[]
            pnt.append([float(thePnts[0]),float(self.lastPnt[0])])
            pnt.append([float(thePnts[i]),float(self.lastPnt[i])])
            pnt.append(self.colorLst[i%len(self.colorLst)])
            theArgs.append(pnt)
        self.lastPnt=thePnts
        return theArgs

if __name__ == '__main__':

    testStr = '1,2,3,4'
    ph=PlotHelper()
    print ph.plotArgs(testStr)


