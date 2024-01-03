#This program is dedicated to a recieving password and validating the stregnth of the password against a set of rules.

#ALGORITHM

#1. Get a username 
#2. Check if user in file 
#3. If not, add username to file 
#4. Prompt passworod from user W displayed rules 
#5. Check password against rules 
#6. Give validation feedback to user 
#7. If not, prompt user for a stronger password 
#8. Give validation feedback to user 
#9. If not, repeat steps 5 and 6 
#10. If, say password is OK
#11. End program

import getpass #password function for command line usage
import sys #running python in the command line

def user_check(usrname): #user function
        #print(f"Parameter 1: {param1}") *DEBUG*
        if len(usrname) == 5: #check if username is stored in a file
            return True
        else: 
            return False 
        
def password_Strengthener(passW): #password function
    print(passW) #Add logic for password, maybe recursive function
        
if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python myscript.py <param1>")
    else:
        # Get command-line arguments
        usrname = sys.argv[1]

        # Call the main function with the provided arguments
        if user_check(usrname): #if the username is in the file do this
            print ("DONT")
        else: #if the username is not in the file, produce this message
            print (usrname + " not found. Try again.")