from copy import deepcopy

PATH = 'Python_\guide_modul\phone_one.txt'
phone_book = {}
original_book = {}

def open_file():                            # функция открывающая справочник
    global phone_book, PATH
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        phone_book[i] = contact
    original_book = deepcopy(phone_book)
    
def save_file():                        # функция сохраняет контакт
    global phone_book, PATH
    data = []
    for contact in phone_book.values():
        contact = ':'.join(contact)
        data.append(contact)
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)

def add_contact(new_contact: list[str]):        # функция добавления контакта
    global phone_book
    c_cd = max(phone_book) + 1
    phone_book[c_cd] = new_contact

def find_contact(word: str) -> dict[int, list[str]]:    # функция находит контакт
    global phone_book
    result = {}
    for c_cd, contact in phone_book.items():
        for feild in contact:
            if word.lower() in feild.lower():
                result[c_cd] = contact
                break
    return result
    
def edit_contact(c_cd: int, new_contact: list[str]):        # функция изменяет контакты
    global phone_book
    current_contact = phone_book.get(c_cd)
    contact = []
    for i in range(len(new_contact)):
        if new_contact[i]:
            contact.append(new_contact[i])
        else:
            contact.append(current_contact[i])
    phone_book[c_cd] = contact
    return contact[0]

def delete_contact(c_id: int) -> str:               # функция удаляет контакты
    global phone_book
    return phone_book.pop(c_id)[0]