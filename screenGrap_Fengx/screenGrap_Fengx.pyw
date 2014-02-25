#!/usr/bin/env python
import ImageGrab
import Image
import sys
import win32api,win32gui,win32con ,win32ui ,os
import wx
import os


# rootDir=os.getcwd()
rootDir="K:\\temp\\screenGrap_Fengx\\"
iconPath=rootDir+"\\app.ico"
savePath=rootDir+"fengx.png"
grapPath=rootDir+"screen.png"
canGrap=True
rect=[1,1,2,2]
screenSize=(win32api.GetSystemMetrics(win32con.SM_CXSCREEN),win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
MoniterDev=win32api.EnumDisplayMonitors(None,None)  
w = MoniterDev[0][2][2]  
h = MoniterDev[0][2][3]  

screenSize=(w,h)

class TB_Icon(wx.TaskBarIcon):
    TBMENU_RESTORE = wx.NewId()
    TBMENU_CLOSE   = wx.NewId()
    TBMENU_CHANGE  = wx.NewId()
    TBMENU_REMOVE  = wx.NewId()
    TBMENU_SHOW	=   wx.NewId()
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon( wx.Icon(iconPath, wx.BITMAP_TYPE_ICO), "screenGrap by fengx!")
        self.imgidx = 1
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate)
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=self.TBMENU_RESTORE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE) 
        self.Bind(wx.EVT_MENU, self.showWindow, id=self.TBMENU_SHOW)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRemove, id=self.TBMENU_REMOVE)
	
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.TBMENU_RESTORE, "Restore wxPython Demo")
        menu.Append(self.TBMENU_CLOSE,   "Close wxPython Demo")
        menu.AppendSeparator()
        menu.Append(self.TBMENU_SHOW, "关闭窗口")
        menu.Append(self.TBMENU_REMOVE, "关闭")
        return menu

    def OnTaskBarActivate(self, evt):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()
        
    def OnTaskBarClose(self, evt):
        self.frame.Show(False)
        #self.frame.Close()
        #if not self.frame.IsShown():
            #self.frame.Show(True)
        #else:
            #self.frame.Show(False)
    def OnTaskBarChange(self, evt):
        self.SetIcon(wx.Icon(os.getcwd()+'\\arp.ico'), "This is a new icon: " + name)
        self.frame.Show(True)
    def OnTaskBarRemove(self, evt):
        self.RemoveIcon()
        #self.frame.Close()
        sys.exit()
		
    def showWindow(self, evt):
        self.frame.show()
        #self.frame.show(False)
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

        self.icon = wx.Icon(iconPath, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)  


        
        self.bg=wx.StaticBitmap(self,-1,  wx.BitmapFromImage(bmp), (0,0))
        self.bg.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.bg.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.bg.Bind(wx.EVT_MOTION,  self.OnMove) 


        try:
            self.tbicon = TB_Icon(self)
        except:
            self.tbicon = None
        self.button2.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
    def OnButtonClick(self, event):
        self.panel.SetBackgroundColour(os.getcwd()+'Green')
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
            
            #self.bg.Bind(wx.EVT_MOUSEWHEEL,  self.scaleS)
            #self.bg.Bind(wx.EVT_MIDDLE_UP,  self.scaleB)
            
            #self.bg.Bind(wx.EVT_MIDDLE_DOWN,  self.OnMove)
            self.icon = wx.Icon(rootDir+"\\max.ico", wx.BITMAP_TYPE_ICO)
            self.SetIcon(self.icon)
            self.Bind(wx.EVT_MOUSEWHEEL, self.scale)
        
        def scale(self,event):
            if event.GetWheelRotation()>0:
                if self.GetSize()[0]>30 and self.GetSize()[1]>30 :
                    tSize=(self.GetSize()[0]*0.8,self.GetSize()[1]*0.8)
                    self.SetSize(tSize)
            elif self.GetSize()[0]<bSize[0] and self.GetSize()[1]<bSize[0] :
                tSize=(self.GetSize()[0]*1.2,self.GetSize()[1]*1.2)
                self.SetSize(tSize)

        
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

	
	
'''cmd /k "echo $(CURRENT_DIRECTORY)" & PAUSE 
cmd /k set b="\\" & set a=%CURRENT_DIRECTORY:~1,-1%%b:~1,-1% % echo %a%  & PAUSE 

set c=%a:~1,-1%%b:~1,-1%

cmd /k set a= %"$(CURRENT_DIRECTORY)":~1,-1%%"\\":~1,-1%  & PAUSE 


cmd /k set a="$(CURRENT_DIRECTORY)" &  echo %a% & set b="//" &  echo %b%   &set c=%"$(CURRENT_DIRECTORY)":~1,-1%%b:~1,-1% & echo %c%  & echo "$(CURRENT_DIRECTORY)" &  PAUSE 


cmd  cd "$(CURRENT_DIRECTORY)" & ECHO. & PAUSE 


变量名称                含义                 例子
FULL_CURRENT_PATH     文件路径名称        E:\java\HelloNpp.java
CURRENT_DIRECTORY     文件目录            E:\java\
FILE_NAME             文件全名称            HelloNpp.java
NAME_PART             文件名称            HelloNpp
EXT_PART              文件扩展名            java


'''
