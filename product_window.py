import tkinter as tk



def insert_data():
     pass

root = tk.Tk()
root.title("Stuff")

root.geometry("350x350")

label_name = tk.Label(root, text="name:", font=("Arial", 14))
label_name.grid(row=0, column=0, pady=10, padx=10)
entry_name = tk.Entry(root, font=("Arial", 14))
entry_name.grid(row=0, column=1, pady=10, padx=10)

label_brand = tk.Label(root, text="brand:", font=("Arial", 14))
label_brand.grid(row=5, column=0, pady=10, padx=10)
entry_brand = tk.Entry(root, font=("Arial", 14))
entry_brand.grid(row=5, column=1, pady=10, padx=10)

label_count = tk.Label(root, text="count:", font=("Arial", 14))
label_count.grid(row=2, column=0, pady=10, padx=10)
entry_count = tk.Entry(root, font=("Arial", 14))
entry_count.grid(row=2, column=1, pady=10, padx=10)

label_price_b = tk.Label(root, text="price_b:", font=("Arial", 14))
label_price_b.grid(row=3, column=0, pady=10, padx=10)
entry_price_b = tk.Entry(root, font=("Arial", 14))
entry_price_b.grid(row=3, column=1, pady=10, padx=10)


label_price_b = tk.Label(root, text="price_b:", font=("Arial", 14))
label_price_b.grid(row=4, column=0, pady=10, padx=10)
entry_price_b = tk.Entry(root, font=("Arial", 14))
entry_price_b.grid(row=4, column=1, pady=10, padx=10)



button_insert = tk.Button(root, text="INSERT", command=insert_data, font=("Arial", 20))
button_insert.grid(row=6, column=1, columnspan=2, pady=20)

root.mainloop()
