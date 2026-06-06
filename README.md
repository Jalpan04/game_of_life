# **Conway's Game of Life 🧬**

![GitHub top language](https://img.shields.io/github/languages/top/Jalpan04/game_of_life) ![GitHub repo size](https://img.shields.io/github/repo-size/Jalpan04/game_of_life) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
A Python implementation of John Conway's Game of Life using `pygame`. This simulation of cellular automata follows simple rules to create complex, evolving patterns.

---

## **Features 🚀**
👉 **Interactive Grid** – Click to toggle cell states.  
👉 **Dynamic Resizing** – Zoom in and out with the scroll wheel.  
👉 **Simulation Control** – Start, pause, and clear the grid with keyboard shortcuts.  
👉 **Help Screen** – Detailed instructions displayed on startup.  
👉 **Customizable** – Easily adjust grid size, colors, and speed.

---

## **Installation 🛠**
### **Prerequisites**
- Python **3.6+** installed  
- `pygame` and `numpy` libraries

### **Setup**
```bash
git clone <repository_url>
cd <repository_folder>
pip install -r requirements.txt
python game_of_life.py
```

---

## **Usage 🎮**
### **Keyboard Controls**
| Key       | Action                        |
|-----------|------------------------------|
| `Space`   | Start/Pause simulation       |
| `Ctrl+C`  | Clear the grid               |
| `Enter`   | Start simulation from help screen |
| `Esc`     | Exit the game                |

### **Mouse Controls**
| Action | Description |
|--------|------------|
| **Left Click**  | Toggle cell state (alive/dead) |
| **Scroll Up**   | Zoom in (increase cell size) |
| **Scroll Down** | Zoom out (decrease cell size) |

---

## **Screenshots & Video 🎥**
### **Screenshots**
#### Initial Help Screen
<a href="static/Initial%20Help%20Screen.png"><img src="static/Initial%20Help%20Screen.png" width="300"></a>

#### Grid with Randomized Cells
<a href="static/Grid%20with%20Randomized%20Cells.png"><img src="static/Grid%20with%20Randomized%20Cells.png" width="300"></a>

#### Paused State
<a href="static/Paused%20State%20.png"><img src="static/Paused%20State%20.png" width="300"></a>

#### Zoomed-In View
<a href="static/Zoomed-In%20View.png"><img src="static/Zoomed-In%20View.png" width="300"></a>

### **Video Preview**
[![Simulation Running](static/Simulation%20Running.gif)](static/Simulation%20Running.gif)

_(For the best experience, play the video to see the simulation in action.)_

---

## **Customization 🎨**
- **Cell Size:** Change `DEFAULT_CELL_SIZE` in the script.
- **Speed:** Adjust `clock.tick(10)` to control simulation speed.
- **Colors:** Modify `BLACK`, `WHITE`, `GRAY`, etc., for a different theme.

---

## **Contributing 🤝**
Feel free to fork and improve this project. PRs are welcome!

---

