# Git Visualizer Pro
## Interactive Git Repository Visualization Tool

### 🎯 Features
- Interactive graph visualization of Git history
- Branch and commit visualization
- Commit details display
- Real-time updates
- Branch filtering

### 📋 Requirements
- Python 3.7+
- NetworkX
- Matplotlib
- Tkinter

### 🚀 Installation
```bash
# Install dependencies
pip install -r requirements.txt
```

### 💻 Usage
```bash
# Run the visualizer
python visualizer.py
```

### 🎮 Controls
1. **Refresh Button**: Updates the graph with latest repository changes
2. **Branch Filter**: Filter commits by branch
3. **Graph Interaction**: 
   - Zoom: Mouse wheel
   - Pan: Click and drag
   - Select: Click on commit node

### 🔍 Visualization Elements
- **Nodes**: Represent commits
- **Edges**: Show parent-child relationships
- **Colors**: Indicate different branches
- **Labels**: Show commit messages and hashes

### 💡 Tips
1. Keep window size reasonable for best visualization
2. Use branch filter for complex repositories
3. Hover over nodes to see full commit details
4. Regular refresh recommended for active repositories
