from copy import deepcopy

class Contact:
    def __init__(self, name: str, phone: str, commet: str):
        self.name = name
        self.phone = phone
        self.comment = commet

    def full(self):
        return f'{self.name} {self.phone} {self.comment}'

class PhoneBook:
    def __init__(self, phone_book: dict = None, path: str = 'Pithon_\guide_class\phone_.txt'):
        self.path = path
        if phone_book is None:
            self.phone_book: dict[int, Contact] = {}
        else:
            self.phone_book = phone_book
        self.original_book = {}

    def open_file(self):                            # открывающая справочник
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for i, contact in enumerate(data, 1):
            contact = contact.strip().split(';')
            self.phone_book[i] = Contact(*contact)
        self.original_book = deepcopy(self.phone_book)
        
    def save_file(self):                        # сохраняет контакт
        data = []
        for contact in self.phone_book.values():
            contact = ';'.join(contact)
            data.append(contact)
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def add_contact(self, new_contact: list[str]):        # добавления контакта
        c_id = max(self.phone_book) + 1
        self.phone_book[c_id] = new_contact

    def find_contact(self, word: str):    # находит контакт
        result = {}
        for c_id, contact in self.phone_book.items():
            if word.lower() in contact.full():
                result[c_id] = contact
                break
        return PhoneBook(result)
        
    def edit_contact(self, c_id: int, new_contact: list[str]):        # изменяет контакты
        current_contact = self.phone_book.get(c_id)
        contact = []
        for i in range(len(new_contact)):
            if new_contact[i]:
                contact.append(new_contact[i])
            else:
                contact.append(current_contact[i])
        self.phone_book[c_id] = Contact(*contact)
        return contact[0]

    def delete_contact(self, c_id: int) -> str:               # удаляет контакты
        return self.phone_book.pop(c_id)[0]

    def max_len(self, option: str) -> int:
        result = []
        for contact in self.phone_book.values():
            if option == 'name':
                item = contact.name
            elif option == 'phone':
                item = contact.phone
            else:
                item = contact.comment
            result.append(item)
        return len(max(result, key = len))