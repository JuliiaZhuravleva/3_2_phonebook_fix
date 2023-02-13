from phonebook import Phonebook

from pprint import pprint
import csv


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    headers = contacts_list[0]
    contacts = contacts_list[1::]

    phonebook = Phonebook(attrs=headers, contacts_raw=contacts)
    phonebook.normalize()

    contacts_list = [headers]
    for contact in phonebook.unique_contacts:
        row = []
        for header in headers:
            row.append(phonebook.unique_contacts[contact][header])
        contacts_list.append(row)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
