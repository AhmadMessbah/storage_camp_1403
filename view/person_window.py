import tkinter as tk



def insert_data():
     pass

root = tk.Tk()
root.title("person")

root.geometry("700x300")

label_id = tk.Label(root, text="ID:", font=("Arial", 14))
label_id.grid(row=0, column=0, pady=10, padx=10)
entry_id = tk.Entry(root, font=("Arial", 14))
entry_id.grid(row=0, column=1, pady=10, padx=10)

label_name = tk.Label(root, text="Name:", font=("Arial", 14))
label_name.grid(row=0, column=2, pady=10, padx=10)
entry_name = tk.Entry(root, font=("Arial", 14))
entry_name.grid(row=0, column=3, pady=10, padx=10)

label_family = tk.Label(root, text="Family:", font=("Arial", 14))
label_family.grid(row=2, column=0, pady=10, padx=10)
entry_family = tk.Entry(root, font=("Arial", 14))
entry_family.grid(row=2, column=1, pady=10, padx=10)

label_phone = tk.Label(root, text="Phone:", font=("Arial", 14))
label_phone.grid(row=3, column=0, pady=10, padx=10)
entry_phone = tk.Entry(root, font=("Arial", 14))
entry_phone.grid(row=3, column=1, pady=10, padx=10)

button_insert = tk.Button(root, text="INSERT", command=insert_data, font=("Arial", 14))
button_insert.grid(row=6, column=2, columnspan=2, pady=20)

root.mainloop()
