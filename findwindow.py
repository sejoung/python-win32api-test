
# coding=utf-8
__author__ = 'sanaes'
import win32gui,win32api,win32con
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



#windowHandle = win32gui.FindWindow('Qt5QWindowIcon', 'Telegram')


#(left,top,right,bottom) = win32gui.GetWindowRect(windowHandle)
#win32api.SetCursorPos((left+(right-left)/2,top+(bottom-top)/2))
#inputfile = win32gui.GetDlgItem(windowHandle,None)

#win32gui.SendMessage(inputfile,win32con.WM_SETTEXT,0,'result')


#windowHandle = win32gui.FindWindow('Qt5QWindowIcon', None)


#windowHandle = win32gui.FindWindow(None, 'Medialog')
#hbtn = win32gui.FindWindowEx(windowHandle,None,None,'인증')



#print win32gui.SendMessage(hbtn,win32con.WM_COMMAND,0,0)
#(left,top,right,bottom) = win32gui.GetWindowRect(windowHandle)
#win32api.SetCursorPos((left+(right-left)/2,top+(bottom-top)/2))


def window_handle_Title(Title):
    handle = win32gui.FindWindow(None, Title)
    return handle

def window_handle_class(className):
    handle = win32gui.FindWindow(className, None)
    return handle

def click_btn(hWnd, Button):
    hbutton = win32gui.FindWindowEx(hWnd, 0, 'Button', Button)
    if hbutton != 0:
        win32api.PostMessage(hbutton, win32con.WM_LBUTTONDOWN, 0, 0)
        win32api.PostMessage(hbutton, win32con.WM_LBUTTONUP, 0, 0)
        return True
    return None


DialogName = "Medialog".encode("utf-8")
ButtonName = "인증".encode("utf-8")



hWnd = window_handle_Title(DialogName)

hbtn = win32gui.FindWindowEx(hWnd,None,None,ButtonName)

print hWnd
print hbtn