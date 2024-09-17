import tkinter as tk
import PIL
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title("Heidy's Pet")
root.geometry("50x50")
# Removes window border and title bar
root.overrideredirect(True)

# Load and display pet
pet_image = Image.open("/Users/heidyhernandez/Desktop/cutepet/pet.png")
pet_image = pet_image.resize((50,50), PIL.Image.LANCZOS)
pet_photo = ImageTk.PhotoImage(pet_image)

label = tk.Label(root, image=pet_photo, bg="white")
label.pack()
def move_pet():
    y= root.winfo_y()
    x = random.randint(0, root.winfo_screenwidth() - 50)

    # Move the window to the new Y position (X remains the same)
    root.geometry(f"50x50+{x}+{y}")
    
    # Schedule the next move after 1 second
    root.after(100000, move_pet)
    """
    x = random.randint(0, root.winfo_screenwidth() - 50)
    y = random.randint(0, root.winfo_screenheight() - 50)
    root.geometry(f"50x50+{x}+{y}")
    root.after(1000, move_pet)  # Move the pet every second
    """
    
#Function to move the window
def move_start(event):
    root.x = event.x
    root.y = event.y

def move_drag(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f'+{x}+{y}')

def cute_messages(event):
    messages = [
        "You are so smart",
        "I love you so much",
        "You are the best",
        "I'm so lucky to have you",
        "You make me happy",
        "You are doing amazing sweetheart"
    ]
    message = random.choice(messages)
    note = tk.Toplevel(root)
    note.geometry("200x100")
    note.title("A Cute Note")
    note_label = tk.Label(note, text=message, font=("Arial", 14))
    note_label.pack(expand=True)

    note.attributes('-topmost', True)  # Ensure the note window appears on top

    # Position the message window near the pet
    x = root.winfo_x() + 50  # Adjust position to be slightly to the right of the pet
    y = root.winfo_y() + 50  # Adjust position to be slightly below the pet
    note.geometry(f"200x100+{x}+{y}")
    
    note.after(2000, note.destroy)  # Close the note after 2 seconds


# label.bind('<Button-1>', move_start)
#label.bind('<B1-Motion>', move_drag)

move_pet()

# Bind the cute_notes function to double-click events
label.bind('<Double-Button-1>', cute_messages)

root.mainloop()