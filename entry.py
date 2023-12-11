import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def increment_id():
    """
    This function will increment the cartridge_id by 1
    """
    with open('cartridges.json', 'r') as f:
        cartridges = json.load(f)
    max_id = max(cartridge['cartridge_id'] for cartridge in cartridges)
    return int(max_id) + 1

def add_cartridge():
    """
    This function will add a new cartridge to the 'cartridges.json' file
    """
    new_id = increment_id()
    new_model = model_entry.get()
    new_return_date = return_date_entry.get()
    if not new_return_date.strip():
        messagebox.showerror("Error","Return date field cannot be empty")
    elif not new_model.strip():
        messagebox.showerror("Error","Model field cannot be empty")
    elif not all(c.isdigit() or c=='-' for c in new_return_date):
        messagebox.showerror("Error","Return date format should be in yyyy-mm-dd")
    else:
        new_cartridge = {"cartridge_id": new_id, "model": new_model, "return_date": new_return_date}
        with open('cartridges.json', 'r') as f:
            cartridges = json.load(f)
        cartridges.append(new_cartridge)
        with open('cartridges.json', 'w') as f:
            json.dump(cartridges, f)
        messagebox.showinfo("Info", "Cartridge has been added to the inventory!")
        model_entry.delete(0, 'end')
        return_date_entry.delete(0, 'end')
   

root = tk.Tk()
root.title("Inventory Manager")

label1 = ttk.Label(root, text="Model:")
label1.grid(row=0, column=0, padx=5, pady=5)

model_entry = ttk.Entry(root)
model_entry.grid(row=0, column=1, padx=5, pady=5)

label2 = ttk.Label(root, text="Return Date (yyyy-mm-dd):")
label2.grid(row=1, column=0, padx=5, pady=5)

return_date_entry = ttk.Entry(root)
return_date_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = ttk.Button(root, text="Add Cartridge", command=add_cartridge)
add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
