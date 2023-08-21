import shutil
import time
import sys

# CHANGE PER SYSTEM

pro_loc = "C:\\Users\\YOUR_USER\\Saved Games\\Respawn\\Apex\\profile\\profile.cfg"
set_loc = "C:\\Users\\YOUR_USER\\Saved Games\\Respawn\\Apex\\local\\settings.cfg"

player1 = "YOUR_PLAYER_1"
player2 = "YOUR_PLAYER_2"

# Check current user
current_txt = open("current.txt", "r")
current_user = current_txt.read()
current_txt.close()

# LOOOOOP
while True:
    
    # Ask if user should be swapped
    print("Current user is:", current_user)
    swp = input("Would you like to swap user? (y/n): ")

    # Program runs if 'y'
    if swp == "y":
        
        # Tell the program who next_user is
        if current_user == player1:
            next_user = player2
        elif current_user == player2:
            next_user = player1
        else:
            print("Something went wrong...")
            time.sleep(2)
            sys.exit()

        # Move current profile.cfg to cfg_store
        copyname = "cfg_store\\profile_" + current_user + ".cfg"
        shutil.move(pro_loc, copyname)
        print("profile.cfg backed up.")
        # Move backup profile.cfg to Apex folder
        copyname = "cfg_store\\profile_" + next_user + ".cfg"
        shutil.copy(copyname, pro_loc)
        print("profile.cfg replaced.")

        # Move current settings.cfg to cfg_store
        copyname = "cfg_store\\settings_" + current_user + ".cfg"
        shutil.move(set_loc, copyname)
        print("settings.cfg backed up.")
        # Move backup settings.cfg to Apex folder
        copyname = "cfg_store\\settings_" + next_user + ".cfg"
        shutil.copy(copyname, set_loc)
        print("settings.cfg replaced.")
        
        # Change current.txt to represent user change
        current_txt = open("current.txt", "w")
        current_txt.write(next_user)
        current_txt.close()
        current_user = next_user
        print("User swapped.")

    # Program closes if 'n'  
    elif swp == "n":
        print("Program will close...")
        time.sleep(2)
        sys.exit()

    # Program loops otherwise
    else:
        print("Invalid input.")

    print()






    
