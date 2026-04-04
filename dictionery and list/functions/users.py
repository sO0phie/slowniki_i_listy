from random import randint

def generate_unique_id(data: list[dict]) -> int:
    lst_id = []
    for user in data:
        lst_id.append(user.get("id"))
    new_id = randint(1, 1000000)
    while new_id in lst_id:
        new_id = randint(1, 1000000)
    return new_id

def add_new_user(data: list[dict])-> dict:
    return {
        "id": generate_unique_id(data),
        "name": input("Enter name: ").strip().lower() or None,
        "surname":input("Enter surname: ").strip().lower() or None,
        "date of birth":input("date of birth: ").strip().lower() or None,
        "grades mathematics": add_or_remove_grades(data),
        "grades polish": [], 
        "grades english":[]        
    }
    
def add_or_remove_grades(data: list[dict])-> None:
    oceny = []
    id = int(input("ID użytkownika --- "))
    for user in data:
        if user["id"] == id:
            choice = input("a - dodanie oceny, b - usunięcie")
            if choice == "a":
                subject:str = input("m - matematyka, p - polski, a - angielski")
                if subject == "m":
                    ocena = int(input("Podaj ocenę z matematyki: "))
                    user["grades mathematics"].append(ocena)
                elif subject == "p":
                    ocena = int(input("Podaj ocenę z polskiego: "))
                    user["grades polish"].append(ocena)
                elif subject == "a":
                    ocena = int(input("Podaj ocenę z angielskiego: "))
                    user["grades english"].append(ocena)
                else:
                    print("Nieprawidłowy przedmiot")
        else:
            pass
        


