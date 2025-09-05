#  Create a dictionary (phonebook) with numbers as keys and names as values
phone = {
    "01275321645": "abdo",
    "01275321598": "ayman",
    "01245312794": "sayed",
    "01254697234": "nour"
}

#  Function to check if the number is valid (must be 11 digits and only numbers)
def is_valid_number(number):
    if len(number) != 11:
        return False
    for x in number :
        if x < "0" or x > "9" :
            return False
    return True

#  Function to find a name by phone number
def find_name_by_number ():
    num = input ("enter a number: ")
    if is_valid_number(num):  # Check if the number is valid
            for n in phone:   # Loop through the phonebook
                if num == n :
                    print (phone[n])  # Print the name if found
                    return
            print ("not found")  # Number not found
    else:
        print ("this is invalid number: ")

#  Function to find a phone number by name
def find_number_by_name ():
    name = input ("enter a name: ")
    for number, owner in phone.items():  # Loop through dictionary items
        if name == owner :
            print (number)  # Print the number if found
            return 
    print("sorry, not defind: ")  # Name not found

#  Function to add a new contact to the phonebook
def add_new_contact():
    new_name = input ("enter a name: ")
    new_number = input ("enter a number: ")
    if is_valid_number(new_number):   # Check if the number is valid
        phone[new_number] = new_name  # Add new contact
        print ("succesfuly")
    else:
        print ("invalid number: ")

#  Function to display the main menu
def choose():
    print (""" 
                        this is your phone number:

        1: find name by number.
        2: find number by name.
        3: add new contact.
        4: show all contact.
    """)

#  Start of the program
king = input ("you have phone list. open? (yes or no): ")

#  Loop while the user wants to use the phonebook
while king in ["yes", "y"]:
    choose()  # Show menu
    user_choose = input("enter a (1, 2, 3, 4); ")

    #  Option 1: Find name by number
    while user_choose == "1" or user_choose in ["y", "yes"]:
        find_name_by_number()
        user_choose=input("try again? ")
        if user_choose in ["y", "yes"]:
            pass
        elif user_choose in ["n", "no"]:
            king = input ("go to home? (yes or no) ")
            if king == ["no", "n"]:  # ⚠️ Small mistake here, but not changed
                break
            elif king in ["yes", "y"]:
                pass
            else:
                while king not in ["yes", "y"] and king not in  ["no", "n"]:
                    print ("please enter (yes or no)")
                    king = input ("go to home? (yes or no) ")
        else:
            while user_choose not in ["yes", "y"] and user_choose not in  ["no", "n"]:
                    print ("please enter (yes or no)")
                    user_choose = input ("try again (yes or no) ")

    #  Option 2: Find number by name
    while user_choose == "2" or user_choose in ["y", "yes"]:
        find_number_by_name()
        user_choose=input("try again? ")
        if user_choose in ["y", "yes"]:
            pass
        elif user_choose in ["n", "no"]:
            king = input ("go to home? (yes or no) ")
            if king in ["no", "n"]:
                break
            elif king in ["yes", "y"]:
                pass
            else:
                while king not in ["yes", "y"] and king not in  ["no", "n"]:
                    print ("please enter (yes or no)")
                    king = input ("go to home? (yes or no) ")
        else:
            while user_choose not in ["yes", "y"] and user_choose not in  ["no", "n"]:
                    print ("please enter (yes or no)")
                    user_choose = input ("try again? (yes or no) ")

    #  Option 3: Add a new contact
    while user_choose == "3" or user_choose in ["y", "yes"]:
        add_new_contact()
        user_choose=input("try again? ")
        if user_choose in ["y", "yes"]:
            pass
        elif user_choose in ["n", "no"]:
            king = input ("go to home? (yes or no) ")
            if king in ["no", "n"]:
                break
            elif king in ["yes", "y"]:
                pass
            else:
                while king not in ["yes", "y"] and king not in  ["no", "n"]:
                    print ("please enter (yes or no)")
                    king = input ("go to home? (yes or no) ")
        else:
            while user_choose not in ["yes", "y"] and user_choose not in  ["no", "n"]:
                    print ("please enter (yes or no)")
                    user_choose = input ("try again? (yes or no) ")
    
    #  Option 4: Show all contacts
    while user_choose == "4" or user_choose in ["yes", "y"]:
        for k, v in phone.items():  # Print all numbers and names
            print (k, v)
        user_choose = input ("do you want try again? ")
        if user_choose in ["no", "n"]:
            king = input ("go to home? ")
            if king in ["no", "n"]:
                break
            elif king in [ "yes", "y"]:
                pass
            else:
                while king not in ["yes", "y"] and king not in  ["no", "n"]:
                    print ("please enter (yes or no)")
                    king = input ("go to home? (yes or no) ")
        elif user_choose in ["yes", "y"]:
            pass
        else:
            while user_choose not in ["yes", "y"] and user_choose not in  ["no", "n"]:
                    print ("please enter (yes or no)")
                    user_choose = input ("try again? (yes or no) ")
else:
    #  Exit message if the user chooses not to open the phonebook
    print ("okay, have a nice time: ")
