import win32gui, win32process, psutil
import win32.lib.win32con as win32con

class Yeeter:
    yeeted_windows = []

    def yeet(self):
        try:
            hwnd = win32gui.GetForegroundWindow()
            self.yeeted_windows.append(hwnd)

            win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        except:
            pass
    
    def yeet_all(self):
        try:
            windows = self.get_all_windows()
            self.yeeted_windows.extend(windows)

            for hwnd in windows:
                win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        except:
            pass

    def unyeet(self):
        try:
            hwnd = self.yeeted_windows.pop()
            win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        except:
            pass
    
    def unyeet_all(self):
        try:
            for hwnd in self.yeeted_windows:
                win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
            
            self.yeeted_windows.clear()
        except:
            pass
    
    def destroy_yeeted(self):
        try:
            for hwnd in self.yeeted_windows:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                process = psutil.Process(pid)
                process.terminate()
            
            self.yeeted_windows.clear()
        except:
            pass
        
    def get_all_windows(self):
        try:
            windows = []

            def callback(hwnd, ctx):
                if win32gui.IsWindowVisible(hwnd):
                    windows.append(hwnd)
            win32gui.EnumWindows(callback, None)

            return windows
        except:
            pass