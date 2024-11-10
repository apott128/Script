import getpass
import hashlib
import string as s

password_manager = {}


#create the menu

def menu():
    print('welcome')
    print('option 1 Add Username,password,url')
    print('option 2 View Stored Credentials')
    print('option 3 Exit')
    return input("Choose an option:")

def create_account ():
    Username = input ('create username')
    password = getpass.getpass ('enter password')
    hashed_password = hashlib.sha256 (password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print('Account created')



def create_login ():
    username = ('enter username')
    password = getpass.getpass('enter password')
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if password_manager.keys in password_manager[username] == hashed_password:
        print('login successfull')
    else:
        print('invalid username or password')

    
            

while True:


    #display menu options
    menu()

    #ask user for input
    choice = input ("Please choose an option:")

    #check if statement work
    if choice == '1':
        #if == 1 ask for input and save to file
        Username = input('enter username')
        encrypted_pass = input('enter password')
        url = input('enter url')

        print(f"your username is {Username} your password is {encrypted_pass} your selected website is {url}")

        #save to file
        with open('Digi.txt','a') as file:
            file.write(f'{Username},{encrypted_pass},{url}\n')
            print("information has been saved")


    elif choice == '2':
        #if == 2 read content of file
        print("\nUsers Credentials")
        print(f'{"username":<20} | {"password":<20} | {"url"}')
        print("=" * 65)

        with open('Digi.txt','r') as file:
            for line in file:
                Username,Password,url = line.strip().split(',')
                print(f'{Username:<20} | {Password:<20} | {url:<20}\n')
            

    elif choice == '3':
        print("You selected option 3, Bye Bye")   
        break
        
    #if = 1
    #ask for input and save file

    #if == 2 read content file

    #exit
