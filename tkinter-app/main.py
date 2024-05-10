import tkinter as tk
from tkinter import messagebox
import calculation

def validate_input():
    # Reset field colors
    for entry in entry_fields:
        entry.configure(bg="white")

    # Check if any input field is empty or non-numeric
    for i, entry in enumerate(entry_fields):
        value = entry.get()
        if value == "":
            entry.configure(bg="red")
            messagebox.showerror("Error", "Please enter all information.")
            return False
        elif not value.replace('.', '', 1).isdigit():  # Check if value is numeric
            entry.configure(bg="red")
            messagebox.showerror("Error", "Please enter numeric values only.")
            return False

    return True

def calculate_result():
    # Validate the input
    if not validate_input():
        return

    # Retrieve the input values
    input_values = [entry.get() for entry in entry_fields]

    # Call the function from calculation.py
    result = calculation.process_inputs(input_values)

    # Update the weather label
    weather_label.configure(text="Weather: " + result)

# Create the Tkinter app window
window = tk.Tk()
window.title("Weather Prediction App")

# Create input fields
entry_fields = []
input_names = ["Date (yyyy-mm-dd)", "Precipitation", "Temp Max", "Temp Min", "Wind"]
for i, name in enumerate(input_names):
    label = tk.Label(window, text=name + ":")
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry_fields.append(entry)

# Create a button to calculate the result
calculate_button = tk.Button(window, text="Predict", command=calculate_result)
calculate_button.configure(bg="blue", fg="white")  # Set background color to blue and foreground (text) color to white
calculate_button.grid(row=len(input_names), columnspan=2, padx=10, pady=10)

# Create a label to display the weather
weather_label = tk.Label(window, text="Weather: ")
weather_label.grid(row=len(input_names) + 1, columnspan=2, padx=10, pady=5)

# Start the Tkinter event loop
window.mainloop()
