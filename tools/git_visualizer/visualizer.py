import networkx as nx
import matplotlib.pyplot as plt
import subprocess
from datetime import datetime

def get_git_log():
    """Get git log information"""
    cmd = [
        "git", "log", "--all", "--pretty=format:%H|%an|%ad|%s"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def visualize_git_history():
    """Visualize git repository history"""
    # Create directed graph
    G = nx.DiGraph()
    
    # Get git log data
    log_data = get_git_log()
    
    try:
        # Parse commits
        commits = []
        for line in log_data.split('\n'):
            if line.strip():
                parts = line.split('|')
                if len(parts) == 4:
                    commit = {
                        "hash": parts[0],
                        "author": parts[1],
                        "date": parts[2],
                        "message": parts[3]
                    }
                    commits.append(commit)
        
        # Add nodes and edges
        for commit in commits:
            short_hash = commit["hash"][:7]
            G.add_node(short_hash, 
                      message=commit["message"],
                      author=commit["author"],
                      date=commit["date"])
        
        # Add edges based on commit order
        for i in range(len(commits)-1):
            G.add_edge(commits[i]["hash"][:7], commits[i+1]["hash"][:7])
        
        # Create visualization with larger figure size
        plt.figure(figsize=(20, 12))
        
        # Use hierarchical layout for better commit flow visualization
        pos = nx.kamada_kawai_layout(G)
        
        # Increase spacing between nodes
        pos = {node: (coord[0] * 1.5, coord[1] * 1.5) for node, coord in pos.items()}
        
        # Draw graph with improved visual parameters
        nx.draw(G, pos, 
               node_color='lightblue',
               node_size=3000,  # Increased node size
               font_size=10,    # Increased font size
               font_weight='bold',
               with_labels=True,
               arrows=True,
               edge_color='gray',
               width=2,
               arrowsize=20,
               alpha=0.7)       # Added transparency
        
        # Add commit messages as labels with better formatting
        labels = {node: f"{node}\n{G.nodes[node]['message'][:30]}..." 
                 for node in G.nodes()}
        
        # Draw labels with offset to prevent overlap
        label_pos = {node: (coord[0], coord[1] - 0.08) for node, coord in pos.items()}
        nx.draw_networkx_labels(G, label_pos, labels, font_size=8)
        
        plt.title("Git Repository Visualization\nCommit History Graph", 
                 fontsize=16, pad=20)
        plt.axis('off')
        plt.tight_layout(pad=2.0)  # Increased padding
        plt.show()
        
    except Exception as e:
        print(f"Error visualizing git history: {e}")

if __name__ == "__main__":
    visualize_git_history()
