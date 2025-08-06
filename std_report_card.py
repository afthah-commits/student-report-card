import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd

# --- Setup ---
window = tk.Tk()
window.title("Student Report Card Generator")
window.geometry("300x350")
filename = "report_cards.csv"

# --- Create Label & Entry ---
def create_entry(label):
    tk.Label(window, text=label).pack()
    e = tk.Entry(window)
    e.pack()
    return e

entry_name = create_entry("Student Name:")
entry_math = create_entry("Math Marks:")
entry_science = create_entry("Science Marks:")
entry_english = create_entry("English Marks:")

# --- Submit Function ---
def submit():
    name = entry_name.get()
    try:
        marks = [int(entry_math.get()), int(entry_science.get()), int(entry_english.get())]
    except ValueError:
        return messagebox.showerror("Input Error", "Enter valid numbers.")

    data = pd.DataFrame([[name] + marks], columns=["Name", "Math", "Science", "English"])
    try:
        data.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
        messagebox.showinfo("Success", "Data saved!")
    except:
        messagebox.showerror("Error", "Could not save data.")

# --- Analyze Function ---
def analyze():
    try:
        df = pd.read_csv(filename)
        if df.empty: raise ValueError
    except FileNotFoundError:
        return messagebox.showerror("Error", "File not found.")
    except:
        return messagebox.showinfo("No Data", "No student data to show.")

    x = range(len(df))
    plt.figure(figsize=(10, 6))
    for i, sub in enumerate(["Math", "Science", "English"]):
        plt.bar([j + (i - 1) * 0.2 for j in x], df[sub], width=0.2, label=sub)
    plt.xticks(x, df["Name"])
    plt.title("Student Marks Comparison")
    plt.ylabel("Marks")
    plt.legend()
    plt.tight_layout()
    plt.show()

# --- Buttons ---
tk.Button(window, text="Submit", command=submit, bg="lightgreen").pack(pady=10)
tk.Button(window, text="Analyze & Plot", command=analyze, bg="lightblue").pack(pady=5)

window.mainloop()