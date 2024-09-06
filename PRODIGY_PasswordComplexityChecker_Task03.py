# Importing necessary libraries
import re
import tkinter as tk
from tkinter import messagebox
from typing import Tuple, List

# Creating the PasswordStrengthChecker class to check the strength of a password
class PasswordStrengthChecker:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def assess_password_strength(self, password: str) -> Tuple[str, List[str]]:
        if not isinstance(password, str):
            raise ValueError("Password must be a string.")

        # Initialize score and feedback list
        score = 0
        feedback = []

        # Check for length
        if len(password) >= self.min_length:
            score += 1
        else:
            feedback.append(f"Password should be at least {self.min_length} characters long.")

        # Check for uppercase letters
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Password should contain at least one uppercase letter.")

        # Check for lowercase letters
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Password should contain at least one lowercase letter.")

        # Check for digits
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Password should contain at least one number.")

        # Check for special characters
        if re.search(r'[\W_]', password):
            score += 1
        else:
            feedback.append("Password should contain at least one special character.")

        # Determine strength based on score
        if score == 5:
            return "Password is strong!", feedback
        elif 3 <= score < 5:
            return "Password is medium.", feedback
        else:
            return "Password is weak.", feedback

# Creating the PasswordStrengthApp class to implement the GUI with Tkinter
class PasswordStrengthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")

        # Add labels, entry, and button
        self.label = tk.Label(root, text="Enter your password:")
        self.label.pack(pady=10)

        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack(pady=10, padx=30)

        self.check_button = tk.Button(root, text="Check Strength", command=self.check_password_strength)
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", fg="red", justify="left")
        self.feedback_label.pack(pady=10)

        self.again_button = tk.Button(root, text="Check Another Password", command=self.reset)
        self.again_button.pack(pady=10)
        self.again_button.config(state="disabled")

    def check_password_strength(self):
        password = self.password_entry.get()
        checker = PasswordStrengthChecker(min_length=8)
        strength, feedback = checker.assess_password_strength(password)

        # Display strength
        self.result_label.config(text=f"Password Strength: {strength}")

        # Display feedback
        if feedback:
            feedback_text = "\n".join(f"- {f}" for f in feedback)
            self.feedback_label.config(text=f"Feedback:\n{feedback_text}")
        else:
            self.feedback_label.config(text="Great job! Your password meets all the criteria.")

        # Enable the check again button
        self.again_button.config(state="normal")

    def reset(self):
        # Reset the form for another check
        self.password_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.feedback_label.config(text="")
        self.again_button.config(state="disabled")

# Main Tkinter loop to start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthApp(root)
    root.mainloop()
