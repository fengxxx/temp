#!/usr/bin/env python
# -*- coding: cp936 -*-

import Image
import sys
import win32api,win32gui,win32con ,win32ui 
import wx
import os
import pythoncom
import pyHook

GRAP_NUM=0
ROOT_DIR=os.getcwd()
#ROOT_DIR="K:\\temp\\screenGrap_Fengx\\"
ICON_PATH=ROOT_DIR+"\\app.ico"
SAVE_GRAP_MAP_PATH=ROOT_DIR+"\\fengx.png"
SAVE_SCREEN_MAP_PATH=ROOT_DIR+"\\screen.png"
CAN_GRAP=True
CAN_MOVE=False
GRAP_RECT=[1,1,2,2]
GRAP_POS={}
SCREEN_SIZE=(10,10)

#³õÊ¼»¯
#def __int__(self):
    #global SCREEN_SIZE
SCREEN_SIZE=(win32api.GetSystemMetrics(win32con.SM_CXSCREEN),win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
MoniterDev=win32api.EnumDisplayMonitors(None,None)  
SCREEN_SIZE=(MoniterDev[0][2][2],MoniterDev[0][2][3])
 


class TB_Icon(wx.TaskBarIcon):
    global ICON_PATH
    global ALL_FRAME
    m_close=wx.NewId()
    m_seting=wx.NewId()
    m_hide=wx.NewId()
    m_show=wx.NewId()
    m_screenGrap=wx.NewId()
    m_DeleteAll=wx.NewId()
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
        self.SetIcon( wx.Icon(ICON_PATH, wx.BITMAP_TYPE_ICO), "screenGrap by fengx!")
        self.imgidx = 1

        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate )   
        self.Bind(wx.EVT_MENU, self.showALL_FRAME, id=self.m_show)
        self.Bind(wx.EVT_MENU, self.hideALL_FRAME, id=self.m_hide) 
        self.Bind(wx.EVT_MENU, self.grapScreen, id=self.m_screenGrap)
        self.Bind(wx.EVT_MENU, self.closeApp, id=self.m_close)
    	self.Bind(wx.EVT_MENU, self.onDeleteAll, id=self.m_DeleteAll)
    def CreatePopupMenu(self):
        menu= wx.Menu()
        menu.Append(self.m_show, "Show all window") 
        menu.Append(self.m_hide,  "Hide all window")
        menu.AppendSeparator()
        menu.Append(self.m_screenGrap, "Grap")
        menu.Append(self.m_DeleteAll, "Delete All DATA")
        menu.Append(self.m_close, "Exit")
        return menu

    def OnTaskBarActivate(self, evt):
        grapStart(bmp)
        '''
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()
        '''
    def OnTaskBarClose(self, evt):
        self.frame.Show(False)

    def OnTaskBarChange(self, evt):
        self.SetIcon(wx.Icon(os.getcwd()+'\\arp.ico'), "This is a new icon: " + name)
        #self.frame.Show(True)
    def showALL_FRAME(self,evt):
        for s in ALL_FRAME:
            try:
                s.Show()
            except ImportError:
                print ""
    def hideALL_FRAME(self,evt):
        for s in ALL_FRAME:   
            try:
                s.Hide()
            except ImportError:
                print ""
        
    def closeApp(self, evt):
        self.RemoveIcon()
        #self.frame.Close()
        sys.exit()
		
    def grapScreen(self, evt):
        grapStart(bmp)

    def onDeleteAll(self, event):
        global ROOT_DIR
        files= os.listdir(ROOT_DIR)
        for s in ALL_FRAME:
            try:
                s.Hide()
                s.Close()
            except ImportError:
                print ""
        for m in files:
            if os.path.splitext(m)[1]==".png":
                os.remove(m)

class grapingScreenFrame(wx.Frame):
    global ICON_PATH
    global SAVE_GRAP_MAP_PATH
    global GRAP_RECT
    global SCREEN_SIZE
    print SCREEN_SIZE
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id,'null',size=SCREEN_SIZE ,style=wx.SIMPLE_BORDER|wx.STAY_ON_TOP)
        tBmp=wx.EmptyBitmap(10,10, depth=-1)
        self.SetSize(SCREEN_SIZE)
        self.bg=wx.StaticBitmap(self,-1,  tBmp, (0,0))
        self.bg.Bind(wx.EVT_LEFT_UP, self.OnLeftMouseUp)
        self.bg.Bind(wx.EVT_LEFT_DOWN, self.OnLeftMouseDown)
        self.bg.Bind(wx.EVT_MIDDLE_UP,  self.close)
        self.icon = wx.Icon(ICON_PATH, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)  
        
        #set icon
        try:
            self.tbicon = TB_Icon(self)
        except:
            self.tbicon = None

    def OnLeftMouseDown(self, event):
        GRAP_RECT[0]= event.GetPosition()[0]
        GRAP_RECT[1]= event.GetPosition()[1]
        print GRAP_RECT
            
    def OnLeftMouseUp(self, event):
        GRAP_RECT[2]= event.GetPosition()[0]
        GRAP_RECT[3]= event.GetPosition()[1]
        self.Hide()
        grap(GRAP_RECT,SAVE_GRAP_MAP_PATH)
        #print GRAP_RECT
    def close(self,event):
        self.Hide()
        #self.Close()


class grapPartFrame(wx.Frame):
    global SCREEN_SIZE
    global GRAP_RECT
    global CAN_MOVE
    global GRAP_NUM
    global GRAP_POS

    cRect=(10,10,10,10)
    pos=(20,20)
    cRect=[0,0,0,0]
    cRect[0]=GRAP_RECT[0]
    cRect[1]=GRAP_RECT[1]
    pos=[GRAP_RECT[0],GRAP_RECT[1]]
    bSize=SCREEN_SIZE
    sSize=(SCREEN_SIZE[0]*0.1,SCREEN_SIZE[1]*0.1)
    log="ss"
    ID=0
    

    def __init__(self, parent, id):
        GRAP_POS[str(GRAP_NUM)]=[GRAP_RECT[0],GRAP_RECT[1],10,10,0,1,1]
        self.ID=GRAP_NUM
        wx.Frame.__init__(self, parent, id, 'fengx', size=SCREEN_SIZE,style=wx.SIMPLE_BORDER|wx.STAY_ON_TOP)
        #self.bg=wx.StaticBitmap(self,-1,  wx.EmptyBitmap(10,10, depth=-1), (0,0))

        tBmp=wx.EmptyBitmap(10,10, depth=-1)

        self.bg=wx.StaticBitmap(self,-1,  tBmp, (0,0))
        self.bg.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.bg.Bind(wx.EVT_LEFT_DCLICK, self.OnMouseLeftDclick)
        self.bg.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.bg.Bind(wx.EVT_MOTION,  self.OnMove)
        self.bg.Bind(wx.EVT_MIDDLE_UP,  self.close)
        self.Bind(wx.EVT_MOUSEWHEEL, self.scale)
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
       
        #self.p=wx.Panel   
        #self.p.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)    
    def scale(self,event):
        im=wx.Image(str(os.path.dirname(SAVE_GRAP_MAP_PATH)+"\\grapPart_"+str(self.ID)+".png" ))
        #im= self.bg.GetBitmap().ConvertToImage()
        if event.GetWheelRotation()<0:
            if self.GetSize()[0]>30 and self.GetSize()[1]>30 :
                tSize=(self.GetSize()[0]*0.9,self.GetSize()[1]*0.9)
                #im.Resize(tSize)
                tim=im.Rescale(self.GetSize()[0]*0.9,self.GetSize()[1]*0.9)
                self.bg.SetBitmap(wx.BitmapFromImage(tim))  
                self.SetSize(tSize)
        elif self.GetSize()[0]<self.bSize[0] and self.GetSize()[1]<self.bSize[1] :
            tSize=(self.GetSize()[0]*1.1,self.GetSize()[1]*1.1)
            tim=im.Rescale(self.GetSize()[0]*1.1,self.GetSize()[1]*1.1)
            self.bg.SetBitmap(wx.BitmapFromImage(tim))  
            self.SetSize(tSize)


    def OnMouseLeftDclick(self, event):  
        im=wx.Image(str(os.path.dirname(SAVE_GRAP_MAP_PATH)+"\\grapPart_"+str(self.ID)+".png" )) 
        if self.GetSize()[0]<im.Width*0.2:
            tim=im.Rescale(im.Width,im.Height)
            self.bg.SetBitmap(wx.BitmapFromImage(tim))  
            self.SetSize((im.Width,im.Height))
            self.SetPosition(((GRAP_POS[str(self.ID)][0]-GRAP_POS[str(self.ID)][5]),(GRAP_POS[str(self.ID)][1]-GRAP_POS[str(self.ID)][6])))

        else:
            tim=im.Rescale(im.Width*0.2,im.Height*0.2)
            self.bg.SetBitmap(wx.BitmapFromImage(tim))  
            self.SetSize((im.Width*0.2,im.Height*0.2))
            GRAP_POS[str(self.ID)][5]=event.GetPosition()[0]
            GRAP_POS[str(self.ID)][6]=event.GetPosition()[1]
            self.SetPosition(((GRAP_POS[str(self.ID)][1]+GRAP_POS[str(self.ID)][5]),(GRAP_POS[str(self.ID)][6]+GRAP_POS[str(self.ID)][6])))
    def OnMouseLeftDown(self, event):

        GRAP_POS[str(self.ID)][2]=event.GetPosition()[0]
        GRAP_POS[str(self.ID)][3]=event.GetPosition()[1]
        GRAP_POS[str(self.ID)][4]=1
        #print "dian ji DOWN"
        #print self.ID

    def OnMouseLeftUp(self, event):
        GRAP_POS[str(self.ID)][4]=0
        #print "dian ji up"

    def close(self,event):
        self.Close()

    def OnMouseRightDown(self, event):
        print "RightDown"
        #self.Close()

    def OnMove(self, event):
        newPosX=event.GetPosition()[0]-GRAP_POS.get(str(self.ID))[2]+GRAP_POS.get(str(self.ID))[0]
        newPosY=event.GetPosition()[1]-GRAP_POS.get(str(self.ID))[3]+GRAP_POS.get(str(self.ID))[1]
        newPos=wx.Point=(newPosX,newPosY)
        if GRAP_POS[str(self.ID)][4]==1:
            self.SetPosition(newPos)
            GRAP_POS[str(self.ID)][0]=newPosX
            GRAP_POS[str(self.ID)][1]=newPosY
            #print self.ID



    def OnContextMenu(self, event):
        #print ("OnContextMenu\n")

        # only do this part the first time so the events are only bound once
        #
        # Yet another anternate way to do IDs. Some prefer them up top to
        # avoid clutter, some prefer them close to the object of interest
        # for clarity. 

        if not hasattr(self, "pp_SAVE"):
            self.pp_SAVE = wx.NewId()
            self.pp_CLOSE = wx.NewId()
            self.pp_HIDE = wx.NewId()
            self.pp_DELETE = wx.NewId()
            self.pp_TEST= wx.NewId()
            self.pp_GRAP=wx.NewId()

            self.Bind(wx.EVT_MENU, self.onSave, id=self.pp_SAVE)
            self.Bind(wx.EVT_MENU, self.onClose, id=self.pp_CLOSE)
            self.Bind(wx.EVT_MENU, self.onHide, id=self.pp_HIDE)
            self.Bind(wx.EVT_MENU, self.onDelete, id=self.pp_DELETE)    
            self.Bind(wx.EVT_MENU, self. grapScreen, id=self.pp_GRAP)

        menu = wx.Menu()

        menu.Append(self.pp_GRAP,"&Grap")
        item = wx.MenuItem(menu, self.pp_SAVE,"&Save")
        bmp=wx.BitmapFromIcon(wx.Icon(os.getcwd()+'\\App.ico'))
        #item.SetBitmap(bmp)
        menu.AppendItem(item)

        menu.Append(self.pp_CLOSE, "&Close")
        menu.Append(self.pp_HIDE, "&Hide")
        menu.Append(self.pp_DELETE, "&Delete")
        sm = wx.Menu()
        sm.Append(self.pp_TEST, "ThreeKindom")
        sm.Append(self.pp_TEST, "ZHOU")
        menu.AppendMenu(self.pp_TEST, "RuangJi", sm)

        self.PopupMenu(menu)
        menu.Destroy()

    def grapScreen(self, evt):
        grapStart(bmp)
    def onSavee(self, event):
        
        wildcard = "Python source (*.png)|*.png|"     \
           "All files (*.*)|*.*"

        dlg = wx.FileDialog(
            self, message="Save file as ...", defaultDir=os.getcwd(), 
            defaultFile="", wildcard=wildcard, style=wx.SAVE
            )

        print dlg.GetPath()
        dlg.SetFilterIndex(2)
        print "xxxxa"
        print dlg.GetPath()
        if dlg.ShowModal() == wx.ID_OK:
            if os.path.isdir(dlg.GetPath()):
                sPath=os.path.dirname(sPath)+"\\grapPart_"+str(self.ID+1)+".png" 
                copyFiles(sPath, dlg.GetPath())
        dlg.Destroy()

    def onSave(self,event):
        global SAVE_GRAP_MAP_PATH
        wildcard = "Python source (*.png)|*.png|"     \
        "All files (*.*)|*.*"
        dialog=wx.FileDialog(self, message="Save file as ...", defaultDir=os.getcwd(), 
        defaultFile="test.png", wildcard=wildcard,style=wx.SAVE)

        tPath=os.path.dirname(SAVE_GRAP_MAP_PATH)+"\\grapPart_"+str(self.ID)+".png" 
        if dialog.ShowModal()==wx.ID_OK:            
            #print tPath
            #print  dialog.GetPath()
            #print os.path.isdir(self.beWindowsPath(tPath))
            #if os.path.isdir(self.beWindowsPath(tPath)):
            os.system ("copy %s %s" % (tPath, dialog.GetPath()))


        #dialog.destory()
    def onClose(self, event):
        self.Close()

    def onHide(self, event):
        self.Hide()

    def onDelete(self, event):
        tPath=os.path.dirname(SAVE_GRAP_MAP_PATH)+"\\grapPart_"+str(self.ID)+".png"
        os.remove(tPath)
        self.Close()

    def onDeleteAll(self, event):
        global ROOT_DIR
        files= os.listdir(ROOT_DIR)
        for s in ALL_FRAME:
            try:
                s.Hide()
                s.Close()
            except ImportError:
                print ""
        for m in files:
            if os.path.splitext(m)[1]==".png":
                os.remove(m)

    def beWindowsPath(self,cPath):
        newPath=""
        for s in cPath:
            if s=="\\":
                newPath+="/"
            else:
                newPath+=s

        return newPath

#---<string> map path
def createMap(mapPath):
    global GRAP_RECT
    global SCREEN_SIZE
    global GRAP_NUM
    GRAP_NUM+=1
    startPos=wx.Point=(GRAP_RECT[0],GRAP_RECT[1])
    tImage=wx.Image(mapPath,wx.BITMAP_TYPE_PNG)
    mapSize=tImage.GetSize()
    newFrame = grapPartFrame(parent=None, id=-1)
    newFrame.SetSize(mapSize)
    newFrame.SetPosition(startPos)
    newFrame.bg.SetBitmap(wx.BitmapFromImage(tImage))
    newFrame.Show()
    ALL_FRAME.append(newFrame)


        
def grap(box,sPath):
    global GRAP_NUM
    global SAVE_SCREEN_MAP_PATH
    sPath=os.path.dirname(sPath)+"\\grapPart_"+str(GRAP_NUM+1)+".png" 
    im = Image.open(SAVE_SCREEN_MAP_PATH)
    imSize=()
    cim=Image.new('RGB',(abs(box[2]-box[0]),abs(box[3]-box[1])))
    region = im.crop(box)
    cim.paste(region, (0,0))
    cim.save(sPath)
    createMap(sPath)
def screenCapture(savePath,size):
    global SAVE_SCREEN_MAP_PATH

    hwnd = 0  
    hwndDC = win32gui.GetWindowDC(hwnd)   
    mfcDC=win32ui.CreateDCFromHandle(hwndDC)   
    saveDC=mfcDC.CreateCompatibleDC()   
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, size[0], size[1])   
    saveDC.SelectObject(saveBitMap)   
    saveDC.BitBlt((0,0),(size[0], size[1]) , mfcDC, (0,0), win32con.SRCCOPY)  
    

    saveBitMap.SaveBitmapFile(saveDC,SAVE_SCREEN_MAP_PATH)  
    Image.open(SAVE_SCREEN_MAP_PATH).save(SAVE_SCREEN_MAP_PATH[:-4]+".png")  



    

def grapStart(bmp):
    global SCREEN_SIZE
    global SAVE_SCREEN_MAP_PATH
    screenCapture(SAVE_SCREEN_MAP_PATH,SCREEN_SIZE)
    tImage=wx.Image(SAVE_SCREEN_MAP_PATH,wx.BITMAP_TYPE_PNG)
    mainFrame.bg.SetBitmap(wx.BitmapFromImage(tImage))
    mainFrame.Show()

        
def start():
    #global GRAP_NUM
    global ROOT_DIR
    #files=os.walk(ROOT_DIR)
    files= os.listdir(ROOT_DIR)
    print type(files)
    #files.sort() 
    for m in files:
        if os.path.splitext(m)[1]==".png":
            if os.path.basename(m)[0]=="g":
                createMap(ROOT_DIR+"\\"+ m)
                #GRAP_NUM[0]+=1





def onMouseEvent(event):
    '''

    fobj.writelines('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '\n')
    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    fobj.writelines("MessageName:%s\n" % str(event.MessageName))
    fobj.writelines("Message:%d\n" % event.Message)
    fobj.writelines("Time_sec:%d\n" % event.Time)
    fobj.writelines("Window:%s\n" % str(event.Window))
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))
    fobj.writelines("Position:%s\n" % str(event.Position))
    fobj.writelines('-' * 20 + 'MouseEvent End' + '-' * 20 + '\n')
    '''
    return True


def onKeyboardEvent(event):
    '''

    fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')
    fobj.writelines("Current Time:%s\n" %  time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    fobj.writelines("MessageName:%s\n" % str(event.MessageName))
    fobj.writelines("Message:%d\n" % event.Message)
    fobj.writelines("Time:%d\n" % event.Time)
    fobj.writelines("Window:%s\n" % str(event.Window))
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))
    fobj.writelines("Ascii_code: %d\n" % event.Ascii)
    fobj.writelines("Ascii_char:%s\n" % chr(event.Ascii))
    fobj.writelines("Key:%s\n" % str(event.Key))
    fobj.writelines('-' * 20 + 'Keyboard End' + '-' * 20 + '\n')
    print str(event.Key)
    '''
    #print str(event.Key)
    return True





ALL_FRAME=[]
mainApp = wx.PySimpleApp()
bmp=wx.EmptyBitmap(10,10, depth=-1)
mainFrame=grapingScreenFrame(parent=None, id=-1)
mainFrame.bg.SetBitmap(bmp)
start()
'''
hm = pyHook.HookManager()

hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()

hm.MouseAll = onMouseEvent
hm.HookMouse()

pythoncom.PumpMessages()
'''
mainApp.MainLoop()
#---------global key

