from tkinter import *

root = Tk()
root.title('Codemy.com - Auto Select/Search')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")


# Update the listbox
def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add toppings to listbox
    for item in data:
        my_list.insert(END, item)


# Update entry box with listbox clicked
def fillout(e):
    # Delete whatever is in the entry box
    my_entry.delete(0, END)
    id_entry.delete(0, END)
    time_entry.delete(0, END)
    status_entry.delete(0, END)
    city_entry.delete(0, END)
    address_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    deadline_entry.delete(0, END)
    arrival_entry.delete(0, END)
    weight_entry.delete(0, END)

    # Add clicked list item to entry box
    my_entry.insert(0, my_list.get(ANCHOR))
    id_entry.insert(0, my_list.get(ANCHOR))
    time_entry.insert(0, my_list.get(ANCHOR))
    status_entry.insert(0, my_list.get(ANCHOR))
    city_entry.insert(0, my_list.get(ANCHOR))
    address_entry.insert(0, my_list.get(ANCHOR))
    zipcode_entry.insert(0, my_list.get(ANCHOR))
    deadline_entry.insert(0, my_list.get(ANCHOR))
    arrival_entry.insert(0, my_list.get(ANCHOR))
    weight_entry.insert(0, my_list.get(ANCHOR))


# Create function to check entry vs listbox
def check(e):
    # grab what was typed
    typed = my_entry.get()
    # typed = time_entry.get()

    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)

    # update our listbox with selected items
    update(data)


# Create a label
my_label = Label(root, text="Search Packages",
                 font=("Helvetica", 14), fg="grey")

my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list of pizza toppings
toppings = ["Pepperoni", "Peppers", "Mushrooms",
            "Cheese", "Onions", "Ham", "Taco"]

# Add the toppings to our list
update(toppings)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)


# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)



# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand=1, padx=20)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=1, padx=10, pady=10)

time_label = Label(data_frame, text="TIME")
time_label.grid(row=0, column=2, padx=10, pady=10)
time_entry = Entry(data_frame)
time_entry.grid(row=0, column=3, padx=10, pady=10)

status_label = Label(data_frame, text=" ")
status_label.grid(row=0, column=4, padx=10, pady=10)
status_entry = Entry(data_frame)
status_entry.grid(row=0, column=5, padx=10, pady=10)

city_label = Label(data_frame, text="CITY")
city_label.grid(row=1, column=0, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=1, padx=10, pady=10)

address_label = Label(data_frame, text="ADDRESS")
address_label.grid(row=1, column=2, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=3, padx=10, pady=10)

zipcode_label = Label(data_frame, text="ZIP")
zipcode_label.grid(row=1, column=4, padx=10, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=5, padx=10, pady=10)

deadline_label = Label(data_frame, text="DEADLINE")
deadline_label.grid(row=2, column=0, padx=10, pady=10)
deadline_entry = Entry(data_frame)
deadline_entry.grid(row=2, column=1, padx=10, pady=10)

arrival_label = Label(data_frame, text="ARRIVAL")
arrival_label.grid(row=2, column=2, padx=10, pady=10)
arrival_entry = Entry(data_frame)
arrival_entry.grid(row=2, column=3, padx=10, pady=10)

weight_label = Label(data_frame, text="WEIGHT")
weight_label.grid(row=3, column=0, padx=10, pady=10)
weight_entry = Entry(data_frame)
weight_entry.grid(row=3, column=1, padx=10, pady=10)

submit_button_frame = LabelFrame(root, text="SUBMIT")
submit_button_frame.pack(fill="x", expand=1, padx=20)

# Create a binding on the entry box
time_entry.bind("<KeyRelease>", check)

# # Search Menu
# search_menu = Menu(my_menu, tearoff=0)
# my_menu.add_cascade(label="Search", menu=search_menu)
# # Drop down menu
# search_menu.add_command(label="Search", command=lookup_records)
# search_menu.add_separator()
# search_menu.add_command(label="Reset", command=query_database)

root.mainloop()
