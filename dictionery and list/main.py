from functions import data
from functions import users
import os
import time 

def program_menu()->None:
        print(
    """
    ================================================
    \n
    e - exsit
    w - add user
    r - data inf
    t - add/remove user's grades
    y - find user by ID
    u - find user by name
    i - delete user by ID
    u - update user's name
    k - update user's surname
    l - update user's birth date
    \n
    ================================================
    """)


def main(): 
    loaded_data:list[dict] = data.read_data()
    while True:
        program_menu()
        inp = input("- ").lower().strip()
        if inp == "e":
            print("The program has finished running")
            data.save_data(loaded_data)
            break
        elif inp == "w":
            new_user = users.add_new_user(loaded_data)
            loaded_data.append(new_user)
            data.save_data(loaded_data)
        elif inp == "r":
            data.print_all_data(loaded_data)
        elif inp == "t":
            users.add_or_remove_grades(loaded_data)
        elif inp == "y":
            user_id = int(input("Wpisz ID użytkownika "))
            users.find_user_by_id(loaded_data, user_id)
        elif inp == "u":
            name = str(input("Wpisz imię użytkownika: "))
            users.find_users_by_name(loaded_data, name)
        elif inp == "i":
            user_id = int(input("Wpisz ID użytkownika "))
            users.delete_user_by_id(loaded_data, user_id)
        elif inp == "o":
            user_id = int(input("Wpisz ID użytkownika "))
            new_name = str(input("Wpisz nowe imię użytkownika "))
            users.update_user_name(loaded_data, user_id, new_name)
        elif inp == "k":
            user_id = int(input("Wpisz ID użytkownika "))
            new_surname = str(input("Wpisz nowe nazwisko użytkownika "))
            users.update_user_surname(loaded_data, user_id, new_surname)
        elif inp == "l":
            user_id = int(input("Wpisz ID użytkownika "))
            new_birth_date = str(input("Wpisz nową datę urodzenia użytkownika "))
            users.update_user_birth_date(loaded_data, user_id, new_birth_date)
        elif inp == "m":
            pass
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("There is no such command")
            time.sleep(2)


if __name__ == '__main__':
    main()
