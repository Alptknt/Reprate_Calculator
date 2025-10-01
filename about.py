# # ==============================
# # Developed by Alptekin Tanatar
# # ==============================


import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

def build_about_tab(parent_frame):
    # Header
    about_header = tk.Label(parent_frame, text="About This Software", font=("Open Sans", 18, "bold"))
    about_header.pack(pady=20)

    # Description
    about_text = """This software calculates fiber and free-space cavity lengths for oscillator, 
    computes cavity frequency, and provides fiber lenghts for reprate multiplier. Developed and maintained by Lumos Laser."""
    about_label = tk.Label(parent_frame, text=about_text, font=("Open Sans", 12), justify="center")
    about_label.pack(pady=10)


    # GitHub link
    def open_github():
        webbrowser.open("https://github.com/yourusername/yourrepo")

    github_btn = tk.Button(parent_frame, text="GitHub Repository", font=("Open Sans", 12, "underline"), fg="blue", bd=0, cursor="hand2", command=open_github)
    github_btn.pack(pady=5)

    # Company website link
    def open_company():
        webbrowser.open("https://lumoslaser.com/contact/")

    company_btn = tk.Button(parent_frame, text="Company Website", font=("Open Sans", 12, "underline"), fg="blue", bd=0, cursor="hand2", command=open_company)
    company_btn.pack(pady=5)


    # Company logo
    try:
        logo_img = Image.open("Lumos_Laser_Logo_1024x236.png")  # logo path
        logo_img = logo_img.resize((512, 118), Image.Resampling.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(parent_frame, image=logo_photo)
        logo_label.image = logo_photo
        logo_label.pack(pady=10)
    except Exception as e:
        logo_error = tk.Label(parent_frame, text=f"Logo not found: {e}", fg="red", font=("Open Sans", 12))
        logo_error.pack(pady=10)

