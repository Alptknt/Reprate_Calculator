# # ==============================
# # Developed by Alptekin Tanatar
# # ==============================

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import config as conf
from about import build_about_tab

# ==============================
# Tooltip class
# ==============================
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            tw,
            text=self.text,
            justify='left',
            background="#ffffe0",
            relief='solid',
            borderwidth=1,
            font=("Open Sans", 10)
        )
        label.pack(ipadx=5, ipady=3)

    def hide_tip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

# ==============================
# Main Window
# ==============================
root = tk.Tk()
root.title(conf.WINDOW_TITLE)
root.geometry(conf.WINDOW_SIZE)
root.resizable(*conf.WINDOW_RESIZABLE)

# Load your logo
logo_img = Image.open("Lumos_Logo_32x32.png")  # your 32x32 logo
logo_icon = ImageTk.PhotoImage(logo_img)

# Set as window icon
root.iconphoto(False, logo_icon)

# Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

oscillator_frame = tk.Frame(notebook, width=1280, height=720)

about_frame = tk.Frame(notebook, width=1280, height=720)
notebook.add(about_frame, text="About")
about_frame.pack_propagate(False)

# Only build the About tab content when it's selected
def on_tab_changed(event):
    selected = event.widget.index("current")
    # Assuming 'About' tab is the second tab (index 1)
    if selected == 1 and not hasattr(about_frame, 'built'):
        build_about_tab(about_frame)
        about_frame.built = True  # prevent rebuilding every time

notebook.bind("<<NotebookTabChanged>>", on_tab_changed)


# Add tabs
notebook.add(about_frame, text="About")
notebook.add(oscillator_frame, text="Oscillator Frequency")
oscillator_frame.pack_propagate(False)
about_frame.pack_propagate(False)

# Set default tab
notebook.select(1)  # Open "Oscillator Frequency" by default

oscillator_frame.pack_propagate(False)
about_frame.pack_propagate(False)

# Left and Right Frames
left_frame = tk.Frame(oscillator_frame, width=600, height=720)
left_frame.pack(side="left", fill="both")
left_frame.pack_propagate(False)

right_frame = tk.Frame(oscillator_frame, width=680, height=720)
right_frame.pack(side="right", fill="both")
right_frame.pack_propagate(False)

# Vertical Divider
divider = tk.Frame(oscillator_frame, width=2, bg="#A0A0A0")
divider.place(x=conf.MID_DIV_X_POS, y=50, height=620)

# Constants
c_fiber_val = tk.DoubleVar(value=conf.C_FIBER_DEFAULT)
c_air_val   = tk.DoubleVar(value=conf.C_AIR_DEFAULT)

# ==============================
# Left Side: Fiber Section
# ==============================
header_left = tk.Label(left_frame, text="Fiber Cavity Length", font=("Open Sans", 18,"bold"))
header_left.place(relx=0.5, y=20, anchor="n")

fiber_inputs = []
fiber_outputs = []
y_pos = 80

for label_text, default_val in conf.FIBER_SEGMENTS:
    lbl = tk.Label(left_frame, text=f"{label_text} =", font=("Open Sans", 12))
    lbl.place(x=60, y=y_pos)

    entry = tk.Entry(left_frame, font=("Open Sans", 13), width=5, justify="right")
    entry.place(x=180, y=y_pos)
    entry.insert(0, f"{default_val:.1f}")
    fiber_inputs.append(entry)

    unit = tk.Label(left_frame, text="cm", font=("Open Sans", 12))
    unit.place(x=240, y=y_pos)

    if label_text == "WDM":
        v_divider_mid = tk.Frame(left_frame, width=2, bg="#A0A0A0", height=220)
        v_divider_mid.place(x=290, y=80)

    out = tk.Entry(left_frame, font=("Open Sans", 13), width=7, justify="left", state="readonly")
    out.place(x=360, y=y_pos)
    fiber_outputs.append(out)

    unit2 = tk.Label(left_frame, text="ns", font=("Open Sans", 12))
    unit2.place(x=440, y=y_pos)

    y_pos += 40

# Total fiber time
lbl_sum = tk.Label(left_frame, text="Total Time in Fiber   =", font=("Open Sans", 12, "bold"))
lbl_sum.place(x=120, y=y_pos+5)
fiber_sum = tk.Entry(left_frame, font=("Open Sans", 13,"bold"), width=7, justify="left", state="readonly")
fiber_sum.place(x=300, y=y_pos+5)
lbl_unit_sum = tk.Label(left_frame, text="ns", font=("Open Sans", 12, "bold"))
lbl_unit_sum.place(x=380, y=y_pos+5)

y_pos += 45
h_divider2 = tk.Frame(left_frame, height=2, bg="#A0A0A0", width=500)
h_divider2.place(relx=0.5, y=y_pos, anchor="n")
y_pos += 20

# ==============================
# FreeSpace Section
# ==============================
header_fs = tk.Label(left_frame, text="Freespace Cavity Length", font=("Open Sans", 18,"bold"))
header_fs.place(relx=0.5, y=y_pos, anchor="n")
y_pos += 60

lbl_fs = tk.Label(left_frame, text="A to B =", font=("Open Sans", 12))
lbl_fs.place(x=60, y=y_pos)

fs_entry = tk.Entry(left_frame, font=("Open Sans", 13), width=5, justify="left")
fs_entry.place(x=180, y=y_pos)
fs_entry.insert(0, f"{conf.FREE_SPACE_DEFAULT:.1f}")
lbl_fs_unit = tk.Label(left_frame, text="cm", font=("Open Sans", 12))
lbl_fs_unit.place(x=240, y=y_pos)

v_divider_fs = tk.Frame(left_frame, width=2, bg="#A0A0A0", height=40)
v_divider_fs.place(x=290, y=y_pos-5)

fs_out = tk.Entry(left_frame, font=("Open Sans", 13), width=7, justify="left", state="readonly")
fs_out.place(x=360, y=y_pos)
lbl_fs_out = tk.Label(left_frame, text="ns", font=("Open Sans", 12))
lbl_fs_out.place(x=440, y=y_pos)

y_pos += 60
h_divider3 = tk.Frame(left_frame, height=2, bg="#A0A0A0", width=500)
h_divider3.place(relx=0.5, y=y_pos, anchor="n")
y_pos += 50

# ==============================
# Total Cavity Time
# ==============================
lbl_cavity_total = tk.Label(left_frame, text="Total Time in Cavity =", font=("Open Sans", 12, "bold"))
lbl_cavity_total.place(x=120, y=y_pos)

cavity_total = tk.Entry(left_frame, font=("Open Sans", 13,"bold"), width=7, justify="left", state="readonly")
cavity_total.place(x=300, y=y_pos)
lbl_cavity_unit = tk.Label(left_frame, text="ns", font=("Open Sans", 12,"bold"))
lbl_cavity_unit.place(x=380, y=y_pos)

y_pos += 40

# ==============================
# Cavity Frequency
# ==============================
lbl_cavity_freq = tk.Label(left_frame, text="Cavity Frequency =", font=("Open Sans", 13, "bold"))
lbl_cavity_freq.place(x=130, y=y_pos)

cavity_freq = tk.Entry(left_frame, font=("Open Sans", 13,"bold"), width=7, justify="left", state="readonly")
cavity_freq.place(x=300, y=y_pos)

lbl_freq_unit = tk.Label(left_frame, text="MHz", font=("Open Sans", 13,"bold"))
lbl_freq_unit.place(x=380, y=y_pos)

# ==============================
# Right Side
# ==============================
header = tk.Label(right_frame, text="Lightspeed Constants", font=("Open Sans", 18,"bold"))
header.place(relx=0.5, y=20, anchor='n')

# C_fiber
c_fiber_label = tk.Label(right_frame, text="Cglass =", font=("Open Sans", 14))
c_fiber_label.place(x=50, y=80)
c_fiber_entry = tk.Entry(right_frame, font=("Open Sans", 13), width=9, justify="left")
c_fiber_entry.place(x=135, y=80)
c_fiber_entry.insert(0, conf.C_FIBER_DEFAULT)
c_fiber_unit = tk.Label(right_frame, text=" m/s", font=("Open Sans", 14))
c_fiber_unit.place(x=240, y=80)

# C_air
c_air_label = tk.Label(right_frame, text="Cair =", font=("Open Sans", 14))
c_air_label.place(x=conf.RIGHT_MID_X_POS, y=80)
c_air_entry = tk.Entry(right_frame, font=("Open Sans", 13), width=9, justify="left")
c_air_entry.place(x=conf.RIGHT_MID_X_POS + 60, y=80)
c_air_entry.insert(0, conf.C_AIR_DEFAULT)
c_air_unit = tk.Label(right_frame, text=" m/s", font=("Open Sans", 14))
c_air_unit.place(x=conf.RIGHT_MID_X_POS + 160, y=80)

h_divider_r = tk.Frame(right_frame, height=2, bg="#A0A0A0", width=580)
h_divider_r.place(relx=0.5, y=130, anchor="n")

# Image
try:
    img = Image.open(conf.OSC_IMAGE)
    img = img.resize(conf.OSC_IMAGE_SIZE, Image.Resampling.LANCZOS)
    osc_img = ImageTk.PhotoImage(img)

    img_frame = tk.Frame(right_frame, bg="gray", width=conf.OSC_IMAGE_SIZE[0]+4, height=conf.OSC_IMAGE_SIZE[1]+2)
    img_frame.place(x=38, y=400)
    img_frame.pack_propagate(False)

    img_label = tk.Label(img_frame, image=osc_img)
    img_label.image = osc_img
    img_label.pack(expand=True, padx=2, pady=2)
    ToolTip(img_label, "Representation of fiber and free-space cavity of the Oscillator")
except Exception as e:
    error_label = tk.Label(right_frame, text=f"Image not found: {e}", fg="red", font=("Open Sans", 14))
    error_label.place(x=20, y=400)

# ==============================
# Repetition Rate Doubling Section
# ==============================
rep_rate_rows = []

def build_repetition_rate_section_right(parent_frame, start_y):
    labels_text = ["To 2x Repetition Rate", "To 4x Repetition Rate", "To 8x Repetition Rate", "To 16x Repetition Rate","To 32x Repetition Rate"]
    rows = []

    for i, text in enumerate(labels_text):
        y = start_y + i*40
        lbl = tk.Label(parent_frame, text=text, font=("Open Sans", 12))
        lbl.place(x=100, y=y)

        fiber_out = tk.Entry(parent_frame, font=("Open Sans", 13), width=6, justify="left", state="readonly")
        fiber_out.place(x=280, y=y)

        unit_cm = tk.Label(parent_frame, text="cm", font=("Open Sans", 12))
        unit_cm.place(x=340, y=y)

        freq_out = tk.Entry(parent_frame, font=("Open Sans", 13), width=9, justify="right", state="readonly")
        freq_out.place(x=420, y=y)

        unit_mhz = tk.Label(parent_frame, text="MHz", font=("Open Sans", 12))
        unit_mhz.place(x=520, y=y)

        rows.append((fiber_out, freq_out))

    return rows

rep_rate_rows = build_repetition_rate_section_right(right_frame, start_y=150)

# ==============================
# Update function
# ==============================
def update_times(*args):
    try:
        c_fiber = float(c_fiber_entry.get())
        c_air = float(c_air_entry.get())
    except ValueError:
        return

    # --- Fiber calculations ---
    total_time = 0.0
    for entry, out in zip(fiber_inputs, fiber_outputs):
        try:
            length_cm = float(entry.get())
            length_m = length_cm / 100.0
            t = length_m / c_fiber
            t_ns = t * 1e9
            out.config(state="normal")
            out.delete(0, tk.END)
            out.insert(0, f"{t_ns:.5f}")
            out.config(state="readonly")
            total_time += t_ns
        except ValueError:
            pass

    fiber_sum.config(state="normal")
    fiber_sum.delete(0, tk.END)
    fiber_sum.insert(0, f"{total_time:.5f}")
    fiber_sum.config(state="readonly")

    # --- Free-space calculation ---
    fs_time_ns = 0.0
    try:
        fs_len = float(fs_entry.get()) / 100.0
        t_fs = fs_len / c_air
        fs_time_ns = t_fs * 1e9
        fs_out.config(state="normal")
        fs_out.delete(0, tk.END)
        fs_out.insert(0, f"{fs_time_ns:.5f}")
        fs_out.config(state="readonly")
    except ValueError:
        pass

    # --- Total cavity time ---
    cavity_time = total_time + fs_time_ns
    cavity_total.config(state="normal")
    cavity_total.delete(0, tk.END)
    cavity_total.insert(0, f"{cavity_time:.5f}")
    cavity_total.config(state="readonly")

    # --- Cavity frequency ---
    if cavity_time > 0:
        freq_mhz = 1000 / cavity_time
    else:
        freq_mhz = 0.0
    cavity_freq.config(state="normal")
    cavity_freq.delete(0, tk.END)
    cavity_freq.insert(0, f"{freq_mhz:.3f}")
    cavity_freq.config(state="readonly")

    # --- Repetition Rate Doubling Section ---
    try:
        f0 = freq_mhz * 1e6
        for i, (fiber_out, freq_out) in enumerate(rep_rate_rows):
            mult = 2 * (2**i)  # 2,4,8,16
            f_new = f0 * mult
            period_s = 1 / f_new
            fiber_len_m = period_s * c_fiber
            fiber_len_cm = fiber_len_m * 100

            fiber_out.config(state="normal")
            fiber_out.delete(0, tk.END)
            fiber_out.insert(0, f"{fiber_len_cm:.3f}")
            fiber_out.config(state="readonly")

            freq_out.config(state="normal")
            freq_out.delete(0, tk.END)
            freq_out.insert(0, f"{f_new/1e6:.3f}")
            freq_out.config(state="readonly")
    except Exception:
        pass

# --- Bind all relevant input entries ---
for e in fiber_inputs + [fs_entry, c_fiber_entry, c_air_entry]:
    e.bind("<KeyRelease>", lambda event: update_times())

# Initial calculation
update_times()

# Run
root.mainloop()
