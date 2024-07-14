import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Initialize the database
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create tasks table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, title TEXT, description TEXT, priority TEXT, due_date TEXT, completed INTEGER)''')
conn.commit()

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("500x400")

        # Title input
        self.title_label = tk.Label(root, text="Task Title")
        self.title_label.pack()
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack()

        # Description input
        self.description_label = tk.Label(root, text="Task Description")
        self.description_label.pack()
        self.description_entry = tk.Entry(root, width=50)
        self.description_entry.pack()

        # Priority input
        self.priority_label = tk.Label(root, text="Task Priority (Low, Medium, High)")
        self.priority_label.pack()
        self.priority_entry = tk.Entry(root, width=50)
        self.priority_entry.pack()

        # Due Date input
        self.due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD)")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(root, width=50)
        self.due_date_entry.pack()

        # Add Task Button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Task List
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
        self.task_listbox.pack()
        self.task_listbox.bind('<Double-1>', self.edit_task)

        # Delete Task Button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        # Mark as Completed Button
        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.pack()

        # Load tasks
        self.load_tasks()

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_entry.get()
        due_date = self.due_date_entry.get()
        
        if not title:
            messagebox.showwarning("Input Error", "Task title is required.")
            return

        # Insert into database
        c.execute("INSERT INTO tasks (title, description, priority, due_date, completed) VALUES (?, ?, ?, ?, ?)",
                  (title, description, priority, due_date, 0))
        conn.commit()
        
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        
        self.load_tasks()

    def edit_task(self, event):
        selected_task = self.task_listbox.get(self.task_listbox.curselection())
        task_id = selected_task.split('.')[0]

        c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
        task = c.fetchone()

        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, task[1])
        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, task[2])
        self.priority_entry.delete(0, tk.END)
        self.priority_entry.insert(0, task[3])
        self.due_date_entry.delete(0, tk.END)
        self.due_date_entry.insert(0, task[4])

        def save_changes():
            new_title = self.title_entry.get()
            new_description = self.description_entry.get()
            new_priority = self.priority_entry.get()
            new_due_date = self.due_date_entry.get()

            c.execute("UPDATE tasks SET title=?, description=?, priority=?, due_date=? WHERE id=?",
                      (new_title, new_description, new_priority, new_due_date, task_id))
            conn.commit()

            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
            
            self.load_tasks()
            self.save_button.pack_forget()

        self.save_button = tk.Button(self.root, text="Save Changes", command=save_changes)
        self.save_button.pack()

    def delete_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            task_id = selected_task.split('.')[0]

            c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            conn.commit()
            
            self.load_tasks()
        except tk.TclError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_as_completed(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            task_id = selected_task.split('.')[0]

            c.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
            conn.commit()
            
            self.load_tasks()
        except tk.TclError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        
        for row in c.execute("SELECT * FROM tasks"):
            task_status = "Completed" if row[5] else "Active"
            self.task_listbox.insert(tk.END, f"{row[0]}. {row[1]} [{task_status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
    conn.close()

