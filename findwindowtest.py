# coding=utf-8
__author__ = 'sanaes'
import win32gui, win32api, win32con
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


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


def click_MouseLbtn(hWnd):
    (left, top, right, bottom) = win32gui.GetWindowRect(hWnd)
    win32api.SetCursorPos((left + (right - left) / 2, top + (bottom - top) / 2))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    return True


def get_id(hWnd):
    id = win32gui.GetDlgItem(hWnd, 0x000003F6)
    return id


def get_pw(hWnd):
    pw = win32gui.GetDlgItem(hWnd, 0x000003F9)
    return pw


def get_btn(hWnd):
    btn = win32gui.GetDlgItem(hWnd, 0x000003FC)
    return btn

def send_input_hax(hwnd, msg):
    for c in msg:
        if c == "\n":
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        else:
            win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(c), 0)
    return None


DialogName = "Medialog".encode("utf-8")

hWnd = window_handle_Title(DialogName)
win32gui.SetForegroundWindow(hWnd)

id = get_id(hWnd)
click_MouseLbtn(id)
time.sleep(0.05)
send_input_hax(id,'aaa')
time.sleep(0.05)
pw = get_pw(hWnd)
click_MouseLbtn(pw)
time.sleep(0.05)
send_input_hax(pw,'aa!')
time.sleep(0.05)
btn = get_btn(hWnd)
click_MouseLbtn(btn)

"""
pw = win32gui.GetDlgItem(hWnd, 0x000003F9)

hbtn = win32gui.GetDlgItem(hWnd, 0x000003FC)

(left,top,right,bottom) = win32gui.GetWindowRect(hbtn)
time.sleep(0.05)

win32api.SetCursorPos((left+(right-left)/2,top+(bottom-top)/2))
time.sleep(0.05)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

win32api.SendMessage(id, win32con.WM_KEYDOWN, 0x0000000D, 0x001C0001)
win32api.SendMessage(id, win32con.WM_CHAR, 0x0000000D, 0x001C0001)
win32api.SendMessage(id, win32con.WM_KEYUP, 0x0000000D, 0x001C0001)
"""
