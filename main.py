import tkinter as tk
import requests
from tkinter import messagebox
import time

from github_lib import get_latest_version_name


__version__ = "1.0.0"


def check_for_updates():
    latest_version = get_latest_version_name()
    if latest_version > __version__:
        show_update_popup()


def show_update_popup():
    messagebox.showinfo("Update Available",
                        "A new version is available. Please update your app.")


def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))


def on_clear():
    entry.delete(0, tk.END)


def on_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying the input/output
entry = tk.Entry(root, width=20, font=("Arial", 24),
                 borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2,
                           font=("Arial", 20), command=on_equal)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=(
            "Arial", 20), command=lambda value=text: on_button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text="C", width=5,
                         height=2, font=("Arial", 20), command=on_clear)
clear_button.grid(row=5, column=0, columnspan=4, pady=5)

# Check for updates when the application starts
check_for_updates()

# Start the GUI event loop
root.mainloop()
