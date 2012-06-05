#!/usr/bin/python
# ===NAME===
#    PythonExercise2.py <username>
# ===DESCRIPTION===
#    Show the shell used by a given user. The shell used by every username should be stored in a dictionary, and the user-
#    name of which you want to get the shell will be provided as a command line argument.
#    You should handle possible errors like invalid user names or even if no user name is provided.
# ===LASTS MODIFICATIONS===
#	 12/09/2011: Creation Antonio Carmona
# =========================
import sys, os, string

def getUserList(userList):
	if os.path.exists("/etc/passwd"):
		passwdFile=open("/etc/passwd","r")
        for line in passwdFile:
            line=line.rstrip()   # Erase the \n
            fields=line.split(":")
            userList[fields[0]]=fields[6]
        return userList               
            	
if len(sys.argv) <= 1:
    print "ERROR: you must indicate a user name."
    exit()    
    
inputUser = sys.argv[1]
userList={}
userList=getUserList(userList)

try:
   print "Shell used by "+inputUser+" is "+userList[inputUser]
except KeyError, error:
   print "User: "+inputUser+" does not exist."






