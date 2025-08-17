import psutil, curses
import time, warnings
import psutil
import sys
import os
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
print("all of this is false, so, ignore this")
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

#psutil
def cpu_monitor(stdscr):
    stdscr.clear()

    while True:
        stdscr.clear()
        cpu = (psutil.cpu_percent(interval=0.5))
        mem = (psutil.virtual_memory().percent)

        stdscr.addstr(1, 1,f"CPU: {cpu}% | Memory: {mem}%")
        stdscr.addstr(3, 1, "presiona 'q' para salir")
        stdscr.refresh()
            
        key1 = stdscr.getch()
        if key1 == ord('q'):
            break

def monitor_menu(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(1, 1, "1: Monitor")
        stdscr.addstr(2,1,"2: Exit program")
        stdscr.refresh()
        time.sleep(0.5)
        key01 = stdscr.getch()
        
        if key01 == ord('1'):
            cpu_monitor(stdscr)
        elif key01 == ord('2'):
            break
        else:
            os.system('clear')
            stdscr.addstr(1,0, "Invalid, try another one")
            stdscr.refresh()
            stdscr.getch()     

def main(stdscr):
    animation(stdscr)
    monitor_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
    os.system('clear')