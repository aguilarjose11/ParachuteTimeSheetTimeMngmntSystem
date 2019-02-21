# TSTools.py module for tools used in timesheet.py
try:
    from pyautogui import typewrite
    autogui = True
except (ImportError, KeyError):
    import readline
    autogui = False
try:
    from ctypes import windll, create_string_buffer
    CTYPES_IMPORTED = True
except (ImportError, KeyError):
    CTYPES_IMPORTED = False


def getcmdxandy():
    if(CTYPES_IMPORTED):
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            import struct
            (bufx, bufy, curx, cury, wattr,
            left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
        else:
            sizex, sizey = 80, 25 # can't determine actual size - return default values
        return sizex, sizey
    else:
        return -1


# Getch() replacement
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


# getch for linux
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


# getch for windows.
class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
