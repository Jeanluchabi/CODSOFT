from contact import Contact

def add_contact(contact_list, contact):
    contact_list.append(contact)

def view_contacts(contact_list):
    return [str(contact) for contact in contact_list]

def search_contact(contact_list, search_term):
    results = [contact for contact in contact_list if search_term.lower() in contact.name.lower() or search_term in contact.phone]
    return results

def update_contact(contact, name=None, phone=None, email=None, address=None):
    if name:
        contact.name = name
    if phone:
        contact.phone = phone
    if email:
        contact.email = email
    if address:
        contact.address = address

def delete_contact(contact_list, contact):
    contact_list.remove(contact)

