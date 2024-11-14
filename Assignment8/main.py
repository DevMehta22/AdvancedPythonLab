import hashlib;
import re;
import logging

logging.basicConfig(filename='users.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def is_valid_username(username):
    if len(username.strip())==0:
        logging.warning('Invalid username: '+username)
        return False 
    else:
        return True

def is_valid_password(password):
    if len(password)<8:
        return False
    elif not re.match('[a-zA-Z0-9_]',password):
        logging.warning('password should include small, capital letters and numbers')
        return False
    else:
        return True

def signup(username,password):
    if (not is_valid_username(username)) or (not is_valid_password(password)):
        logging.warning(f"Signup attempt failed for username: {username}")
        return "Invalid username or password"
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open('user_data.txt','a') as fp:
            fp.write(username+":"+hashed_password)
            fp.write("\n")

        fp.close()
        logging.info(f"User '{username}' registered successfully.")
        return  "User Registered successfully"
    except FileNotFoundError:
        logging.error("Failed to write to user_data.txt")
        return "Error: Unable to write to file"


def login(username,password):
    if (not is_valid_username(username)) or (not is_valid_password(password)):
        logging.warning(f"Login attempt failed for username: {username} due to invalid credentials.")
        return "Invalid username or password"
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open('user_data.txt','r') as fp:
            for line in fp:
                stored_username,stored_password = line.strip().split(':')
                if stored_username == username and stored_password == hashed_password:
                    logging.info(f"User '{username}' logged in successfully.")
                    fp.close()
                    return "Login successfull"
                
            logging.warning(f"Login failed for username: {username} due to incorrect password.")
            fp.close()
            return "Username or password is Incorrect"
            
    except FileNotFoundError:
        logging.error("Failed to read from user_data.txt")
        return "Error: Unable to read from file"

if __name__ == "__main__":
    print("Name: Dev Mehta\nRoll No: 22BCP282")
    while(True):
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print(signup(username,password))
            
        elif choice == 2:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print(login(username,password))
        elif choice == 3:
            logging.info("Program exited by the user.")
            break
        else:
            logging.warning(f"Invalid menu choice: {choice}")
            print("Invalid choice")

        
    
    