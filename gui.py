
# Python program to create 
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
  
# import filedialog module
from tkinter import filedialog
from tkinter import ttk

from buttonfunctions import *
from sys import exit

# Create the root window
window = Tk()
  
# Set window title
window.title('Links To Dokuwiki Links Converter')
  
# Set window size
window.geometry("1000x800")
  
#Set window background color
window.config(background = "light gray")
  
# Create a File Explorer label
label_file_explorer = Label(window, 
                            text = "Links To Dokuwiki Links Converter",
                            height = 2, 
                            fg = "black",
                            background = "light gray")
label_file_explorer.grid(column = 1, row = 1, columnspan=2, sticky='we', pady = 4)




# Input Text Widget
label_file_explorer = Label(window, 
                            text = "Links Input",
                            height = 1, 
                            fg = "black",
                            background = "light gray",
                            justify="left")
label_file_explorer.grid(column = 1, row = 2, columnspan=2, sticky='w', pady = 0, padx=32)

input_textwidg_scrollbar = Scrollbar(window, orient=VERTICAL ,width=16)
input_textwidg = Text(window, yscrollcommand=input_textwidg_scrollbar.set, height = 10)
input_textwidg.grid(column = 1, row = 3, pady=(0,4), padx = 32, sticky='news')



# Console Output Text Widget
label_file_explorer = Label(window, 
                            text = "Status",
                            height = 1, 
                            fg = "black",
                            background = "light gray",
                            justify="left")
label_file_explorer.grid(column = 1, row = 4, columnspan=2, sticky='w', pady = 0, padx=32)

console_textwidg_scrollbar = Scrollbar(window, orient=VERTICAL ,width=16)
console_textwidg = Text(window, yscrollcommand=console_textwidg_scrollbar.set, height = 2)
console_textwidg.grid(column = 1, row = 5, pady=(0,4), padx = 32, sticky='news')

button_convert = Button(window, 
                        text = "Convert",
                        command = lambda: convertLinks(input_textwidg, console_textwidg, results_textwidg)) 
button_convert.grid(column = 2, row = 5, sticky='e', padx = 32)



# Results Output Text Widget
label_file_explorer = Label(window, 
                            text = "Converted Links",
                            height = 1, 
                            fg = "black",
                            background = "light gray",
                            justify="left")
label_file_explorer.grid(column = 1, row = 6, columnspan=2, sticky='w', pady = 0, padx=32)

results_textwidg_scrollbar = Scrollbar(window, orient=VERTICAL ,width=16)
results_textwidg = Text(window, yscrollcommand=results_textwidg_scrollbar.set, height = 10)
results_textwidg.grid(column = 1, row = 7, pady=(0,8), padx = 32, sticky='news')

button_exit = Button(window, 
                     text = "Exit",
                     command = exit) 
button_exit.grid(column = 2,row = 7, sticky='e', padx = 32)

window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(3, weight=5)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(7, weight=5)

# Let the window wait for any events
window.mainloop()

# TODO: Add a save button that prompts filename to save to