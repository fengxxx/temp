from ctypes import *
import win32api, win32con
import time
#装载windows dll
User32dll = windll.User32
print windll.User32
"""
主要学习
1 python byref关键字,送数据结构指针空间的关键字
2 windows api:
GetCursorPos(x,y)
SetCursorPos(x,y)
"""
class POINT(Structure):
        _fields_ = [
                ("x", c_ulong),
                ("y", c_ulong)
                ]

def timer_Tick():
        point = POINT()
        User32dll.GetCursorPos(byref(point))
        print 'current Pos:', point.x, point.y

if __name__ == '__main__':
        i = 0
        maxcount = 10
        while i < maxcount:
              timer_Tick()
              time.sleep(1)
              i += 1
