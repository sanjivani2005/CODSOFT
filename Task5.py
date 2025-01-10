import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        
        self.contacts = []
        
        # Title
        self.title_label = tk.Label(root, text="Contact Manager", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333333")
        self.title_label.pack(pady=20)
        
        # Frame for contact details
        self.contact_frame = tk.Frame(root, bg="#f0f0f0")
        self.contact_frame.pack(pady=20)
        
        # Labels and Entries for contact details
        self.name_label = tk.Label(self.contact_frame, text="Name:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333333")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.contact_frame, width=30, font=("Helvetica", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.phone_label = tk.Label(self.contact_frame, text="Phone:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333333")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.contact_frame, width=30, font=("Helvetica", 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.email_label = tk.Label(self.contact_frame, text="Email:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333333")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.contact_frame, width=30, font=("Helvetica", 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_label = tk.Label(self.contact_frame, text="Address:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333333")
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.address_entry = tk.Entry(self.contact_frame, width=30, font=("Helvetica", 12))
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # Buttons for CRUD operations
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)
        
        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=10, pady=5)
        
        self.view_button = tk.Button(self.button_frame, text="View Contacts", command=self.view_contacts, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white")
        self.view_button.grid(row=0, column=1, padx=10, pady=5)
        
        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact, font=("Helvetica", 12, "bold"), bg="#FF9800", fg="white")
        self.search_button.grid(row=0, column=2, padx=10, pady=5)
        
        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact, font=("Helvetica", 12, "bold"), bg="#9C27B0", fg="white")
        self.update_button.grid(row=0, column=3, padx=10, pady=5)
        
        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, font=("Helvetica", 12, "bold"), bg="#f44336", fg="white")
        self.delete_button.grid(row=0, column=4, padx=10, pady=5)
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            contact = {
                "Name": name,
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter Name and Phone number.")
    
    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join(f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts)
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")
    
    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if 
                              search_term.lower() in contact['Name'].lower() or 
                              search_term in contact['Phone']]
            if found_contacts:
                contact_list = "\n".join(f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts)
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", f"No contacts found for '{search_term}'.")
    
    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if 
                              search_term.lower() in contact['Name'].lower() or 
                              search_term in contact['Phone']]
            if found_contacts:
                contact = found_contacts[0]
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, contact['Name'])
                self.phone_entry.delete(0, tk.END)
                self.phone_entry.insert(0, contact['Phone'])
                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, contact['Email'])
                self.address_entry.delete(0, tk.END)
                self.address_entry.insert(0, contact['Address'])
                messagebox.showinfo("Update Contact", "Update the details and click 'Add Contact' to save changes.")
            else:
                messagebox.showinfo("Update Contact", f"No contacts found for '{search_term}'.")
    
    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if 
                              search_term.lower() in contact['Name'].lower() or 
                              search_term in contact['Phone']]
            if found_contacts:
                contact = found_contacts[0]
                self.contacts.remove(contact)
                messagebox.showinfo("Delete Contact", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Delete Contact", f"No contacts found for '{search_term}'.")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Main function to run the application
def main():
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
