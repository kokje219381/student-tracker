import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re

# Data structures
attendance_list = []  # List of tuples: (name, timestamp)
attendance_dict = {}  # Dict: name -> list of timestamps

def validate_name(name):
    """Validate that name is alphabetic and not empty."""
    return name.isalpha() and len(name.strip()) > 0

def validate_time(time_str):
    """Validate time in HH:MM format."""
    pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
    return re.match(pattern, time_str) is not None

def add_entry():
    name = name_entry.get().strip()
    time_str = time_entry.get().strip()

    if not validate_name(name):
        messagebox.showerror("Invalid Input", "Name must be alphabetic and not empty.")
        return

    if not validate_time(time_str):
        messagebox.showerror("Invalid Input", "Time must be in HH:MM format (e.g., 14:30).")
        return

    # Create timestamp
    try:
        timestamp = datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid time format.")
        return

    # Store in list and dict
    attendance_list.append((name, timestamp))
    if name not in attendance_dict:
        attendance_dict[name] = []
    attendance_dict[name].append(timestamp)

    # Clear entries
    name_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Entry added successfully!")

def generate_summary():
    if not attendance_list:
        summary_text.delete(1.0, tk.END)
        summary_text.insert(tk.END, "No attendance entries yet.")
        return

    summary = "Attendance Summary:\n\n"
    summary += f"Total Entries: {len(attendance_list)}\n\n"

    for name, timestamps in attendance_dict.items():
        summary += f"Student: {name}\n"
        summary += f"Attendance Count: {len(timestamps)}\n"
        summary += "Timestamps: " + ", ".join([t.strftime("%H:%M") for t in sorted(timestamps)]) + "\n\n"

    summary_text.delete(1.0, tk.END)
    summary_text.insert(tk.END, summary)

# GUI Setup
root = tk.Tk()
root.title("Student Attendance Tracker")

# Labels and Entries
tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Time (HH:MM):").grid(row=1, column=0, padx=10, pady=5)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

summary_button = tk.Button(root, text="Generate Summary", command=generate_summary)
summary_button.grid(row=3, column=0, columnspan=2, pady=10)

# Text Area for Summary
summary_text = tk.Text(root, height=10, width=50)
summary_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
