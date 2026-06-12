import random   
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def password_generator(): 
    while True:
        clear()
        
        print("===================================")
        print("        PASSWORD GENERATOR         ")
        print("===================================")
        print("")
        print("")
        print("yes - generate a password")
        print("no - exit the password generator")
        choice = input("Enter your choice: ")
        
        if choice.lower() == "yes":
            try:
                length = int(input("Enter the desired password length: "))                  
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            
            if length < 1:
                print("Password length must be at least 1.")
                time.sleep(2)
                continue
            elif length > 100:
                print("Password length is too long. Please enter a number less than or equal to 100.")
                time.sleep(2)
                continue

            # --- YOUR BETTER LOGIC ---
            characters = ""
            include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
            include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
            include_numbers   = input("Include numbers? (yes/no): ").lower() == "yes"
            include_special   = input("Include special symbols? (yes/no): ").lower() == "yes"

            if include_lowercase:
                characters += "abcdefghijklmnopqrstuvwxyz"
            if include_uppercase:
                characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if include_numbers:
                characters += "0123456789"
            if include_special:
                characters += "!@#$%^&*()"

            if characters == "":
                print("You must select at least one character type.")
                time.sleep(2)
                continue   # Go back to the start of the loop

            generated_password = "".join(random.choice(characters) for _ in range(length))
            print(f"\nGenerated password: {generated_password}")
            input("Press Enter to continue...")
            clear()

        elif choice.lower() == "no":
            goodbye()
            break
        
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            time.sleep(2)
            clear()

def goodbye():
    print("Exiting the program.")
    time.sleep(2)
    clear()

def github():
    print("GitHub link: https://github.com/tbbaker-lab")

def mainmenu():
    while True:
        clear()  
        print("===================================")
        print("        PASSWORD GENERATOR         ")
        print("===================================")
        print("(1) password generator")
        print("(2) github link")
        print("(3) exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            clear()
            password_generator()
        elif choice == "2":
            clear()
            github()
            input("Press Enter to continue...")
            clear()
        elif choice == "3":
            clear()
            goodbye()
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            time.sleep(2)

if __name__ == "__main__":
    mainmenu()