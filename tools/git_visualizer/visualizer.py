import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess
import json

class GitVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Git Visualizer Pro")
        
        # Setup main container
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create graph
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=2)
        
        # Controls
        self.controls_frame = ttk.LabelFrame(self.main_frame, text="Controls", padding="5")
        self.controls_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Refresh button
        self.refresh_btn = ttk.Button(self.controls_frame, text="Refresh", command=self.refresh_graph)
        self.refresh_btn.grid(row=0, column=0, padx=5)
        
        # Branch filter
        self.branch_var = tk.StringVar(value="all")
        self.branch_filter = ttk.Combobox(self.controls_frame, textvariable=self.branch_var)
        self.branch_filter.grid(row=0, column=1, padx=5)
        
        # Initialize graph
        self.refresh_graph()
        
    def get_git_log(self):
        """Get git log in JSON format"""
        cmd = [
            "git", "log", "--all", "--decorate", "--oneline", "--graph",
            "--pretty=format:{%n  \"commit\": \"%H\",%n  \"author\": \"%an\",%n  \"date\": \"%ad\",%n  \"message\": \"%s\"%n}"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    
    def build_graph(self):
        """Build networkx graph from git log"""
        G = nx.DiGraph()
        log_data = self.get_git_log()
        
        # Parse log and build graph
        commits = [json.loads(commit) for commit in log_data.split("\n\n") if commit.strip()]
        
        for commit in commits:
            G.add_node(commit["commit"][:7], 
                      message=commit["message"],
                      author=commit["author"],
                      date=commit["date"])
        
        # Add edges based on parent-child relationships
        for i in range(len(commits)-1):
            G.add_edge(commits[i]["commit"][:7], commits[i+1]["commit"][:7])
        
        return G
    
    def refresh_graph(self):
        """Refresh the graph visualization"""
        self.ax.clear()
        G = self.build_graph()
        
        # Draw graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, ax=self.ax, with_labels=True, 
                node_color='lightblue', node_size=1000, 
                font_size=8, font_weight='bold')
        
        # Add commit messages as labels
        labels = nx.get_node_attributes(G, 'message')
        nx.draw_networkx_labels(G, pos, labels, font_size=6)
        
        self.canvas.draw()
    
    def run(self):
        """Start the visualizer"""
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = GitVisualizer(root)
    app.run()
