import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd  # NEW: pandas

window = tk.Tk()
window.title("Student Report Card Generator")
window.geometry("300x350")

tk.Label(window, text="Student Name:").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Math Marks:").pack()
entry_math = tk.Entry(window)
entry_math.pack()

tk.Label(window, text="Science Marks:").pack()
entry_science = tk.Entry(window)
entry_science.pack()

tk.Label(window, text="English Marks:").pack()
entry_english = tk.Entry(window)
entry_english.pack()

# File path
filename = "report_cards.csv"  # changed to .csv (pandas works better with CSV)

# Save student data
def submit():
    name = entry_name.get()
    try:
        math = int(entry_math.get())
        science = int(entry_science.get())
        english = int(entry_english.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid marks (numbers).")
        return

    # Create a DataFrame with one row
    new_data = pd.DataFrame([[name, math, science, english]], 
                            columns=["Name", "Math", "Science", "English"])

    try:
        # If file exists, append without header
        new_data.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
    except:
        messagebox.showerror("Error", "Failed to save data.")
        return

    messagebox.showinfo("Success", "Student data saved successfully!")


# Plot analysis using pandas
def analyze():
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found.")
        return
    except pd.errors.EmptyDataError:
        messagebox.showinfo("No Data", "The file is empty.")
        return

    if df.empty:
        messagebox.showinfo("No Data", "No student data to analyze.")
        return

    names = df["Name"]
    math = df["Math"]
    science = df["Science"]
    english = df["English"]

    # --- BAR CHART (per subject per student) ---
    x = range(len(names))
    plt.figure(figsize=(10, 6))
    plt.bar([i - 0.2 for i in x], math, width=0.2, label="Math")
    plt.bar(x, science, width=0.2, label="Science")
    plt.bar([i + 0.2 for i in x], english, width=0.2, label="English")
    plt.xticks(x, names)
    plt.ylabel("Marks")
    plt.title("Student Performance Comparison")
    plt.legend()
    plt.tight_layout()
    plt.show()

# --- GUI Buttons ---

tk.Button(window, text="Submit", command=submit, bg="lightgreen").pack(pady=10)
tk.Button(window, text="Analyze & Plot", command=analyze, bg="lightblue").pack(pady=5)

window.mainloop()