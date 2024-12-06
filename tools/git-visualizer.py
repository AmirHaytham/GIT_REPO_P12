import tkinter as tk
from tkinter import ttk
import subprocess
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import os

class GitVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Git Visualizer Pro")
        
        # Setup main container
        self.main_container = ttk.Frame(root)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Repository section
        self.setup_repo_section()
        
        # Visualization section
        self.setup_visualization_section()
        
        # Commands section
        self.setup_command_section()
        
        # Status section
        self.setup_status_section()
        
        # Initialize graph
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def setup_repo_section(self):
        repo_frame = ttk.LabelFrame(self.main_container, text="Repository")
        repo_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(repo_frame, text="Repository Path:").pack(side=tk.LEFT, padx=5)
        self.repo_path = ttk.Entry(repo_frame)
        self.repo_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        ttk.Button(repo_frame, text="Browse", command=self.browse_repo).pack(side=tk.LEFT, padx=5)
        ttk.Button(repo_frame, text="Load", command=self.load_repo).pack(side=tk.LEFT, padx=5)
        
    def setup_visualization_section(self):
        self.viz_frame = ttk.LabelFrame(self.main_container, text="Visualization")
        self.viz_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
    def setup_command_section(self):
        cmd_frame = ttk.LabelFrame(self.main_container, text="Git Commands")
        cmd_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.cmd_entry = ttk.Entry(cmd_frame)
        self.cmd_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        ttk.Button(cmd_frame, text="Execute", command=self.execute_command).pack(side=tk.LEFT, padx=5)
        
    def setup_status_section(self):
        status_frame = ttk.LabelFrame(self.main_container, text="Status")
        status_frame.pack(fill=tk.X)
        
        self.status_text = tk.Text(status_frame, height=5)
        self.status_text.pack(fill=tk.X, padx=5, pady=5)
        
    def browse_repo(self):
        # Implement repository browser
        pass
        
    def load_repo(self):
        # Load and visualize repository
        self.update_graph()
        
    def execute_command(self):
        command = self.cmd_entry.get()
        try:
            result = subprocess.run(['git'] + command.split(), 
                                 cwd=self.repo_path.get(),
                                 capture_output=True, text=True)
            self.status_text.insert(tk.END, f"Command: {command}\n{result.stdout}\n")
            self.update_graph()
        except Exception as e:
            self.status_text.insert(tk.END, f"Error: {str(e)}\n")
        
    def update_graph(self):
        try:
            # Get git log in JSON format
            result = subprocess.run(['git', 'log', '--pretty=format:{"commit": "%H", "parent": "%P", "author": "%an", "date": "%ad", "message": "%s"}'],
                                 cwd=self.repo_path.get(),
                                 capture_output=True, text=True)
            
            # Parse git log
            commits = [json.loads(line) for line in result.stdout.split('\n') if line]
            
            # Create graph
            G = nx.DiGraph()
            
            # Add nodes and edges
            for commit in commits:
                G.add_node(commit['commit'][:7], 
                          author=commit['author'],
                          date=commit['date'],
                          message=commit['message'])
                
                for parent in commit['parent'].split():
                    G.add_edge(commit['commit'][:7], parent[:7])
            
            # Clear previous plot
            self.ax.clear()
            
            # Draw new graph
            pos = nx.spring_layout(G)
            nx.draw(G, pos, ax=self.ax, with_labels=True, 
                   node_color='lightblue', 
                   node_size=1000,
                   arrowsize=20)
            
            # Update canvas
            self.canvas.draw()
            
        except Exception as e:
            self.status_text.insert(tk.END, f"Error updating graph: {str(e)}\n")

def main():
    root = tk.Tk()
    app = GitVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
