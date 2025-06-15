#Write py functions that calculate certain fiber characteristics based on prompt.
import numpy as np
import tkinter as tk
from tkinter import ttk

angl_deg = 45
angl_rad = np.radians(angl_deg)
ans = round(angl_rad,4)

#print(f"{round(np.sin(np.radians(45)),4)}")
print(ans)


# Main window creation
root = tk.Tk()
root.title("Simple OptFiber Calculator")
root.geometry("300x200") # Set initial window size

# Function to update the label when a new item is selected in the dropdown
def on_dropdown_select(event):
    selected_item = dropdown_var.get()
    status_label.config(text=f"Selected: {selected_item}")

# --- Labels ---
# Label 1: A simple static label
label1 = tk.Label(root, text="Choose an option from the dropdown:", font=("Arial", 12))
label1.pack(pady=10) # Add some padding

# Label 2: A label to display the selected item from the dropdown
status_label = tk.Label(root, text="Selected: None", font=("Arial", 10), fg="blue")
status_label.pack(pady=5)

# --- Dropdown (Combobox) ---
# Create a Tkinter variable to hold the selected value
dropdown_var = tk.StringVar()

# Define the options for the dropdown
options = ["Numerical Aperature", "Mode-Field Size", "Attenuation", "Critical Angle"]

# Create the Combobox widget
# textvariable: links the combobox's value to dropdown_var
# values: provides the list of options
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=options, state="readonly")
dropdown.set("Select an option") # Set initial placeholder text
dropdown.pack(pady=5)

# Bind the selection event to the function
dropdown.bind("<<ComboboxSelected>>", on_dropdown_select)

# Label 3: Another static label
label3 = tk.Label(root, text="This is another informative label.", font=("Arial", 10), fg="gray")
label3.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()