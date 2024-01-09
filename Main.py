#This program is dedicated to a recieving password and validating the stregnth of the password against a set of rules.

#ALGORITHM

#1. Get a username 
#2. Check if user in db 
#3. If in db, end program. Ifnot, add username to db
#4. Prompt passworod from user with displayed rules 
#5. Check password against rules 
#6. Give validation feedback to user 
#7. If not, prompt user for a stronger password 
#8. Give validation feedback to user 
#9. If not, repeat steps 5 and 6 
#10. If, say password is OK and add username and password to the db
#11. End program

import getpass #password function for command line usage
import sys #running python in the command line
import sqlite3 #store username data
import hashlib #hashing the password

def user_check(usrname): #user function
        #print(f"Parameter 1: {param1}") *DEBUG*
        #Make connection to db
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        
        #if the username is in the file do this
        #print(len(usrname)) *DEBUG*
        
        newName = (usrname,) #change len of the username to fit in parameterized query
        #print(len(newName)) *DEBUG*
        
        #literal sql query to test logic
        
        #cursor.execute("SELECT * FROM users WHERE Username = 'MickeyMouse'") *DEBUG*
        #rows = cursor.fetchall() *DEBUG*
        #for row in rows: *DEBUG*
            #print("LITERAL", row) *DEBUG*

        cursor.execute("SELECT * FROM users WHERE Username = ?", newName) #get data for username in the db
        rows = cursor.fetchall() #recall data
        if len(rows) ==1: #if there is data ...
            conn.close() #close connection
            return False #End Program
        else: 
            conn.close() #close connection
            return True #Request Password

        
def password_Strengthener(passW): #password function
    if 8 <= len(passW) <= 64:
        # Check for at least one uppercase, one lowercase, one digit, and one special character
        if any(char.isupper() for char in passW) and \
           any(char.islower() for char in passW) and \
           any(char.isdigit() for char in passW) and \
           any(char in "!@#$%^&*()-_+=,.?/:;{}[]~" for char in passW):
               return True
    return False

def write_to_db(usrname, password_hash):
    #open connection to db
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    #insert the username and hashed password
    cursor.execute("INSERT INTO users (Username, PassW_hash) VALUES (?, ?)", (usrname, password_hash))
    #commit and close the connection
    conn.commit()
    conn.close()
    return True

if __name__ == "__main__":
    
    if len(sys.argv) != 2: #far too many arguments? FYI to user
        print("Usage: python main.py username_Here")
    else:
        # Get command-line arguments
        usrname = sys.argv[1]

        
        if user_check(usrname): 
            print ("With username '"+ usrname +"'... Submit a password with the following requirements")
            print("\nLength: Between 8 and 64 characters \nspecial character:Use of at least one ie !@#$%^&*()-_+=,.?/:;{}[]~ \nUpper and Lowercase Characters: Use least one of each \nNumber: Use at least one")
            passW = getpass.getpass("Enter a strong password:") # get the password from the user using getpass
            if password_Strengthener(passW): #call the password function and save in DB
                password_hash = hashlib.sha256(passW.encode()).hexdigest()
                write_to_db(usrname, password_hash)
                print ("\n\nCongratulations "+ usrname + ", you are now in our system! Thanks for supporting!")
            else: #option to try again or terminate the program
                choice = input("That password does not meet the requirements, would you like to try again? Yes or no.")
                while choice == "yes" or choice == "Yes":
                    print("\n\nLength: Between 8 and 64 characters \nspecial character:Use of at least one ie !@#$%^&*()-_+=,.?/:;{}[]~ \nUpper and Lowercase Characters: Use least one of each \nNumber: Use at least one")
                    passW = getpass.getpass("\nEnter a strong password:") # get the password from the user, using getpass
                    if password_Strengthener(passW):
                        password_hash = hashlib.sha256(passW.encode()).hexdigest()
                        write_to_db(usrname, password_hash) #insert into appDB
                        choice = "no"
                        print ("\n\nCongratulations "+ usrname + ", you are now in our system! Thanks for supporting!")
                    else:
                        choice = input("That password does not meet the requirements, would you like to try again? Yes or no.")
                        
        else: #if the username is not in the file, produce this message
            print (usrname + " is already in our system! Thanks for supporting!")