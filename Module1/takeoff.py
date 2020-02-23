from tello import Tello
import sys
from datetime import datetime
import time

start_time = str(datetime.now())
file_name = sys.argv[1]

print 'message received'

f = open(file_name, "r")
commands = f.readlines()

tello = Tello()
for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()

        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print 'delay %s' %sec 
            time.sleep(sec)
            pass
        else :
            tello.send_command(command)