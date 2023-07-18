import sqlite3
from tkinter import *
import tkinter as tk
# Create database
conn = sqlite3.connect('passwords.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (password TEXT)''')

# Generate list of possible passwords
passwords = []
for i in range(100000):
    password = str(i).zfill(4)
    passwords.append(password)

c.execute("insert into passwords values(1738)")
# Brute force algorithm to crack the password
def crack_password(display):
    for i,password in enumerate(passwords):
      #if i%100==0:
        display.insert(tk.END, f"iteration {password}\n")
    
        c.execute("SELECT * FROM passwords WHERE password=?", (password,))
        result = c.fetchone()
        if result:
            return password
        
c.execute("SELECT * FROM passwords")
# GUI interface to enter password and display result
def main():
    root = Tk()
    root.geometry("300x300")
    root.title("Password Cracker")

    # Button to crack password
    crack_button = tk.Button(root, text="Crack Password", command=lambda:get_result())
    crack_button.pack()
    # Label to display result
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)
    display=tk.Text(root)
    display.pack()
     

    # Function to get result and display in label
    def get_result():
        result = crack_password(display)
        if result:
            result_label.configure(text="The password is: " + result)
        else:
            result_label.configure(text="Password not found.")
    

    root.mainloop()

if __name__ == "__main__":
    main()