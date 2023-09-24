import tkinter as tk
from datetime import datetime


def save_note():
    note = text.get("1.0", tk.END).strip()  # Get the content of the text widget
    if note:
        timestamp = datetime.now().strftime('[%H:%M]')
        formatted_note = f"{timestamp} {note}\n"

        today = datetime.today().strftime('%Y-%m-%d')
        notes_path = f"{today}.txt"

        with open(notes_path, 'a') as file:
            file.write(formatted_note)
            text.delete("1.0", tk.END)  # Clear the text widget


app = tk.Tk()
app.title("Simple Note-taking App")

label = tk.Label(app, text="Enter your note:")
label.pack()

# Create a Text widget with a larger height
text = tk.Text(app, width=50, height=10, font=('Arial', 12))
text.pack(pady=10)  # Increased vertical padding

save_button = tk.Button(app, text="Save Note", command=save_note)
save_button.pack()

app.mainloop()
