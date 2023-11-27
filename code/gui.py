# MIT License
#
# Copyright (c) 2023 Amogh Mahesh and others
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as tk
from tkinter import ttk
import subprocess
import re


def execute_gits_command():
    command = command_entry.get()
    command = re.findall(r'[^"\s]+|"[^"]*"', command)
    # print(command)
    command_list = ['python']
    for sub_c in command:
        command_list.append(sub_c)

    try:
        # Execute the GITS command and capture the output
        result = subprocess.check_output(command_list, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)  # Clear previous output
        result_text.insert(tk.END, result)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        print("error here")
        result_text.insert(tk.END, "Error: " + e.output)
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "An error occurred: " + str(e))


# Create the main window
window = tk.Tk()
window.title("GITS GUI")

# # Set the window size and position
# window.geometry("600x400")
# window.resizable(False, False)  # Disable window resizing

# Load a GITS logo (replace 'gits_logo.png' with your actual logo file)
logo_image = tk.PhotoImage(file='../gits-logo.png').subsample(2, 2)
logo_label = tk.Label(window, image=logo_image)
logo_label.pack(pady=10)

# Create a label for GITS commands
command_label = tk.Label(window, text="Enter GITS Command:", font=("Arial", 14))
command_label.pack()
example_label = tk.Label(window, text="Eg: commit -m '<message>'", font=("Arial", 12))
example_label.pack()

# Create an entry for GITS commands with a border
command_entry = tk.Entry(window, font=("Arial", 12), relief="solid", borderwidth=2)
command_entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create a button to execute commands with a nice style
execute_button = tk.Button(window, text="Execute GITS Command", command=execute_gits_command, font=("Arial", 14))
execute_button.pack(pady=10)

# Create a text widget to display the results with a border
result_text = tk.Text(window, height=10, width=60, font=("Arial", 12), relief="solid", borderwidth=2)
result_text.pack(padx=10, fill=tk.BOTH, expand=True)

# Configure a scrollbar for the text widget
scrollbar = ttk.Scrollbar(window, orient="vertical", command=result_text.yview)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Run the GUI
window.mainloop()
