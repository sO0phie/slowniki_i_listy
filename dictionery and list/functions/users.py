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
    
def add_or_remove_grades(data: list[dict])->None:
    ocena = int(input("Ocena: "))
    data.append(ocena)
    if len(data) > 0:
        inp = input("Czy usunąć jakąś ocenę? ")
        if inp == "tak":
            print(data)
            data.pop(input("Ocena do usunięcia: "))
        elif inp == "nie":
            pass
        else:
            print("Nie ma takiej komendy")
    # The function allows you to modify a given student's grades




