import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import random

class BranchSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Branch Strategy Simulator")
        
        # Initialize graph data
        self.graph = nx.DiGraph()
        self.branch_colors = {
            'main': '#2ecc71',
            'develop': '#3498db',
            'feature': '#e74c3c',
            'hotfix': '#f1c40f',
            'release': '#9b59b6'
        }
        
        # Setup UI
        self.setup_ui()
        
        # Initialize simulation state
        self.current_step = 0
        self.simulation_steps = []
        
    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Control panel
        control_frame = ttk.LabelFrame(main_frame, text="Controls")
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Branch operations
        branch_frame = ttk.Frame(control_frame)
        branch_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(branch_frame, text="Branch:").pack(side=tk.LEFT)
        self.branch_var = tk.StringVar(value='feature')
        branch_combo = ttk.Combobox(branch_frame, textvariable=self.branch_var)
        branch_combo['values'] = ('main', 'develop', 'feature', 'hotfix', 'release')
        branch_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(branch_frame, text="Create Branch", 
                  command=self.create_branch).pack(side=tk.LEFT, padx=5)
        ttk.Button(branch_frame, text="Merge Branch", 
                  command=self.merge_branch).pack(side=tk.LEFT, padx=5)
        
        # Commit operations
        commit_frame = ttk.Frame(control_frame)
        commit_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(commit_frame, text="Add Commit", 
                  command=self.add_commit).pack(side=tk.LEFT, padx=5)
        ttk.Button(commit_frame, text="Reset Head", 
                  command=self.reset_head).pack(side=tk.LEFT, padx=5)
        
        # Simulation controls
        sim_frame = ttk.Frame(control_frame)
        sim_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(sim_frame, text="Load Scenario", 
                  command=self.load_scenario).pack(side=tk.LEFT, padx=5)
        ttk.Button(sim_frame, text="Next Step", 
                  command=self.next_step).pack(side=tk.LEFT, padx=5)
        ttk.Button(sim_frame, text="Reset", 
                  command=self.reset_simulation).pack(side=tk.LEFT, padx=5)
        
        # Visualization area
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Status area
        self.status_text = tk.Text(main_frame, height=5)
        self.status_text.pack(fill=tk.X, pady=(10, 0))
        
    def create_branch(self):
        branch_type = self.branch_var.get()
        new_node = f"{branch_type}_{random.randint(1000, 9999)}"
        self.graph.add_node(new_node, 
                          branch_type=branch_type,
                          color=self.branch_colors[branch_type])
        # Add edge from current head if exists
        if len(self.graph.nodes) > 1:
            heads = [n for n in self.graph.nodes if self.graph.out_degree(n) == 0]
            if heads:
                self.graph.add_edge(heads[0], new_node)
        self.update_visualization()
        
    def merge_branch(self):
        # Implement merge logic
        heads = [n for n in self.graph.nodes if self.graph.out_degree(n) == 0]
        if len(heads) >= 2:
            self.graph.add_edge(heads[0], heads[1])
            self.update_visualization()
        
    def add_commit(self):
        # Add new commit to current branch
        branch_type = self.branch_var.get()
        new_node = f"commit_{random.randint(1000, 9999)}"
        self.graph.add_node(new_node, 
                          branch_type=branch_type,
                          color=self.branch_colors[branch_type])
        # Add edge from current head
        heads = [n for n in self.graph.nodes if self.graph.out_degree(n) == 0]
        if heads:
            self.graph.add_edge(heads[0], new_node)
        self.update_visualization()
        
    def reset_head(self):
        # Implement reset logic
        pass
        
    def load_scenario(self):
        # Load predefined scenario
        self.simulation_steps = [
            {'action': 'create_branch', 'branch': 'main'},
            {'action': 'add_commit', 'branch': 'main'},
            {'action': 'create_branch', 'branch': 'feature'},
            {'action': 'add_commit', 'branch': 'feature'},
            {'action': 'merge_branch', 'source': 'feature', 'target': 'main'}
        ]
        self.current_step = 0
        self.reset_simulation()
        
    def next_step(self):
        if self.current_step < len(self.simulation_steps):
            step = self.simulation_steps[self.current_step]
            if step['action'] == 'create_branch':
                self.branch_var.set(step['branch'])
                self.create_branch()
            elif step['action'] == 'add_commit':
                self.branch_var.set(step['branch'])
                self.add_commit()
            elif step['action'] == 'merge_branch':
                self.merge_branch()
            self.current_step += 1
            
    def reset_simulation(self):
        self.graph.clear()
        self.current_step = 0
        self.update_visualization()
        
    def update_visualization(self):
        self.ax.clear()
        
        if len(self.graph.nodes) > 0:
            pos = nx.spring_layout(self.graph)
            
            # Draw nodes
            for node in self.graph.nodes:
                nx.draw_networkx_nodes(self.graph, pos,
                                     nodelist=[node],
                                     node_color=[self.graph.nodes[node]['color']],
                                     node_size=1000)
            
            # Draw edges
            nx.draw_networkx_edges(self.graph, pos, edge_color='gray',
                                 arrows=True, arrowsize=20)
            
            # Draw labels
            nx.draw_networkx_labels(self.graph, pos)
            
        self.canvas.draw()

def main():
    root = tk.Tk()
    app = BranchSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
