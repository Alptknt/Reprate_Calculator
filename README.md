# Reprate Calculator

A desktop application built with Python and Tkinter for calculating oscillator cavity frequencies, repetition rates, and fiber cavity lengths.  
Designed for laser physics applications with fiber + free-space cavities.

## ✨ Features
- Input fiber segment lengths and free-space distances
- Automatic calculation of:
  - Individual fiber delays
  - Total cavity time
  - Oscillator frequency (MHz)
  - Repetition rate multiples (2x, 4x, 8x, 16x) with required fiber lengths
- Adjustable constants for speed of light in glass and air
- Interactive UI with tooltips
- Includes schematic diagram and company branding
- Cross-platform: works on **Windows** and **macOS**

## 📸 Screenshots
*(Add screenshots of your UI here, e.g. `./images/screenshot.png`)*

## 🚀 Installation

### Windows
Download the latest `.exe` from the [Releases](../../releases) page and run directly.

### macOS
Download the latest `.dmg` or `.app` bundle from the [Releases](../../releases).

Or run from source:

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
pip install -r requirements.txt
python main.py
