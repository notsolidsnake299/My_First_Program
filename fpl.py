import psutil, curses
import time, warnings
import platform
from sys import argv
import os, datetime
from curses import wrapper

print("Loading sysmigu...")
time.sleep(3)
print("Ok...")
time.sleep(0.3)
print("Loading Vocaloid...")
time.sleep(3)
print("Ok...")
time.sleep(0.3)
print("Loading Encryptation...")
time.sleep(3)
print("Ok...")
time.sleep(0.3)
print("Loading Animations...")
time.sleep(3)
print("Ok...")
time.sleep(0.3)
print("all of this is fake, so, ignore this")
time.sleep(2)

#asciiwelcome art
open = ("   /\\_/\\ ", "   (o.o) ", "   > ^ < ")

closed = ("   /\\_/\\ ", "   (-.-) ", "   > ^ < ")

warnings.filterwarnings("ignore", category=SyntaxWarning) 

def animation(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    frames = [open, closed]
    blink_ms = 600
    i = 0
    last = time.monotonic()

    while True:
        stdscr.erase()

        h, w = stdscr.getmaxyx()
        frame = frames[i]
        y = max((h - len(frame)) // 2 - 1, 0)
        x = max((w - len(frame[0])) // 2, 0)
        for j, line in enumerate(frame):
            try:
                stdscr.addstr(y + j, x, line[:w - x])
            except curses.error:
                pass

        msg = "Press any key to begin:"
        try:
            stdscr.addstr(h - 2, max((w - len(msg)) // 2, 0), msg)
        except curses.error:
            pass

        stdscr.refresh()

        if (time.monotonic() - last) * 1000 >= blink_ms:
            i ^= 1
            last = time.monotonic()

        key = stdscr.getch()
        if key != -1:
            break 

        time.sleep(0.01)

#Platform
def system_settings(stdscr):
    stdscr.clear()

    while True:
        system = (platform.system(),  platform.platform())
        networknoc = (platform.node())
        stdscr.addstr(1,1, f"System: {system} || {networknoc}")
        stdscr.addstr(3,1, "Press q to exit")
        curses.doupdate()
        window.addstr()
        key1 = stdscr.getch()
        if key1 == ord('q'):
            break

#psutil
def cpu_monitor(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    stdscr.clear()

    while True:
        
        curses.doupdate()

        cpu = (psutil.cpu_percent(interval=0.5))
        mem = (psutil.virtual_memory().percent)
        mem_available = (f"{psutil.virtual_memory().available/(1024**3):,.3f} GB")
        disk_usage = (f"{psutil.disk_usage('/').percent}%")
        disk_free = f"{psutil.disk_usage('/').free/(1024**3):,.3f} GB"
        stdscr.addstr(1, 1, "Task Monitor", curses.color_pair(1))
        stdscr.addstr(2, 1,f"CPU: {cpu}% || Memory: {mem}%")
        stdscr.addstr(3, 1, f"Avalaible Memory: {mem_available}")
        stdscr.addstr(4, 1,f"Disk Usage: {disk_usage}")
        stdscr.addstr(5, 1, f"Free Disk Space: {disk_free}")
        stdscr.addstr(6, 1, "press q to exit")
            
        key1 = stdscr.getch()
        if key1 == ord('q'):
            stdscr.clear()
            break

def monitor_menu(stdscr):
    stdscr.clear()
    while True:

        stdscr.addstr(9, 50,f"Time System Startup: {startupsys} seconds")
        stdscr.addstr(1, 1, "1: Monitor")
        stdscr.addstr(2,1, "2: System Info")
        stdscr.addstr(3, 1,"3: Exit program")
        curses.doupdate()
        time.sleep(1)
        key01 = stdscr.getch()
        
        if key01 == ord('1'):

            cpu_monitor(stdscr)

        if  key01 == ord('2'):

            system_settings(stdscr)

        elif key01 == ord('3'):

            break

def main(stdscr):
    animation(stdscr)
    monitor_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
    os.system('clear')
