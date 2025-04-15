# 🎮 Tetris in PyGame

A simple, visually appealing Tetris clone built using Python and PyGame. This version includes responsive controls, increasing difficulty based on score, and custom block textures for a polished look.

---

## 📸 Preview

![Tetris Screenshot](assets/preview.png) <!-- Add your own screenshot here -->

---

## 🧠 Features

- Classic Tetris gameplay mechanics  
- Custom graphics for blocks  
- Increasing difficulty with level progression  
- Smooth keyboard controls  
- Game over menu with restart and quit options  
- Next block preview panel  
- Score and level display  

---

## 🛠 Requirements

- Python 3.x  
- [PyGame](https://www.pygame.org/) (`pip install pygame`)  

---

## 🚀 How to Run

1. Clone or download this repository:

   ```bash
   git clone https://github.com/yourusername/tetris-pygame.git
   cd tetris-pygame
   ```


2. Install PyGame:
   
   ```bash 
   pip install pygame
   ```

3. Run the game:

    ```bash
    python tetris.py
    ```


## 🎮 Controls

## 📁 Project Structure
    ```bash 
            tetris/
        │
        ├── assets/
        │   ├── 1.png
        │   ├── 2.png
        │   ├── 3.png
        │   ├── 4.png
        │
        ├── tetris.py          # Main game file
        ├── README.md
    ```

        

## 🧩 Game Logic

* The game board is a grid calculated based on cell size.

* Shapes are randomly selected and rotated using defined configurations.

* Collision detection ensures valid block placement.

* Rows are cleared when filled, with scoring and level mechanics.

* The game speeds up as the player's level increases.

## 💡 Customization

* Update block visuals in the assets/ folder to change appearance.

* Modify WIDTH, HEIGHT, or CELL in tetris.py to adjust board size or cell scaling.



