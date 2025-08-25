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
    stdscr.nodelay(True)
    stdscr.clear()
    while True:

        system = (platform.system())
        platform22 = (platform.platform())
        platfr3 = (platform.release())
        os_name = (platform.system())
        networknoc = (platform.node())
        logical_c = (psutil.cpu_count(logical=True))
        logical_c2 = (psutil.cpu_count(logical=False))
        pltform = (platform.processor())
        cpu_stat = (psutil.cpu_stats())
        arch = (platform.machine())

        stdscr.addstr(1,1, f"Generic Name System: {system} ||Detailed string: {platform22}|| OS Version: {platfr3}")
        stdscr.addstr(2,1, f"OS NAME: {os_name}")
        stdscr.addstr(3,1, f"Network Name of the Computer: {networknoc}")
        stdscr.addstr(4,1, f"Number of Threads = {logical_c}")
        stdscr.addstr(5,1, f"Number of Processors = {logical_c2}")
        stdscr.addstr(6,1, f"Processor: {pltform}")
        stdscr.addstr(7,1, f"cpu stats: {cpu_stat}")
        stdscr.addstr(8,1, f"Machine: {arch}")


        stdscr.addstr(9,1, "Press q to exit")
        curses.doupdate()
        key1 = stdscr.getch()

        if key1 == ord('q'):
            stdscr.clear()
            break

#psutil
def cpu_monitor(stdscr): #this has writen by ai, and corrected for me, just, am new in this world of programming, sorry for that 
    stdscr.nodelay(True)
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    confirmation = False
    indic = 0
    scroll_offset = 0
    
#--- config for process---
    processes = sorted(
        psutil.process_iter(['pid', 'name', 'status', 'cpu_percent']),
        key=lambda p: p.info.get('cpu_percent', 0),
                reverse=True
    )[:10]

    while True:

        curses.doupdate()

        h, w = stdscr.getmaxyx()


        stdscr.addstr(1, 1, "Task Monitor", curses.color_pair(1))
        #---Monitor---
        cpu = psutil.cpu_percent(interval=0.5) 
        mem = psutil.virtual_memory().percent
        mem_available = f"{psutil.virtual_memory().available / (1024 ** 3):,.3f} GB"
        disk_usage = f"{psutil.disk_usage('/').percent}%"
        disk_free = f"{psutil.disk_usage('/').free / (1024 ** 3):,.3f} GB"

        stdscr.addstr(2, 1, f"CPU: {cpu}% || Memory: {mem}%")
        stdscr.addstr(3, 1, f"Avalaible Memory: {mem_available}")
        stdscr.addstr(4, 1, f"Disk Usage: {disk_usage}")
        stdscr.addstr(5, 1, f"Free Disk Space: {disk_free}")

        stdscr.addstr(h - 2, 1, "||UP Arrow and DOWN Arrow to Move || Q to exit")
        stdscr.addstr(h - 1, 1, "S to select|| K to kill processes" )

        # --- PROCESS ---
        y_pos = 2
        
        try:

            stdscr.addstr(y_pos, 40, "PID        Name                  Status     CPU % ", curses.A_BOLD)
            
            for i, proc in enumerate(processes):
                pid = proc.info.get('pid', 'N/A')
                name = proc.info.get('name', 'N/A')
                status = proc.info.get('status', 'N/A')
                cpu_percent = proc.info.get('cpu_percent', 'N/A')
                
                if isinstance(cpu_percent, (int, float)):
                    cpu_str = f"{cpu_percent:>5.1f}%"
                else:
                    cpu_str = " N/A "

                line_text = f"{pid:<10} {name:<22} {status:<11} {cpu_str}"
                
                if i == indic:

                    stdscr.addstr(y_pos + i + 1, 40, line_text, curses.color_pair(1) | curses.A_REVERSE)
                else:
                    
                    stdscr.addstr(y_pos + i + 1, 40, line_text, curses.color_pair(2))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            stdscr.addstr(y_pos + 1, 40, "Error: One or more processes could not be read.")

        key = stdscr.getch()
    

        if key == curses.KEY_UP:
            if indic > 0:
                indic -= 1
        elif key == curses.KEY_DOWN:

            if indic < len(processes) - 1:
                indic += 1

        elif key == ord('q'):
            stdscr.clear()
            break

        if key == ord('s'):
            processes_selected = processes[indic]
            selected_pid = processes_selected.info['pid']
            nameinfo = processes_selected.info['name']
            stdscr.addstr(13, 1, f"Selected PID: {selected_pid} Name: {nameinfo}")

        elif confirmation == False and key == ord('k'):
            stdscr.addstr(14,1, "are you sure you want to kill the process? Y/N:")
            confirmation = True
            selected_pid = processes[indic].info['pid']
            stdscr.addstr(15,1, f"Number of PID: {selected_pid}")

        elif confirmation == True and key == ord('y'):
            psutil.Process(selected_pid).kill()
            confirmation = False
            stdscr.clear()
                  
        elif confirmation == True and key == ord('n'):
            confirmation = False
            stdscr.clear()
                

#First Menu

def monitor_menu(stdscr):
    stdscr.nodelay(True)
    stdscr.clear()
    while True:
        
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