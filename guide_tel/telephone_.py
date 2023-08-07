"""
w - перезапись
r - чтение
a - дозапись
encodinf = "UTF-8"

справочник должен содержать данные:
имя, телефон, комментарий
хранится в файле phone.txt
Кирилл; 899999999; Семинары

выводить все контакты на экран
добавить контакт
удалить контакт
изменить контакт
найти контакт конкретный
открыть сохранить файл целиком
выход из меню
можно сделать копию, поработать и сохранить
"""

file = 'Python_lesson_new\guide_tel\guide.txt'
contact = ['Кирukghukukа; 89032621542; рабочий']

def add_contact(contact, file):                                 # добавляет котакты guide.txt
    with open (file, 'a', encoding='UTF-8') as add_c:
        add_c.writelines(f'\n{contact}')

def delete_contact(contact, file):                              # удаляет контакты
    with open(file, "r", encoding='UTF-8') as f:
        lines = f.readlines()
    with open(file, "w", encoding='UTF-8') as f:
        for line in lines:
            if line.strip("\n") != contact:
                f.write(line)

def change_contact(file):                                       # изменяет контакты
    with open(file, "r", encoding='UTF-8') as f:
        lines = f.readlines()
        data = list(enumerate(lines))
        for line in data:
            print(line)
        number = int(input("Введите порядковый номер конатакта который хотите изменить: "))
        changes = input("Введите изменение в формате <Имя; Номер; Комментарий> : ")
        lines[number] = (f"{changes}\n")
    with open(file, "w", encoding='UTF-8') as f:
        for line in lines:
            f.write(line)

def find_contact(contact, file):                                # находит контакт по одному из критериев
    with open(file, "r", encoding='UTF-8') as f:
        lines = f.readlines()
        name = input("Введите параметр поиска (имя, номер, комментарий): ")
        for line in lines:
            if name in line.split(';'):
                print(line)

action = ''
while action != '6':
    print(
        """
    1. добавить контакт
    2. удалить контакт
    3. изменить контакт
    4. найти контакт 
    5. открыть сохранить файл целиком
    6. выход из меню
    """
    )
    action = input('Введите номер действия: ')
    if action == '1':
        name = input('Введите имя: ')
        number = input('Введите номер телефона: ')
        comment = input("Введите комментарий: ")
        add_contact(f'{name};{number};{comment}', file)
        print(f"\nКонтакт '{name};{number};{comment}' успешно добавлен.\n")

    elif action == '2':
        contact = input("Введите данные контакта (имя; номер; комментарий), который хотите удалить: ")
        delete_contact(contact, file)

    elif action == '3':
        contact = input("Введите данные контакта (имя; номер; комментарий), который хотите изменить: ")
        change_contact(file)

    elif action == '4':
        contact = input("Введите данные контакта (имя; номер; комментарий), который хотите найти: ")
        find_contact(contact, file)
















