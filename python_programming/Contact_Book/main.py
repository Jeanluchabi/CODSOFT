import tkinter as tk
from tkinter import messagebox
from contact_manager import add_contact, view_contacts, search_contact, update_contact, delete_contact
from contact import Contact

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=6, column=0)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=6, column=1)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=8, column=0, columnspan=2)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=9, column=0, columnspan=2)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.grid(row=10, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        contact = Contact(name, phone, email, address)
        add_contact(self.contacts, contact)
        messagebox.showinfo("Success", "Contact added successfully")

    def view_contacts(self):
        self.result_text.delete(1.0, tk.END)
        contacts = view_contacts(self.contacts)
        for contact in contacts:
            self.result_text.insert(tk.END, f"{contact}\n")

    def search_contact(self):
        search_term = self.search_entry.get()
        results = search_contact(self.contacts, search_term)
        self.result_text.delete(1.0, tk.END)
        for contact in results:
            self.result_text.insert(tk.END, f"{contact}\n")

    def update_contact(self):
        search_term = self.search_entry.get()
        results = search_contact(self.contacts, search_term)
        if results:
            contact = results[0]
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            update_contact(contact, name, phone, email, address)
            messagebox.showinfo("Success", "Contact updated successfully")
        else:
            messagebox.showerror("Error", "Contact not found")

    def delete_contact(self):
        search_term = self.search_entry.get()
        results = search_contact(self.contacts, search_term)
        if results:
            contact = results[0]
            delete_contact(self.contacts, contact)
            messagebox.showinfo("Success", "Contact deleted successfully")
        else:
            messagebox.showerror("Error", "Contact not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

