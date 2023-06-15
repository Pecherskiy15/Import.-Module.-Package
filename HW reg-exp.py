from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("/Users/aleksanderpecherskiy/Desktop/my_demo/py-homeworks-advanced/5.Regexp/phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.

result_list, phone, name, organisation, position, email, result_dict = [], [], [], [], [], [], {}
buff = ""
for i in range(1, len(contacts_list)):
    res = (re.findall(r'\d+\s*', ''.join(contacts_list[i])))
    phone.append((''.join(res)).replace(' ', ""))

    buff = ""
    for j in range(3):
         if len(contacts_list[i][j]) > 1:
            buff += " " + contacts_list[i][j]
    name.append(buff)
    organisation.append(contacts_list[i][3])
    position.append(contacts_list[i][4])
    email.append(contacts_list[i][6])

for i in range(len(phone)):
    if phone[i]:
        phone[i] = f'+7({phone[i][1:4]}){phone[i][3:]}'
    if len(phone[i]) > 15:
        phone[i] = f'{phone[i][0:15]} доб. {phone[i][15:]}'

result_list = zip(name,organisation,position,phone,email)
result_list = list(result_list)

for i in range(len(result_list)):
    result_dict[" ".join(result_list[i][0].split()[0:2])]= {'last_name':" ".join(result_list[i][0].split()[0:1])}
    result_dict[" ".join(result_list[i][0].split()[0:2])].update({'first_name':" ".join(result_list[i][0].split()[1:2])})
    if len(result_list[i][0].split()[2:3]) > 0:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'surname':" ".join(result_list[i][0].split()[2:3])})
    else:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'surname': "Информации нет"})
    if len(result_list[i][1]) > 0:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'organization':result_list[i][1]})
    else:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'organization': "Информации нет"})
    if len(result_list[i][2]) > 0:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'position':result_list[i][2]})
    else:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'organization': "Информации нет"})
    if len(result_list[i][3]) > 0:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'phone':result_list[i][3]})
    else:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'phone': "Информации нет"})
    if len(result_list[i][4]) > 0:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'email':result_list[i][4]})
    else:
        result_dict[" ".join(result_list[i][0].split()[0:2])].update({'email': "Информации нет"})

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("/Users/aleksanderpecherskiy/Desktop/my_demo/py-homeworks-advanced/5.Regexp/phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(result_dict)
