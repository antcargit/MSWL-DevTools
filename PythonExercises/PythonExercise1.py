#!/usr/bin/python
# ===NAME===
#    PythonExercise1.py
# ===DESCRIPTION===
#    Python script that reads the contents of the passwd file (/etc/passwd) and
#    prints the shell used by every username
# ===LASTS MODIFICATIONS===
#	 12/09/2011: Creation Antonio Carmona
# =========================

import sys, os, string

def getUserList():
   if os.path.exists("/etc/passwd"):
        passwdFile=open("/etc/passwd","r")
        for line in passwdFile:
            line=line.rstrip()   # Erase the \n
            fields=line.split(":")
            targetUser=fields[0]
            targetShell=fields[6]                
            print targetUser+" -> "+targetShell


getUserList()


        