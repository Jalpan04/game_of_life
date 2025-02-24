# **Conway's Game of Life 🧬**
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
![Initial Help Screen](static/Initial%20Help%20Screen.png)

#### Grid with Randomized Cells
![Grid with Randomized Cells](static/Grid%20with%20Randomized%20Cells.png)

#### Paused State
![Paused State](static/Paused%20State%20.png)

#### Zoomed-In View
![Zoomed-In View](static/Zoomed-In%20View.png)

### **Video Preview**
[Simulation Running](static/Simulation%20Running.gif)

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
