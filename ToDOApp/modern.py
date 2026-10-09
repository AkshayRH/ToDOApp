from tkinter import *
import customtkinter as ck

ck.set_appearance_mode("System")
ck.set_default_color_theme("blue")
app = ck.CTk()

def click():
    print("Clicked")

app.geometry('800x600') 

button = ck.CTkButton(
    app,
    text="Click Me",
    fg_color="#F3E3D0",
    text_color="#152034",
    hover_color="#00aaa0",
    border_width=2,
    border_color="#5e87b8",
    cursor="hand2",
    command=click
)
button.pack(pady=50, expand=True)

app.mainloop()
