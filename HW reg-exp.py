import re
import csv

updated_contact_list = []

def change_names(c_list):
    name_pattern = r'([А-Я])'
    count_sub = r' \1'
    for column in c_list[1:]:
        fio = column[0] + column[1] + column[2]
        if len(re.sub(name_pattern, count_sub, fio).split()) == 3:
            column[0] = re.sub(name_pattern, count_sub, fio).split()[0]
            column[1] = re.sub(name_pattern, count_sub, fio).split()[1]
            column[2] = re.sub(name_pattern, count_sub, fio).split()[2]
        elif len(re.sub(name_pattern, count_sub, fio).split()) == 2:
            column[0] = re.sub(name_pattern, count_sub, fio).split()[0]
            column[1] = re.sub(name_pattern, count_sub, fio).split()[1]
            column[2] = ''
        elif len(re.sub(name_pattern, count_sub, fio).split()) == 1:
            column[0] = re.sub(name_pattern, count_sub, fio).split()[0]
            column[1] = ''
            column[2] = ''
    return

def change_phone_number():
    phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_sub = r'+7(\2)\3-\4-\5\7\8\9'
    for column in contacts_list:
        column[5] = phone_pattern.sub(phone_sub, column[5])
    return

def duplicate_fio():
    distinct_list = {}
    for column in contacts_list[1:]:
        last_name = column[0]
        if last_name not in distinct_list:
            distinct_list[last_name] = column
        else:
            for indic, item in enumerate(distinct_list[last_name]):
                if item == '':
                    distinct_list[last_name][indic] = column[indic]

    for last_name, contact in distinct_list.items():
        for contacts in contact:
            if contact not in updated_contact_list:
                updated_contact_list.append(contacts)

    return updated_contact_list



if __name__ == '__main__':
    with open("/Users/aleksanderpecherskiy/Desktop/my_demo/py-homeworks-advanced/5.Regexp/phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        updated_contact_list = []
        change_names(contacts_list)
        change_phone_number()
        duplicate_fio()

    with open("/Users/aleksanderpecherskiy/Desktop/my_demo/py-homeworks-advanced/5.Regexp/phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
