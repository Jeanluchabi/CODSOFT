import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3
import random
import os

# Connect to the SQLite database
conn = sqlite3.connect('quotes.db')
c = conn.cursor()

# Create tables if they do not exist
c.execute('''CREATE TABLE IF NOT EXISTS quotes
             (id INTEGER PRIMARY KEY, quote TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS favorites
             (id INTEGER PRIMARY KEY, quote TEXT)''')
conn.commit()

# Here, you can add some sample quotes
sample_quotes = [
    "The best way to get started is to quit talking and begin doing. - Walt Disney",
    "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. - Winston Churchill",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "You learn more from failure than from success. Don't let it stop you. Failure builds character. - Unknown",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi"
]

# Check if quotes are already in the database
c.execute("SELECT COUNT(*) FROM quotes")
if c.fetchone()[0] == 0:
    c.executemany("INSERT INTO quotes (quote) VALUES (?)", [(quote,) for quote in sample_quotes])
    conn.commit()

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inspiring Quotes")
        self.root.geometry("600x400")

        self.quote_label = tk.Label(root, text="", wraplength=500, justify=tk.CENTER, font=("Arial", 14))
        self.quote_label.pack(pady=20)

        self.favorite_button = tk.Button(root, text="Favorite", command=self.favorite_quote)
        self.favorite_button.pack(pady=5)

        self.share_button = tk.Button(root, text="Share", command=self.share_quote)
        self.share_button.pack(pady=5)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.display_quote)
        self.refresh_button.pack(pady=5)

        self.view_favorites_button = tk.Button(root, text="View Favorites", command=self.view_favorites)
        self.view_favorites_button.pack(pady=5)

        self.display_quote()

    def display_quote(self):
        c.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
        self.current_quote = c.fetchone()
        self.quote_label.config(text=self.current_quote[1])

    def favorite_quote(self):
        c.execute("INSERT INTO favorites (quote) VALUES (?)", (self.current_quote[1],))
        conn.commit()
        messagebox.showinfo("Favorite", "Quote added to favorites!")

    def share_quote(self):
        pyperclip.copy(self.current_quote[1])
        messagebox.showinfo("Share", "Quote copied to clipboard! Share it with others.")

    def view_favorites(self):
        favorites_window = tk.Toplevel(self.root)
        favorites_window.title("Favorite Quotes")
        favorites_window.geometry("600x400")

        c.execute("SELECT * FROM favorites")
        favorites = c.fetchall()

        for favorite in favorites:
            favorite_label = tk.Label(favorites_window, text=favorite[1], wraplength=500, justify=tk.LEFT, font=("Arial", 12))
            favorite_label.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()
    conn.close()

