#!/usr/bin/env python
# encoding=utf-8

from controller.Core import Core
import signal 

#reference: https://stackoverflow.com/questions/18114560/python-catch-ctrl-c-command-prompt-really-want-to-quit-y-n-resume-executi/18115530
def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)
    try:
        if input("\n[~] Really quit? (Y/n)> ").lower().startswith('y'):
            exit(1)
    except KeyboardInterrupt:
        print("Ok ok, quitting")
        exit(1)
    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == "__main__":
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    
    __core = Core()
