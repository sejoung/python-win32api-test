__author__ = 'sanaes'
import pythoncom, pyHook

def OnKeyboardEvent(event):
  # block only the letter A, lower and uppercase
  return (event.Ascii not in (ord('a'), ord('A')))

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()