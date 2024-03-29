import re
import csv


def change_names(contacts_list):
    for contact in contacts_list:
        fio_list = ' '.join(contact[0:3]).split()

        if len(fio_list) != 3:
            fio_list.append('')
        full_contact = fio_list + change_phone_number(contact[3:])
        for current in updated_contact_list:
            if full_contact[:2] == current[:2]:
                updated_contact_list.remove(current)
                full_contact =  [x if x != "" else y for x,y in zip(full_contact, current)]
        updated_contact_list.append(full_contact)

    return updated_contact_list

def change_phone_number(contact_for_change):
    phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_sub = r'+7(\2)\3-\4-\5\7\8\9'
    contact_string = '?'.join(contact_for_change)
    changed_contact_string = phone_pattern.sub(phone_sub, contact_string)
    changed_contact_list = changed_contact_string.split('?')
    return  changed_contact_list

def duplicate_fio():
    distinct_list = {}
    for column in contacts[1:]:
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
        contacts = list(rows)
        updated_contact_list = []
        change_names(contacts)
        # duplicate_fio()

    with open("/Users/aleksanderpecherskiy/Desktop/my_demo/py-homeworks-advanced/5.Regexp/phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(updated_contact_list)
