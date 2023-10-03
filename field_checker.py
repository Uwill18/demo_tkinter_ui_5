# # Create function to check entry vs listbox
# # from main import my_entry, toppings, update
#
#
# def check(e):
#     # grab what was typed
#     typed = my_entry.get()
#     # typed = time_entry.get()
#
#     if typed == '':
#         data = toppings
#     else:
#         data = []
#         for item in toppings:
#             if typed.lower() in item.lower():
#                 data.append(item)
#
#     # update our listbox with selected items
#     update(data)