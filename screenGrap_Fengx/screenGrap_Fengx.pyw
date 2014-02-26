#!/usr/bin/env python
import ImageGrab
import Image
import sys
import win32api,win32gui,win32con ,win32ui ,os
import wx
import os


rootDir=os.getcwd()
#rootDir="K:\\temp\\screenGrap_Fengx\\"

iconPath=rootDir+"\\app.ico"
savePath=rootDir+"\\fengx.png"
screenMapPath=rootDir+"\\screen.png"

canGrap=True
rect=[1,1,2,2]
screenSize=(win32api.GetSystemMetrics(win32con.SM_CXSCREEN),win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
MoniterDev=win32api.EnumDisplayMonitors(None,None)  

screenSize=(MoniterDev[0][2][2],MoniterDev[0][2][3])




class TB_Icon(wx.TaskBarIcon):
    m_close=wx.NewId()
    m_seting=wx.NewId()
    m_hide=wx.NewId()
    m_show=wx.NewId()
    m_screenGrap=wx.NewId()
    '''
    TBMENU_RESTORE = wx.NewId()
    TBMENU_CLOSE   = wx.NewId()
    TBMENU_CHANGE  = wx.NewId()
    TBMENU_REMOVE  = wx.NewId()
    TBMENU_SHOW	=   wx.NewId()
    ''' 
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon( wx.Icon(iconPath, wx.BITMAP_TYPE_ICO), "screenGrap by fengx!")
        self.imgidx = 1

        #self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate    
        #self.Bind(wx.EVT_MENU, self.showAllFrame, id=self.m_show)
        #self.Bind(wx.EVT_MENU, self.hideAllFrame, id=self.m_hide) 
        self.Bind(wx.EVT_MENU, self.grapScreen, id=self.m_screenGrap)
        self.Bind(wx.EVT_MENU, self.closeApp, id=self.m_close)
	
    def CreatePopupMenu(self):
        menu= wx.Menu()
        menu.Append(self.m_show, "Show all window") #"显示窗口")#
        menu.Append(self.m_hide,  "Eide all window") #"隐藏窗口")#
        menu.AppendSeparator()
        menu.Append(self.m_screenGrap, "Grap")#"截图")
        menu.Append(self.m_close, "Exit")#"退出")
        return menu

    def OnTaskBarActivate(self, evt):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()
        
    def OnTaskBarClose(self, evt):
        self.frame.Show(False)

    def OnTaskBarChange(self, evt):
        self.SetIcon(wx.Icon(os.getcwd()+'\\arp.ico'), "This is a new icon: " + name)
        self.frame.Show(True)
    
    def closeApp(self, evt):
        self.RemoveIcon()
        #self.frame.Close()
        sys.exit()
		
    def grapScreen(self, evt):
        grapStart(bmp)
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
        global pos
        pos=[rect[0],rect[1]]
        global canMove
        canMove=[0,0]
        def __init__(self, parent, id):
            wx.Frame.__init__(self, parent, id, 'ccc', 
                    size=mapSize,style=wx.SIMPLE_BORDER)
            self.bg=wx.StaticBitmap(self,-1,  wx.BitmapFromImage(tempBmp), (0,0))
            #self.Bind(wx.EVT_RIGHT_UP, self.OnContextMenu)
            #self.bg.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightUp)
            
            self.bg.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
            self.bg.Bind(wx.EVT_LEFT_DCLICK, self.OnMouseLeftDclick)
            self.bg.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
            self.bg.Bind(wx.EVT_MOTION,  self.OnMove)
            
            #self.bg.Bind(wx.EVT_MOUSEWHEEL,  self.scaleS)
            self.bg.Bind(wx.EVT_MIDDLE_UP,  self.close)
            
            #self.bg.Bind(wx.EVT_MIDDLE_DOWN,  self.OnMove)
            self.icon = wx.Icon(rootDir+"\\max.ico", wx.BITMAP_TYPE_ICO)
            self.SetIcon(self.icon)
            self.Bind(wx.EVT_MOUSEWHEEL, self.scale)
            
            self.p=wx.Panel   
            #self.p.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)    
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
            canMove[0]=1
            #print canMove
            #print "LeftDown"
            
        def OnMouseLeftUp(self, event):
            #print "LeftUp"
            canMove[0]=0
            #print canMove
        def close(self,event):
            #print "RightUp"
            self.Close()
            
            
        def OnMouseRightDown(self, event):
            print "RightDown"
            #self.Close()

        def OnMove(self, event):
            cRect[2]=event.GetPosition()[0]-cRect[0]+pos[0]
            cRect[3]=event.GetPosition()[1]-cRect[1]+pos[1]
            newPos=wx.Point=(cRect[2],cRect[3])
            if canMove[0]==1:
                self.SetPosition(newPos)
                pos[0]=cRect[2]
                pos[1]=cRect[3]

        
    class TestPanel(wx.Panel):
        def __init__(self, parent):
            wx.Panel.__init__(self, parent, -1)
            box = wx.BoxSizer(wx.VERTICAL)

            # Make and layout the controls
            fs = self.GetFont().GetPointSize()
            bf = wx.Font(fs+4, wx.SWISS, wx.NORMAL, wx.BOLD)
            nf = wx.Font(fs+2, wx.SWISS, wx.NORMAL, wx.NORMAL)

            #t = wx.StaticText(self, -1, "PopupMenu")
            t.SetFont(bf)
            box.Add(t, 0, wx.CENTER|wx.ALL, 5)

            box.Add(wx.StaticLine(self, -1), 0, wx.EXPAND)
            box.Add((10,20))

            t = wx.StaticText(self, -1, text)
            t.SetFont(nf)
            box.Add(t, 0, wx.CENTER|wx.ALL, 5)
            t.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)

            self.SetSizer(box)

            self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)


        def OnContextMenu(self, event):
            self.log.WriteText("OnContextMenu\n")

            # only do this part the first time so the events are only bound once
            #
            # Yet another anternate way to do IDs. Some prefer them up top to
            # avoid clutter, some prefer them close to the object of interest
            # for clarity. 
            if not hasattr(self, "popupID1"):
                self.popupID1 = wx.NewId()
                self.popupID2 = wx.NewId()
                self.popupID3 = wx.NewId()
                self.popupID4 = wx.NewId()
                self.popupID5 = wx.NewId()
                self.popupID6 = wx.NewId()
                self.popupID7 = wx.NewId()
                self.popupID8 = wx.NewId()
                self.popupID9 = wx.NewId()

                self.Bind(wx.EVT_MENU, self.OnPopupOne, id=self.popupID1)
                self.Bind(wx.EVT_MENU, self.OnPopupTwo, id=self.popupID2)


            # make a menu
            menu = wx.Menu()
            # Show how to put an icon in the menu
            item = wx.MenuItem(menu, self.popupID1,"One")
            bmp = images.Smiles.GetBitmap()
            item.SetBitmap(bmp)
            menu.AppendItem(item)
            # add some other items
            menu.Append(self.popupID2, "Two")
            menu.Append(self.popupID3, "Three")
            menu.Append(self.popupID4, "Four")
            menu.Append(self.popupID5, "Five")
            menu.Append(self.popupID6, "Six")
            # make a submenu
            sm = wx.Menu()
            sm.Append(self.popupID8, "sub item 1")
            sm.Append(self.popupID9, "sub item 1")
            menu.AppendMenu(self.popupID7, "Test Submenu", sm)


            # Popup the menu.  If an item is selected then its handler
            # will be called before PopupMenu returns.
            self.PopupMenu(menu)
            menu.Destroy()


        def OnPopupOne(self, event):
            self.log.WriteText("Popup one\n")

        def OnPopupTwo(self, event):
            self.log.WriteText("Popup two\n")

        def OnPopupThree(self, event):
            self.log.WriteText("Popup three\n")

        def OnPopupFour(self, event):
            self.log.WriteText("Popup four\n")

        def OnPopupFive(self, event):
            self.log.WriteText("Popup five\n")

        def OnPopupSix(self, event):
            self.log.WriteText("Popup six\n")

        def OnPopupSeven(self, event):
            self.log.WriteText("Popup seven\n")

        def OnPopupEight(self, event):
            self.log.WriteText("Popup eight\n")

        def OnPopupNine(self, event):
            self.log.WriteText("Popup nine\n")



    startPos=wx.Point=(rect[0],rect[1])
    #app = wx.PySimpleApp()
    frame = ccFrame(parent=None, id=-1)
    frame.SetPosition(startPos)
    frame.Show()
    #app.MainLoop()
        
def grap(box,sPath):
    #im=ImageGrab.grab(box)
    
    
    #im.show()
    im = Image.open(screenMapPath)
    imSize=()
    cim=Image.new('RGB',(abs(box[2]-box[0]),abs(box[3]-box[1])))
    region = im.crop(box)
    cim.paste(region, (0,0))
    cim.save(sPath)
    createMap(sPath)
def screenCapture(savePath,size):
    hwnd = 0  
    hwndDC = win32gui.GetWindowDC(hwnd)   
    mfcDC=win32ui.CreateDCFromHandle(hwndDC)   
    saveDC=mfcDC.CreateCompatibleDC()   
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, size[0], size[1])   
    saveDC.SelectObject(saveBitMap)   
    saveDC.BitBlt((0,0),(size[0], size[1]) , mfcDC, (0,0), win32con.SRCCOPY)  
    

    saveBitMap.SaveBitmapFile(saveDC,screenMapPath)  
    Image.open(screenMapPath).save(screenMapPath[:-4]+".png")  



    

def grapStart(bmp):
    app = wx.PySimpleApp()
    frame = grapFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


screenCapture(screenMapPath,screenSize)
bmp=wx.Image(screenMapPath,wx.BITMAP_TYPE_PNG)
if __name__ == '__main__':
    grapStart(bmp)	
	
















'''cmd /k "echo $(CURRENT_DIRECTORY)" & PAUSE 
cmd /k set b="\\" & set a=%CURRENT_DIRECTORY:~1,-1%%b:~1,-1% % echo %a%  & PAUSE 

set c=%a:~1,-1%%b:~1,-1%

cmd /k set a= %"$(CURRENT_DIRECTORY)":~1,-1%%"\\":~1,-1%  & PAUSE 


cmd /k set a="$(CURRENT_DIRECTORY)" &  echo %a% & set b="//" &  echo %b%   &set c=%"$(CURRENT_DIRECTORY)":~1,-1%%b:~1,-1% & echo %c%  & echo "$(CURRENT_DIRECTORY)" &  PAUSE 


cmd  cd "$(CURRENT_DIRECTORY)" & ECHO. & PAUSE 


±äÁ¿Ãû³Æ                º¬Òå                 Àý×Ó
FULL_CURRENT_PATH     ÎÄ¼þÂ·¾¶Ãû³Æ        E:\java\HelloNpp.java
CURRENT_DIRECTORY     ÎÄ¼þÄ¿Â¼            E:\java\
FILE_NAME             ÎÄ¼þÈ«Ãû³Æ            HelloNpp.java
NAME_PART             ÎÄ¼þÃû³Æ            HelloNpp
EXT_PART              ÎÄ¼þÀ©Õ¹Ãû            java


'''
