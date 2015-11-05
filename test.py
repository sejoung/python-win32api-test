import ctypes

SetCursorPos = ctypes.windll.user32.SetCursorPos
mouse_event = ctypes.windll.user32.mouse_event

def left_click(x, y, clicks=1):
  SetCursorPos(x, y)
  for i in xrange(clicks):
   mouse_event(2, 0, 0, 0, 0)
   mouse_event(4, 0, 0, 0, 0)


left_click(20, 650)
