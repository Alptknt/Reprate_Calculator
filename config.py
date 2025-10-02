# # ==============================
# # Developed by Alptekin Tanatar
# # ==============================

#Constants & Defaults (all here)

# --- Window settings ---
WINDOW_TITLE = "Oscillator-Reprate Calculator v1.0"
WINDOW_SIZE = "1280x720"
WINDOW_RESIZABLE = (False, False)

# --- Divider positions ---
MID_DIV_X_POS = 600
LEFT_MID_X_POS = 300
RIGHT_MID_X_POS = 400

# --- Lightspeed constants (in m/s) ---

# https://www.thorlabs.com/thorproduct.cfm?partnumber=SM980G80
# https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=949&pn=SM980G80#1370

C_FIBER_DEFAULT = 205802470 # this more like c in fiber optic derived from n=1.45670 Taken from Link above for SM980 fiber 
C_AIR_DEFAULT   = 299702547 # taken from wikipedia 
C_VAC_DEFAULT   = 299792458 # taken from wikipedia


# --- Default fiber segments (label, default length in cm) ---
FIBER_SEGMENTS = [
    ("WDM", 6.0),
    ("WDM to SP3", 12.0),
    ("SP3 to A", 12.0),
    ("B to SP4", 12.0),
    ("SP4 to SP5", 20.0),
    ("SP5 to WDM", 12.0)
]

# --- Default FreeSpace length (cm) ---
FREE_SPACE_DEFAULT = 18.0

# --- Image ---
OSC_IMAGE = "Osc_Diagram.png"
OSC_IMAGE_SIZE = (600, 260)
