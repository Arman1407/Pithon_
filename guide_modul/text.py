menu = ['Главное меню',
        'Открыть файл',
        'Сохранить файл',
        'Показать контакты',
        'Создать контакт',
        'Найти контакт',
        'Изменить контакт',
        'Удалить конта',
        'Выход']
input_menu = 'Выберите номер действия: '
input_menu_error = f'Вы ошиблись, введите число от 1 до {len(menu) - 1}'

load_successful = 'Телефонная книга загружена успешно'
save_successful = 'Телефонная книга сохранена успешно'

empty_book_error = 'Телефонная книга закрыта или в ней нет записей'

input_contact = ['Введите имя контакта: ',
                 'Ведите номер телефона: ',
                 'Введите комментарий: ']

input_edit_contact = ['Введите имя контакта или пропустите - ENTER: ',
                 'Ведите номер телефона или пропустите - ENTER: ',
                 'Введите комментарий или пропустите - ENTER: ']

input_search_word = 'Введите значение поиска: '

input_edit_contact_id = 'Введите порядковый номер контакта, подлежащий изменению: '

input_del_contact_id = 'Введите порядковый номер контакта, подлежащий удалению: '

operation = ['создан', 'изменен', 'удален']

confirm_changes = 'У Вас есть не сохраненные изменения. Сохранить (y/n):  '

exit_program = 'Досвидание'

def contact_action(name: str, action: str) -> str:
    return f'Контакт {name} успешно {action}!'

def not_find(word: str) -> str:
    return f'"{word}" в списке контактов не найдено'
