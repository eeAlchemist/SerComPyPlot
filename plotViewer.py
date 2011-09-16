#-------------------------------------------------------------------------------
# Name: plotViewer.py
# Purpose: Works with plot saver to view the plot that plotSaver is saving
#          to the disk.
#
# Author: eeAlchemist - http://eealchemy.wordpress.com
#
# Created: 15SEP11
#
# Licence: This work is licensed under a
#          Creative Commons Attribution-ShareAlike 3.0 Unported License.
#
# ToDo: More error trapping
# ToDo: Use argv's for file to plot
# ToDo: Make Wx independent ?
# ToDo: Make use of numPy arrays?
# ToDo: quit after a time of no new data
# ToDo:
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import time
import matplotlib
matplotlib.use('WXAgg') # do this before importing pylab
import matplotlib.pyplot as plt

args=[]

def getArgs():
    ''' converters a CSV formated data file to matplotlib arguments'''
    try:
        inF=open('lastPlot.csv', 'r')
        #there are many options for line format
        #see the matplotlib site for details
        colorLst ='b-,r-,g-,b-,y-,c-,b-'.split(',')

        allStr=inF.read()
        inF.close()
        if '\r' in allStr:
            lineLst=allStr.split('\r\n')
        else:
            lineLst=allStr.split('\n')

        #the legend is the first line in the plot file
        # the X axis is always time and not included



        thelegend=lineLst.pop(0)

        #if ax.legend.get_texts() =='':
        #ax.legend(tuple(thelegend.split(',')),loc=0)

        #first data point is on 2nd line
        first = lineLst.pop(0)
        coordLst = first.split(',')
        '''setting up the list of floats for x,y0,y1....yn'''

        for i in range(len(coordLst)):
            coordLst[i]= [float(coordLst[i])]
        ## now we have something like this
        ##    [[0.57], [25.0], [25.0], [0.0], [-32.0], [30.0]]
        ## this can be easily appended to.
        for line in lineLst:
            xylst=line.split(',')
            #print xylst
            if len(xylst) == len(coordLst):
                for i in range(len(coordLst)):
                    coordLst[i].append(float(xylst[i]))

        ##x,y0,y1...yn all have their own list and held in coordLst
        ## Now to put it into x,y0,f0,x,y1,f1 arrangement to plot
        args =[]
        for i in range(1,len(coordLst)):
            args.append(coordLst[0])
            args.append(coordLst[i])
            args.append(colorLst[i])
        return args
    except:
        print 'Ooops! there may be a problem'
        return None

def updatePlot(event):
    '''Clears, updates and redraws the plot when called by timer'''
    args=getArgs()

    #lines are removed because all ploted lines are appended
    for line in ax.lines:
        ax.lines.remove(line)
    if args != None:
        lines = ax.plot(*args)
        ax.figure.canvas.draw()



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
args = None
while args == None:
    args=getArgs()

ax.plot(*args)
#uses a wxTimer to update the plot as seen at matplotlib website
import wx
id = wx.NewId()
actor = fig.canvas.manager.frame
timer = wx.Timer(actor, id=id)
timer.Start(1000)
wx.EVT_TIMER(actor, id, updatePlot)

plt.show()

