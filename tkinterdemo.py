import tkinter as tk
from tkinter import messagebox


class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Demo")

        # Label Widget
        self.label = tk.Label(root, text="Enter Your Name:", font=("Arial", 14))
        self.label.pack(pady=50,padx=100)

        # Entry Widget
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=60)

        # Button Widget
        self.button = tk.Button(root, text="Submit", font=("Arial", 14), command=self.display_name)
        self.button.pack(pady=5)

        # Checkbutton Widget
        self.check_var = tk.IntVar()
        self.check = tk.Checkbutton(root, text="Subscribe to Newsletter", font=("Arial", 12), variable=self.check_var)
        self.check.pack(pady=5)

        # Radiobutton Widget
        self.gender_var = tk.StringVar(value="None")
        tk.Label(root, text="Select Gender:", font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Male", variable=self.gender_var, value="Male").pack()
        tk.Radiobutton(root, text="Female", variable=self.gender_var, value="Female").pack()

        # Listbox Widget
        self.listbox = tk.Listbox(root, height=3)
        for item in ["Python", "Java", "C++"]:
            self.listbox.insert(tk.END, item)
        self.listbox.pack(pady=5)

        # Quit Button
        self.quit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit)
        self.quit_button.pack(pady=10)

    def display_name(self):
        """Handles button click and displays user input."""
        name = self.entry.get()
        subscribed = "Yes" if self.check_var.get() else "No"
        gender = self.gender_var.get()
        selected_lang = self.listbox.get(tk.ACTIVE) if self.listbox.curselection() else "None"

        messagebox.showinfo("User Info",
                            f"Name: {name}\nSubscribed: {subscribed}\nGender: {gender}\nLanguage: {selected_lang}")


# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
