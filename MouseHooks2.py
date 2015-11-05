import os
import pyHook
import pythoncom
import threading

# Kills the process if escape is pressed
class EscapeToKill(threading.Thread):
    
    def run(self):
        
        def onKeyboardEvent(event):
            asciiEscapeKey = 27
            if event.Ascii == asciiEscapeKey:
                os._exit(0)
            return True

        hm = pyHook.HookManager()
        hm.KeyDown = onKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()

# Gets global input
class GlobalInput():

    def getMousePos(self):
        self.Active = True
        self.position = None
        
        def onclick(event):
            if( self.Active ):
                self.position = event.Position
            return True        

        hm = pyHook.HookManager()
        hm.SubscribeMouseAllButtonsDown(onclick)
        hm.HookMouse()
        hm.HookKeyboard()   # hm.UnhookMouse throws an error otherwise
        while self.position == None:
            pythoncom.PumpWaitingMessages()
        hm.UnhookMouse()
        hm.UnhookKeyboard()
        self.Active = False
        return self.position
        
    def getKey(self):
        self.Active = True
        self.key = None        
        
        def onKeyboardEvent(event):
            if( self.Active ):
                self.key = event.Ascii
            return True        

        hm = pyHook.HookManager()
        hm.KeyDown = onKeyboardEvent
        hm.HookMouse()  # hm.UnhookMouse throws an error otherwise
        hm.HookKeyboard()
        while self.key == None:
            pythoncom.PumpWaitingMessages()
        hm.UnhookMouse()
        hm.UnhookKeyboard()
        return self.key      

if __name__ == "__main__":   
    t = GlobalInput()
    
    print "Click Mouse, print position: "
    print t.getMousePos()
    
    print "Press Key, print key's ascii code: "
    print t.getKey()

    print "Click Mouse, print position: "
    print t.getMousePos()
    
    print "Press Escape Key to Kill Process: "
    t2 = EscapeToKill()
    t2.start()