# 🔄 Git Conflict Resolver

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An elegant, interactive tool I developed for the Git-A-Head workshop to help students resolve Git conflicts through a user-friendly graphical interface.

## ✨ Features
- 📊 Side-by-side view of conflicting versions
- 🎯 Intuitive interface for version selection
- 🔄 Smart navigation between conflicting files
- 💾 One-click save functionality
- 🔄 Real-time conflict status updates

## 📋 Requirements
- Python 3.x
- tkinter (included with Python)
- Git

## 🚀 Quick Start
1. Run the tool when encountering Git conflicts:
   ```bash
   python resolver.py
   ```

2. The interface displays three panels:
   ```
   +----------------+----------------+----------------+
   |    Current    |     Final     |   Incoming    |
   |    Version    |    Version    |    Version    |
   |     (LEFT)    |   (MIDDLE)    |    (RIGHT)    |
   +----------------+----------------+----------------+
   ```

3. Resolution workflow:
   - Review both versions
   - Choose a version or create custom
   - Save your resolution
   - Move to next conflict

## 🎮 Controls
| Button | Action |
|--------|--------|
| Use Current | Select current version |
| Use Incoming | Select incoming version |
| Save Resolution | Save the solution |
| Next/Previous | Navigate conflicts |
| Refresh | Update status |

## 💡 Tips
- Review both versions carefully before deciding
- Use custom resolution for complex conflicts
- Save frequently to avoid losing work
- Check status bar for current file info

## 🤝 Contributing
Found a bug or have a suggestion? Feel free to:
- Open an issue
- Submit a pull request
- Suggest improvements

Visit the [main repository](https://github.com/AmirHaytham/git-a-head) for more information.

---
<p align="center">
Created by <a href="https://github.com/AmirHaytham">Amir Haytham</a> for the Git-A-Head Workshop
</p>
