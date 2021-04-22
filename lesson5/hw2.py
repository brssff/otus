import csv
import json


# прочитать файл с пользователями: users
with open('data/users.json', 'r') as file:
    j = file.read()
    users = json.loads(j)

books_lst = []
# прочитать файл с книгами: books
with open('data/books.csv', 'r') as file:
    reader = csv.reader(file)
    # получить заголовки
    header = next(reader)
    # итерируюсь по данным из csv делая из них словари, удаляю "лишние" key из словаря
    for row in reader:
        books_dict = dict(zip(header, row))
        books_dict.pop('Publisher')
        books_dict.pop('Genre')
        books_lst.append(books_dict)


def new_users():
    data = []
    for i in range(len(users)):
        updated_user = {
            'name': users[i].get('name'),
            'gender': users[i].get('gender'),
            'address': users[i].get('address'),
            'books': {
                "title": books_lst[i].get('Title'),
                "author": books_lst[i].get('Author'),
                "height": books_lst[i].get('Height')
            }
        }
        data.append(updated_user)
    return data


# записать новый файл
def write_json(users_dict):
    with open('data/result.json', 'w') as f:
        s = json.dumps(users_dict, indent=4)
        f.write(s)


write_json(new_users())