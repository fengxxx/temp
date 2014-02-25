#!/usr/bin/env python
# -*- coding: cp936 -*-
import ImageGrab
import Image
import sys
import win32api,win32gui,win32con ,win32ui ,os
import wx


savePath="fengx.png"
grapPath="screen.png"
canGrap=True
rect=[1,1,2,2]
screenSize=(win32api.GetSystemMetrics(win32con.SM_CXSCREEN),win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
MoniterDev=win32api.EnumDisplayMonitors(None,None)  
w = MoniterDev[0][2][2]  
h = MoniterDev[0][2][3]  

screenSize=(w,h)



class grapFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'null', 
                size=screenSize,style=wx.SIMPLE_BORDER)
        self.panel = wx.Panel(self)                              
        self.button = wx.Button(self.panel, label="Not Over", pos=(100, 15))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button) 
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow) 
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow) 
        self.button.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.button2 = wx.Button(self.panel, label="  Over", pos=(200, 15))
        self.button2.Bind(wx.EVT_RIGHT_UP, self.OnMouseUp)

        self.icon = wx.Icon('App.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)  


        
        self.bg=wx.StaticBitmap(self,-1,  wx.BitmapFromImage(bmp), (0,0))
        self.bg.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.bg.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.bg.Bind(wx.EVT_MOTION,  self.OnMove) 

        
        self.button2.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
    def OnButtonClick(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()


        
    def OnEnterWindow(self, event):
        self.button.SetLabel("Over Me!")
        event.Skip()
        
    def OnLeaveWindow(self, event):
        self.button.SetLabel("Not Over")
        event.Skip()
        
    def OnMouseDown(self, event):
        rect[0]= event.GetPosition()[0]
        rect[1]= event.GetPosition()[1]
        print rect
            
    def OnMouseUp(self, event):
        rect[2]= event.GetPosition()[0]
        rect[3]= event.GetPosition()[1]
        #print rect
        self.Close()
        grap(rect,savePath)

        print "close"
    def OnMove(self, event):
        return True

#---<string> map path
def createMap(mapPath):
    #--pos  and  size

    cRect=[0,0,0,0]
    cRect[0]=rect[0]
    cRect[1]=rect[1]
    tempBmp=wx.Image(mapPath,wx.BITMAP_TYPE_PNG)
    mapSize=tempBmp.GetSize()
    
    bSize=wx.Size=mapSize
    sSize=wx.Size=(mapSize[0]*0.1,mapSize[1]*0.1)
    
    
    class ccFrame(wx.Frame):
        global canMove
        canMove=[1,1]
        def __init__(self, parent, id):
            wx.Frame.__init__(self, parent, id, 'ccc', 
                    size=mapSize,style=wx.SIMPLE_BORDER)
            self.bg=wx.StaticBitmap(self,-1,  wx.BitmapFromImage(tempBmp), (0,0))
            self.bg.Bind(wx.EVT_RIGHT_UP, self.OnMouseRightUp)
            self.bg.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightUp)
            
            self.bg.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
            self.bg.Bind(wx.EVT_LEFT_DCLICK, self.OnMouseLeftDclick)
            self.bg.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
            self.bg.Bind(wx.EVT_MOTION,  self.OnMove)
            #self.bg.Bind(wx.EVT_MIDDLE_DOWN,  self.OnMove)

        def OnMouseLeftDclick(self, event):
            if self.GetSize()[0]<bSize[0]:
                self.SetSize(bSize)
            else:
                self.SetSize(sSize)

        def OnMouseLeftDown(self, event):
            cRect[0]=event.GetPosition()[0]
            cRect[1]=event.GetPosition()[1]
            canMove[0]=0
            #print "LeftDown"
            
        def OnMouseLeftUp(self, event):
            #global canMove
            #print "LeftUp"
            canMove[0]=1
        def OnMouseRightUp(self,event):
            #print "RightUp"
            self.Close()
            
        def OnMouseRightDown(self, event):
            print "RightDown"
            #self.Close()

        def OnMove(self, event):
            #print event.GetPosition()
            cRect[2]=event.GetPosition()[0]-cRect[0]+rect[0]
            cRect[3]=event.GetPosition()[1]-cRect[1]+rect[1]
            pos=wx.Point=(cRect[2],cRect[3])
            if canMove[0]==0:
                #print "canMove"
                #print rect#pos
                self.SetPosition(pos)
                rect[0]=cRect[2]
                rect[1]=cRect[3]
    wx.Point=(rect[0],rect[1])
    #app = wx.PySimpleApp()
    frame = ccFrame(parent=None, id=-1)
    frame.SetPosition(wx.Point)
    frame.Show()
    #app.MainLoop()
        
def grap(box,sPath):
    #im=ImageGrab.grab(box)
    
    
    #im.show()
    im = Image.open(grapPath)
    imSize=()
    cim=Image.new('RGB',(abs(box[2]-box[0]),abs(box[3]-box[1])))
    region = im.crop(box)
    cim.paste(region, (0,0))
    cim.save(sPath)
    createMap(sPath)
def screenCapture(savePath):
 
    hwnd = 0  
    hwndDC = win32gui.GetWindowDC(hwnd)   
    mfcDC=win32ui.CreateDCFromHandle(hwndDC)   
    saveDC=mfcDC.CreateCompatibleDC()   
    saveBitMap = win32ui.CreateBitmap()   


    #print w,h　　　＃图片大小  
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)   
    saveDC.SelectObject(saveBitMap)   
    saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)  
    
    bmpname=grapPath
    saveBitMap.SaveBitmapFile(saveDC, bmpname)  
    Image.open(bmpname).save(bmpname[:-4]+".png")  
    #os.remove(bmpname)  
    #jpgname=bmpname[:-4]+'.bmp'  
    #djpgname=dpath+jpgname  
    #copy_command = "move %s %s" % (jpgname, djpgname)  
    #os.popen(copy_command)  
    #return bmpname[:-4]+'.jpg'



    
    
if __name__ == '__main__':
    #screen=ImageGrab.grab()
    #screen.save(grapPath)
    
    screenCapture("")


    bmp=wx.Image(grapPath,wx.BITMAP_TYPE_PNG)
    mapSize=bmp.GetSize()


    
    app = wx.PySimpleApp()
    frame = grapFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
