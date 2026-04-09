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
        "grades mathematics": [],
        "grades polish": [], 
        "grades english":[]        
    }
    
def add_or_remove_grades(data: list[dict])-> None:
    id = int(input("ID użytkownika --- "))
    for user in data:
        if user["id"] == id:
            choice:str = input("a - dodanie oceny, b - usunięcie")
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
            elif choice == "b":
                subject:str = input("m - matematyka, p - polski, a - angielski ")
                if subject == "m":
                    print(f' Oceny z matematyki {user.get("grades mathematics")}')
                    ocena = int(input("Którą ocenę chcesz usunąć? "))
                    if ocena in user.get("grades mathematics"):
                        user["grades mathematics"].remove(ocena)
                    else:
                        print("Nie ma takiej oceny")
                elif subject == "p":
                    print(f' Oceny z polskiego {user.get("grades polish")}')
                    ocena = int(input("Którą ocenę chcesz usunąć? "))
                    if ocena in user.get("grades polish"):
                        user["grades polish"].remove(ocena)
                    else:
                        print("Nie ma takiej oceny")
                elif subject == "a":
                    print(f' Oceny z angielskiego {user.get("grades english")}')
                    ocena = int(input("Którą ocenę chcesz usunąć? "))
                    if ocena in user.get("grades english"):
                        user["grades english"].remove(ocena)
                    else:
                        print("Nie ma takiej oceny")
                else:
                    print("Nie znaleziono takiej komendy")
            else:
                print("Nie ma takiej komendy")
        else:
            pass

def find_user_by_id(data: list[dict], user_id: int) -> dict | None:
    for user in data:
        if user.get("id") == user_id:
            print(f'{user}')
            return user
    return None

def find_users_by_name(data: list[dict], name: str) -> list[dict]:
    users = []
    nothing = []
    for user in data:
        if user.get("name") == name:
            users.append(user.get("name"))
        elif user.get("name") == None:
            nothing.append(user.get("name"))
    if len(users) > 0:
        print(f'Znaleziono {len(users)} użytkowników o imieniu {name}')
        return users
    elif len(nothing) > 0:
        print(f'Znaleziono {len(nothing)} użytkowników bez imienia')
        return nothing
    else:
        print("Nie znaleziono użytkowników o takim imieniu")
        
def delete_user_by_id(data: list[dict], user_id: int) -> bool:
    for user in data:
        if user.get("id") == user_id:
            data.remove(user)
            print("Użytkownik pomyślnie usunięty!")
            return True
    else:
        print("Nie znaleziono użytkownika")
        return False

def update_user_name(data: list[dict], user_id: int, new_name: str) -> bool:
    for user in data:
        if user.get("id") == user_id:
            user["name"] = new_name
            print("Nazwa użytkownika została zaktualizowana!")
            return True
    else:
        return False

def update_user_surname(data: list[dict], user_id: int, new_surname: str) -> bool:
    for user in data:
        if user.get("id") == user_id:
            user["surname"] = new_surname
            print("Nazwisko użytkownika zostało zaktualizowane!")
            return True
    else:
        return False
    
def update_user_birth_date(data: list[dict], user_id: int, new_birth_date: str) -> bool:
    for user in data:
        if user.get("id") == user_id:
            user["date of birth"] = new_birth_date
            print("Data urodzenia użytkownika została zaktualizowana!")
            return True
    else:
        return False

def is_name_taken(data: list[dict], name: str, surname: str) -> bool:
    for user in data:
        if user.get("name") == name and user.get("surname") == surname:
            print("Taki użytkownik już istnieje")
            return True
        print("Taki użytkownik nie istnieje")
        return False

def show_one_user(user: dict, id:int) -> None:
    for el in user:
        if el.get("id") == id:
            print("==="*20)
            for k,v in el.items():
                print(f'{k} ----- {v}')

def count_all_users(data: list[dict]) -> int:
    print(f'Liczba użytkowników zapisanych w systemie: {len(data)}')
    return len(data)

def count_users_with_missing_name(data: list[dict]) -> int:
    bez_imienia = 0
    for user in data:
        if user.get("name") == None:
            bez_imienia += 1
    print(f'Ilość użytkowników bez imienia wynosi: {bez_imienia}')
    return bez_imienia

def average_math_for_user(data: list[dict], id:int) -> float | None:
    for user in data:
        if user.get("id") == id:
            if len(user.get("grades mathematics")) > 0:
                srednia = sum(user.get("grades mathematics")) / len(user.get("grades mathematics"))
                print(f'Średnia ocen z matematyki dla tego użytkownika wynosi: {srednia}')
                return srednia
            else:
                print("Użytkownik nie ma ocen z danego przedmiotu")
                return None
            
def average_polish_for_user(data: list[dict], id:int) -> float | None:
    for user in data:
        if user.get("id") == id:
            if len(user.get("grades polish")) > 0:
                srednia = sum(user.get("grades polish")) / len(user.get("grades polish"))
                print(f'Średnia ocen z polskiego dla tego użytkownika wynosi: {srednia}')
                return srednia
            else:
                print("Użytkownik nie ma ocen z danego przedmiotu")
                return None
            
def average_english_for_user(data: list[dict], id:int) -> float | None:
    for user in data:
        if user.get("id") == id:
            if len(user.get("grades english")) > 0:
                srednia = sum(user.get("grades english")) / len(user.get("grades english"))
                print(f'Średnia ocen z angielskiego dla tego użytkownika wynosi: {srednia}')
                return srednia
            else:
                print("Użytkownik nie ma ocen z danego przedmiotu")
                return None

def overall_average_for_user(data: list[dict], id:int ) -> float | None:
    for user in data:
        if user.get("id") == id:
            oceny = user.get("grades mathematics") + user.get("grades polish") + user.get("grades english")
            if len(oceny) > 0:
                srednia = sum(oceny) / len(oceny)
                print(f'Średnia ocen ze wszystkich przedmiotów wynosi: {srednia}')
                return srednia
            else:
                print("Użytkownik nie ma ocen")
                return False

def best_student_in_subject(data: list[dict], subject: str) -> dict | None:
    highest_average = 0
    best_student = None
    subject_name = None
    for user in data:
        if subject == "math" and len(user.get('grades mathematics')) > 0:
            math = sum(user.get("grades mathematics")) / len(user.get("grades mathematics"))
            if math > highest_average:
                highest_average = math
                best_student = user.get("name")
                subject_name = "matematyki"
        elif subject == "polish" and len(user.get('grades polish')) > 0:
            polish = sum(user.get("grades polish")) / len(user.get("grades polish"))
            if polish > highest_average:
                highest_average = polish
                best_student = user.get("name")
                subject_name = "polskiego"
        elif subject == "english" and len(user.get('grades english')) > 0:
            english = sum(user.get("grades english")) / len(user.get("grades english"))
            if english > highest_average:
                highest_average = english
                best_student = user.get("name")
                subject_name = "angielskiego"
    print(f"Największą średnią z {subject_name} ma {best_student}")

def subject_average_for_all_users(data: list[dict], subject: str) -> float | None:
    oceny = 0
    ilosc_ocen = 0
    przedmiot_name = None
    average = 0
    for user in data:
        if subject == "math" and len(user.get('grades mathematics')) > 0:
            oceny += sum(user.get("grades mathematics"))
            ilosc_ocen += len(user.get("grades mathematics"))
            przedmiot_name = "matematyki"
        elif subject == "polish" and len(user.get('grades polish')) > 0:
            oceny += sum(user.get("grades polish"))
            ilosc_ocen += len(user.get("grades polish"))
            przedmiot_name = "polskiego"
        elif subject == "english" and len(user.get('grades english')) > 0:
            oceny += sum(user.get("grades english"))
            ilosc_ocen += len(user.get("grades english"))
            przedmiot_name = "angielskiego"
    average = oceny / ilosc_ocen
    print(f'Średnia ocen wszystkich użytkowników z {przedmiot_name} wynosi {average}')
