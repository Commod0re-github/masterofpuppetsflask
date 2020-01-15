#--------------------------------------------------#
#               MASTER OF PUPPETS                  #
#                 v. 0.0.1 InDev                   #
#                                                  #
#                  written by                      #
#                                                  #
#                  Commod0re                       #
#                                                  #
#--------------------------------------------------#

          ATTENTION! USE THIS PROGRAM ONLY FOR EDUCATIONAL PURPOSES
          
AUTHOR OF SOFTWARE REJECT ANY RESPONSIBILITY OF OCCURED DAMAGE FROM THIS PROGRAM

                PROGRAM USE GPLv3 LICENSE AND CANT BE STOLEN
               



                               USER GUIDE
                             
1. Setup C&C
   
    C&C have HTTP-API to contact with master and give commands to puppets
            /puppetsapi  returns you command, given by master
            /adminapi  takes command from master
            
    CONFIGURE PASSWORD! IN SERVER.PY CONFIG! SET A STRONG PASSWORD!
    
2. Setup Commander

    Commander comfortably works with admin-api of C&C
    
    Open program text and change ADMINPASSWORD password to acess admin-api in config, the same as C&C have in config
    
    Set C&C host and port in ADMINSERVER
    
3. Setup Puppet

    Puppet is a your soilder, takes command from C&C API
    
    Open program text amd change COMMANDSERVER to IP adress or dns-name of C&C and http-port
    
    TIME_SLEEP is how long puppet wait to ask command from C&C in seconds
    

#---------ATTENTION---------#

Launch server.py first, than launch ONLY commander.py, give command "WAIT" or other. And only after that launch puppet.py!

#---------------------------#

Commands:
    WAIT - just wait for your command
    STOPALL - stop all
    slowloris - slowloris HTTP-DDoS
    
    other don't wort, in develop

Server requires modules:
    Flask
    Logging

Commander requiers modules:
    colorama
    pyfiglet
    requests

Puppet requires modules:
    requests
    time
    os    
    
    
    
This project is now experemental, and doesn't have any protection and huge functionality, project is developing now, and in future will be have good functionality

If you professional python-developer, and you want to help me, found some bugs or bad practice, write me in github repository error or in email j4s0n4l3rt@gmail.com 

Software works only on linux and can't be like malvare, it requires python and libraries, you can launch it in your hosts only! 

This program uses Git! 


    
By the way, author is 14-years old ukrainian, Slava Ukraine!.


                                               ##################################### 
                                               #####################################
                                               #####################################
#                                              #####################################
#                                              #####################################
#                                              #####################################

(At least,  my editor displays it looks like ukrainian flag (Pluma text editor))

OBEY YOUR MASTER! 
