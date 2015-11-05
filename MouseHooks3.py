__author__ = 'Administrator'
import pythoncom, pyHook,win32api,win32con

def OnMouseEvent(event):
    # called when mouse events are received
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print 'Injected:',event.Injected
    print '---'


def onclick(event):
    print 'Mouse click!'
    return True

# return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
#hm.MouseAll = OnMouseEvent
hm.MouseLeftDown = onclick
# set the hook
hm.HookMouse()
# wait forever
pythoncom.PumpMessages()
