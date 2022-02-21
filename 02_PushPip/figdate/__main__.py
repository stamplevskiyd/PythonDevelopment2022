import sys
import time
import pyfiglet

def date(format='%Y %d %b %A', fnt='graceful'):
    time_str = pyfiglet.Figlet(font=fnt)
    return time_str.renderText(time.strftime(format, time.gmtime()))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(date())
    elif len(sys.argv) == 2:
        print(date(sys.argv[1]))
    else:
        print(date(sys.argv[1], sys.argv[2]))