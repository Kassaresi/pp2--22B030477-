from sql_query import *
import psycopg2, re
from config import config


while True:
    # Соединение с базой благодаря config()
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    
    # Список команд
    action = int(input("""
        send 1 for create table
        send 2 for add information
        send 3 for update data
        send 4 for querying data
        send 5 for delete data
        send 6 for clear table
        send 7 for querying by pattern
        send 0 for quit
        
        YOUR ANSWER --> """))
    
    
    # Запрос по шаблону
    if action == 7:
        # поиск
        pattern = input()
        # phone = "SELECT COUNT(*) FROM phonebook WHERE phone_num LIKE %s"
        offset = 0
        # Вывод поиска
        while True:
            cur.execute(sql_search_by_pattern, ('%' + pattern + '%', '%' + pattern + '%', offset))
            info = cur.fetchall()
            for element in info:
                print(element)
            print(int(offset / 10), offset)
            action = int(input('send 1 for next, send 2 for previous, send 0 for break'))
            if not info:
                if action == 1:
                    offset += 10
                if action == 2:
                    if offset - 10 < 0:
                        print('NO')
                    else:
                        offset -= 10
            if action == 0:
                break
            
            
    # Создание таблицы        
    elif action == 1:
        print("Table is created")
        cur.execute(sql_create_table)
        conn.commit()
        
    
    # Добавление информации в таблицу    
    elif action == 2:
        # Выбираем путь по которому будем записывать информацию, если 1, то поготовому сsv, если 2, то по одному(стандартный способ), если 3, то это стандартный способ, но с большим количеством инфомации
        action = int(input("""
            send 1 for upload from csv
            send 2 for entering from console (sample: "[name], [number]"
            send 3 for entering from list 
            
            !!! 
                the number must be without any spaces,
                special characters, etc. numbers only,
                
                example --> [87324321332]
                
                example of element of list:
                [Kassi, 87058086196]
            
            !!!
            
            YOUR ANSWER --> """))


        if action == 1:
            path = input("Write path (without spaces) --> ")
            cur.execute(sql_upload_from_csv, (path, ))
            conn.commit()
        
        elif action == 2:
            # Чтобы закончить процесс пишите (end)
            print("write 'end' for quit mode")
            while True:
                name = input("contact name --> ")
                if name == 'end':
                    break
                number = input("contact number --> ")
                if number == 'end':
                    break
                cur.execute(sql_check_exist_by_name, (name, ))
                # Проверка существует ли контакт
                if cur.fetchone()[0] != 0:
                    cur.execute(sql_change_phone_by_name, (number, name))
                    print("contact updated")
                else:
                    cur.execute(sql_entering_from_console, (name, str(number)))
                    print("new contact created")
                conn.commit()
        
        elif action == 3:
            print("write 'end' for quit mode")
            returned_list = ''
            # elements = element.split(sep='\n')
            while True:
                element = input()
                if element == 'end':
                    break
                pattern_name = r'[a-zA-Z]+'
                pattern_phone = r'[0-9]+'
                res_name = re.findall(pattern_name, element)
                res_phone = re.findall(pattern_phone, element)
                name = ''
                phone = ''
                for i in res_name:
                    name += i + ' '
                for j in res_phone:
                    phone += j + ' '
                if len(res_phone) != 1:
                    # print(res_phone)
                    returned_list += f'{name}, {phone}' + '\n'
                else:
                    cur.execute(sql_check_exist_by_name, (name,))
                    if cur.fetchone()[0] != 0:
                        cur.execute(sql_change_phone_by_name, (phone, name))
                    else:
                        cur.execute(sql_entering_from_console, (name, phone))
                    conn.commit()
            print(returned_list)
            
            
    # Обновление данных
    elif action == 3:
        # Выбор по определенному поиску
        action = int(input("""
            send 1 for updating by id
            send 2 for updating by name
            send 3 for updating by phone
        
            YOUR ANSWER --> """))
        # Поиск по id 
        if action == 1:
            id = input("id: ")
            action = int(input("send 1 for change name\nsend 2 for change number\nYOUR ANSWER --> "))
            # Обновление по имени
            if action == 1:
                new_name = input("new name: ")
                cur.execute(sql_change_name_by_id, (new_name, id))
            # Обновление по номеру
            if action == 2:
                new_number = input("new number: ")
                cur.execute(sql_change_phone_by_id, (new_number, id))
        # Поиск по имени
        if action == 2:
            name = input("name: ")
            # Выбор что именно изменить
            action = int(input("send 1 for change name\nsend 2 for change number\nYOUR ANSWER --> "))
            # Обновление по имени
            if action == 1:
                new_name = input("new name: ")
                cur.execute(sql_check_exist_by_name, (name, ))
                count = cur.fetchone()[0]
                # Проверка если ли дубликаты или же существует ли контакт вообще
                if count > 1:
                    print("there is two contact: ")
                    cur.execute(sql_select_by_name, (name, ))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_change_name_by_id, (new_name, id))
                elif count == 1:
                    cur.execute(sql_change_name_by_name, (new_name, name ))
                else:
                    print("this contact do not exist")
            # Обновление по номеру
            if action == 2:
                new_number = input("new number: ")
                cur.execute(sql_select_by_name, (name,))
                count = cur.fetchone()[0]
                # Проверка
                if count > 1:
                    print("there are contact: ")
                    cur.execute(sql_select_by_name, (name, ))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_change_name_by_id, (new_number, id))
                elif cur.fetchone()[0] == 1:
                    cur.execute(sql_change_name_by_name, (new_number, name))
                else:
                    print("this contact do not exist")
        # Поиск по номеру телефона
        elif action == 3:
            number = input("number: ")
            action = int(input("send 1 for change name\nsend 2 for change number\nYOUR ANSWER --> "))
            if action == 1:
                new_name = input("new name: ")
                cur.execute(sql_check_exist_by_phone, (number, ))
                count = cur.fetchone()[0]
                if count > 1:
                    print("there are contact: ")
                    cur.execute(sql_select_by_phone, (number, ))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_change_name_by_id, (new_name, id))
                elif count == 1:
                    cur.execute(sql_change_name_by_phone, (new_name, number))
                else:
                    print("this contact do not exist")
            elif action == 2:
                new_number = input("new number: ")
                cur.execute(sql_check_exist_by_phone, (number, ))
                count = cur.fetchone()[0]
                if count > 1:
                    print("there are contact: ")
                    cur.execute(sql_select_by_phone, (number, ))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_change_name_by_id, (new_number, id))
                elif count == 1:
                    cur.execute(sql_change_name_by_phone, (new_number, number))
                else:
                    print("this contact do not exist")
        conn.commit()
    
    
    # Показ данных
    elif action == 4:
        while True:
            filter_id = int(input("1 for turn on, 0 for turn off id\nans: "))
            filter_name = int(input("1 for turn on, 0 for turn off name\nans: "))
            filter_phone = int(input("1 for turn on, 0 for turn off phone\nans: "))

            if filter_id:
                if filter_name:
                    if filter_phone:
                        cur.execute(sql_select_filter_id_phone_name)
                    else:
                        cur.execute(sql_select_filter_name_id)
                elif filter_phone:
                    cur.execute(sql_select_filter_id_phone)
                else:
                    cur.execute(sql_select_filter_id)
            elif filter_name:
                if filter_phone:
                    cur.execute(sql_select_filter_name_phone)
                else:
                    cur.execute(sql_select_filter_name)
            else:
                cur.execute(sql_select_filter_phone)
            temp = cur.fetchall()
            print(len(temp[0]))
            if len(temp[0]) == 3:
                for first, second, third in temp:
                    print(first, second, third)
            elif len(temp[0]) == 2:
                for second, third in temp:
                    print(second, third)

            end = int(input("1 for end, 0 for continue"))
            if end:
                break
            
    # Удаление данных
    elif action == 5:
        action = int(input("send 1 for delete by name\nsend 2 for delete by phone\nYOUR ANS -->"))
        if action == 1:
            while True:
                name = input("name or end for end: ")
                cur.execute(sql_check_exist_by_name, (name,))
                count = cur.fetchone()[0]
                if count > 1:
                    print("there are contact: ")
                    cur.execute(sql_select_by_name, (name,))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_delete_by_id, (id, ))
                elif count == 1:
                    cur.execute(sql_delete_by_name, (name, ))
                else:
                    print("this contact do not exist")
                conn.commit()
                end = int(input("1 for end, 0 for continue"))
                if end:
                    break
        elif action == 2:
            while True:
                name = input("number or end for end: ")
                cur.execute(sql_check_exist_by_phone, (name,))
                count = cur.fetchone()[0]
                if count > 1:
                    print("there are contact: ")
                    cur.execute(sql_select_by_phone, (name,))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_delete_by_id, (id,))
                elif count == 1:
                    cur.execute(sql_delete_by_phone, (name,))
                else:
                    print("this contact do not exist")
                conn.commit()
                end = int(input("1 for end, 0 for continue"))
                if end:
                    break
    # Очистка данных
    elif action == 6:
        cur.execute(sql_clear_all)
        conn.commit()
    # Выход
    elif action == 0:
        break