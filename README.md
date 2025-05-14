# Mazed GameEngine

This is a **minimal game engine prototype** built using **PyOpenGL** and **Pygame**. It's currently a work-in-progress and serves as a starting point for learning and experimenting with OpenGL in Python.

---

## Features

- Window creation and context management with Pygame
- Basic OpenGL rendering with PyOpenGL
- Modular, object-oriented architecture
- A foundation for building 3D games or rendering engines
- **Includes a simple Maze Game** built using the engine framework

---

## Setup Instructions

> ✅ **Recommended**: Use a Python virtual environment to isolate dependencies.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/minimal-game-engine.git
cd minimal-game-engine
```
### 2. Create and Activate a Virtual Environment
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
###On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
### 3.Installing Dependencies
With the virtual environment activated, install all required dependencies by running:

```bash
pip install -r requirements.txt
```
### This will install the necessary packages, including:

pygame

PyOpenGL

PyOpenGL_accelerate (optional but improves performance)

other lib

Running the Engine
To launch the base engine or any demo project:

```bash
python MazedEngine/mazed.py
```

⚠️ Make sure your system supports OpenGL and you have the necessary graphics drivers installed.
