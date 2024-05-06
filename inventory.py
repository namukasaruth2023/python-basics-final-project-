import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")
        self.master.geometry("950x950")
        self.master.configure(bg="yellow")

        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inventory"
        )
        self.cursor = self.db_connection.cursor()

        self.items = []

        self.label = tk.Label(master, text="Inventory Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.item_label = tk.Label(master, text="Item:")
        self.item_label.pack()
        self.item_entry = tk.Entry(master)
        self.item_entry.pack()

        self.price_label = tk.Label(master, text="Price (per kg):")
        self.price_label.pack()
        self.price_entry = tk.Entry(master)
        self.price_entry.pack()

        self.quantity_label = tk.Label(master, text="Quantity (in kgs):")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.pack()

        self.supplier_label = tk.Label(master, text="Supplier:")
        self.supplier_label.pack()
        self.supplier_entry = tk.Entry(master)
        self.supplier_entry.pack()

        self.date_label = tk.Label(master, text="Date of Purchase (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(master)
        self.date_entry.pack()
        
        self.search_label = tk.Label(master, text="Search Item:")
        self.search_label.pack()
        self.search_entry = tk.Entry(master)
        self.search_entry.pack()


        self.add_button = tk.Button(master, text="Add Item", command=self.add_item, bg="red")
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(master, text="Update Item", command=self.update_item, bg="red")
        self.update_button.pack(pady=5)

        self.view_button = tk.Button(master, text="View Inventory", command=self.view_inventory, bg="red")
        self.view_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Item", command=self.delete_item, bg="red")
        self.delete_button.pack(pady=5)
        
        self.search_button = tk.Button(master, text="Search Item", command=self.search_item, bg="green")
        self.search_button.pack(pady=5)

        self.print_button = tk.Button(master, text="Print List of Inventory", command=self.print_inventory, bg="red")
        self.print_button.pack(pady=5)

    def add_item(self):
        item = self.item_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        supplier = self.supplier_entry.get()
        date = self.date_entry.get()

        if item and price and quantity and supplier:
                
                self.cursor.execute("INSERT INTO inventory (item, price, quantity, supplier, purchase_date) VALUES (%s, %s, %s, %s, %s)", (item, price, quantity, supplier, date))
                self.db_connection.commit()
                messagebox.showinfo("Success", f"Item '{item}' added to inventory.")
                self.item_entry.delete(0, tk.END)
                self.price_entry.delete(0, tk.END)
                self.quantity_entry.delete(0, tk.END)
                self.supplier_entry.delete(0, tk.END)
                self.date_entry.delete(0, tk.END)
          
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def update_item(self):
        item = self.item_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        supplier = self.supplier_entry.get()
        if item and price and quantity and supplier:
            self.cursor.execute("UPDATE inventory SET price=%s, quantity=%s, supplier=%s WHERE item=%s", (price, quantity, supplier, item))
            self.db_connection.commit()
            messagebox.showinfo("Success", f"Item '{item}' updated.")
            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.supplier_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_inventory(self):
        self.cursor.execute("SELECT * FROM inventory")
        items = self.cursor.fetchall()
        if items:
            inventory_info = "\n".join([f"Item: {item[0]}, Price (per kg): {item[1]}, Quantity (in kgs): {item[2]}, Supplier: {item[3]}, Purchase Date: {item[4]}" for item in items])
            messagebox.showinfo("Inventory", inventory_info)
        else:
            messagebox.showinfo("Inventory", "No items in inventory.")

    def delete_item(self):
        item = self.item_entry.get()
        if item:
            self.cursor.execute("DELETE FROM inventory WHERE item=%s", (item,))
            self.db_connection.commit()
            messagebox.showinfo("Success", f"Item '{item}' deleted from inventory.")
            self.item_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter an item.")
            
    def search_item(self):
        search_query = self.search_entry.get()
        if search_query:
            self.cursor.execute("SELECT * FROM inventory WHERE item LIKE %s", ('%' + search_query + '%',))
            items = self.cursor.fetchall()
            if items:
                inventory_info = "\n".join([f"Item: {item[0]}, Price (per kg): {item[1]}, Quantity (in kgs): {item[2]}, Supplier: {item[3]}, Purchase Date: {item[4]}" for item in items])
                messagebox.showinfo("Search Results", inventory_info)
            else:
                messagebox.showinfo("Search Results", f"No items found for '{search_query}'.")
        else:
            messagebox.showerror("Error", "Please enter an item name to search.")


    def print_inventory(self):
        self.cursor.execute("SELECT * FROM inventory")
        items = self.cursor.fetchall()
        if items:
            with open("inventory.txt", "w") as file:
                for item in items:
                    file.write(f"Item: {item[0]}, Price: {item[1]}, Quantity: {item[2]}, Supplier: {item[3]}, Purchase Date: {item[4]}\n")
            messagebox.showinfo("Success", "Inventory data has been downloaded to inventory.txt file.")
        else:
            messagebox.showinfo("Inventory", "No items in inventory.")

def main():
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
