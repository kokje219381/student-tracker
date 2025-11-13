# TODO: Student Attendance Tracker App

## Steps to Complete

- [x] Update file.py to integrate Tkinter GUI for input and summary display
  - Import tkinter and datetime
  - Create main window with title "Student Attendance Tracker"
  - Add labels and entry fields for student name and time (HH:MM)
  - Add "Add Entry" button to validate and store attendance
  - Add "Generate Summary" button to display formatted summary in a text area
  - Adapt input_attendance and attendance_summary functions to work with GUI elements
  - Ensure validation for name (alphabetic) and time (HH:MM format)
  - Store data in attendance_list (list of tuples) and attendance_dict (dict of lists)

- [x] Test the GUI app locally by running the script

- [x] Install PyInstaller if not already installed (pip install pyinstaller)

- [x] Build standalone executable using PyInstaller (pyinstaller --onefile file.py)

- [x] Verify the generated .exe file runs independently without Python installation

- [x] Perform thorough GUI testing: Add entries, validate inputs, generate summary, test edge cases
