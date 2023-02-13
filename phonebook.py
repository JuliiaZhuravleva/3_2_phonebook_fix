import re


class Phonebook:
    def __init__(self, attrs, contacts_raw):
        self.attrs = attrs
        self.contacts_raw = contacts_raw
        self.contacts_dict = []
        self.unique_contacts = {}

    def normalize(self):
        self.contacts_to_dict()
        self.get_names_structured()
        self.phone_normalize()
        self.get_unique_contacts()

    def contacts_to_dict(self):
        for contact in self.contacts_raw:
            contact_dict = {}
            for attr in self.attrs:
                contact_dict[attr] = contact[self.attrs.index(attr)]
            self.contacts_dict.append(contact_dict)

    def get_names_structured(self):
        for contact in self.contacts_dict:
            fio = ' '.join([contact['lastname'], contact['firstname'], contact['surname']]).strip()
            regex_fio = re.compile(r'^([А-ё]+)\s+([А-ё]+)\s*([А-ё]*)')
            result_fio = regex_fio.search(fio)
            contact['lastname'] = result_fio.group(1)
            contact['firstname'] = result_fio.group(2)
            contact['surname'] = result_fio.group(3)

    def phone_normalize(self):
        regex_phone = re.compile(r'(\+7|8)\s*\(?(495)\)?\s*-?(\d{3})\s*-?(\d{2})\s*-?(\d{2})')
        regex_additional_phone = re.compile(r'\(?доб.\s*(\d{4})\)?')
        for contact in self.contacts_dict:
            contact['phone'] = regex_phone.sub(r'+7(\2)\3-\4-\5', contact['phone'])
            contact['phone'] = regex_additional_phone.sub(r'доб.\1', contact['phone'])

    def get_unique_contacts(self):
        for contact in self.contacts_dict:
            contact_key = contact['lastname'] + ' ' + contact['firstname']
            if contact_key not in self.unique_contacts:
                self.unique_contacts[contact_key] = contact
            for attr in contact:
                if contact[attr] != '':
                    self.unique_contacts[contact_key][attr] = contact[attr]








