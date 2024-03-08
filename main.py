import json, keyboard, traceback, threading
from pystray import Icon, Menu, MenuItem
from win11toast import toast
from PIL import Image

from yeeter import Yeeter

def thread(func):
    threading.Thread(target=func, daemon=True).start()

def enable_hotkeys(config):
    keyboard.add_hotkey(config["hotkeys"]["yeet"], yeeter.yeet, suppress=True)#
    keyboard.add_hotkey(config["hotkeys"]["yeet_all"], yeeter.yeet_all, suppress=True)
    keyboard.add_hotkey(config["hotkeys"]["unyeet"], yeeter.unyeet, suppress=True)
    keyboard.add_hotkey(config["hotkeys"]["unyeet_all"], yeeter.unyeet_all, suppress=True)

yeeter = Yeeter()

def runner():
    try:
        keyboard.remove_all_hotkeys()
    except:
        pass

    config = {}
    with open("config.json", "r+") as raw_config:
        config = json.load(raw_config)
    
    enable_hotkeys(config)
    thread(lambda: toast("Tray Yeeter has settled in (。・ω・。)", f"Yeet current active window: [{config['hotkeys']['yeet'].upper()}]\nUnyeet latest window: [{config['hotkeys']['unyeet'].upper()}]\nYeet everything: [{config['hotkeys']['yeet_all'].upper()}]\nUnyeet everything: [{config['hotkeys']['unyeet_all'].upper()}]"))

try:
    runner()

    icon = Icon("tray yeeter",
                        icon=Image.open("icon.png"), menu=Menu(
                            MenuItem("Reload", runner)
                        ))
    icon.run()
except:
    stack = traceback.format_exc()
    print(stack)
    thread(lambda: toast("Tray Yeeter can't initialize hotkeys ⊙﹏⊙∥", stack))