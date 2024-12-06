import tkinter as tk
from tkinter import ttk, scrolledtext
import difflib
import subprocess
import os

class ConflictResolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Git Conflict Resolution Trainer")
        
        # Setup main container
        self.main_container = ttk.Frame(root)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Setup UI components
        self.setup_file_section()
        self.setup_conflict_view()
        self.setup_resolution_section()
        self.setup_status_section()
        
    def setup_file_section(self):
        file_frame = ttk.LabelFrame(self.main_container, text="File Selection")
        file_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(file_frame, text="Conflicted File:").pack(side=tk.LEFT, padx=5)
        self.file_path = ttk.Entry(file_frame)
        self.file_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        ttk.Button(file_frame, text="Browse", 
                  command=self.browse_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Load", 
                  command=self.load_file).pack(side=tk.LEFT, padx=5)
        
    def setup_conflict_view(self):
        conflict_frame = ttk.LabelFrame(self.main_container, text="Conflict View")
        conflict_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Local changes
        local_frame = ttk.LabelFrame(conflict_frame, text="Local Changes")
        local_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.local_text = scrolledtext.ScrolledText(local_frame)
        self.local_text.pack(fill=tk.BOTH, expand=True)
        
        # Remote changes
        remote_frame = ttk.LabelFrame(conflict_frame, text="Remote Changes")
        remote_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.remote_text = scrolledtext.ScrolledText(remote_frame)
        self.remote_text.pack(fill=tk.BOTH, expand=True)
        
    def setup_resolution_section(self):
        resolution_frame = ttk.LabelFrame(self.main_container, text="Resolution")
        resolution_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.resolved_text = scrolledtext.ScrolledText(resolution_frame)
        self.resolved_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        button_frame = ttk.Frame(resolution_frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Use Local", 
                  command=self.use_local).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Use Remote", 
                  command=self.use_remote).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Custom Merge", 
                  command=self.custom_merge).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Apply Resolution", 
                  command=self.apply_resolution).pack(side=tk.LEFT, padx=5)
        
    def setup_status_section(self):
        status_frame = ttk.LabelFrame(self.main_container, text="Status")
        status_frame.pack(fill=tk.X)
        
        self.status_text = tk.Text(status_frame, height=5)
        self.status_text.pack(fill=tk.X, padx=5, pady=5)
        
    def browse_file(self):
        # Implement file browser
        pass
        
    def load_file(self):
        try:
            # Simulate loading a file with conflicts
            local_content = """def calculate_total(items):
    total = 0
    for item in items:
        total += item.price * item.quantity
    return total"""
            
            remote_content = """def calculate_total(items):
    total = 0
    for item in items:
        if item.is_discounted:
            total += item.price * item.quantity * 0.9
        else:
            total += item.price * item.quantity
    return total"""
            
            self.local_text.delete('1.0', tk.END)
            self.local_text.insert('1.0', local_content)
            
            self.remote_text.delete('1.0', tk.END)
            self.remote_text.insert('1.0', remote_content)
            
            self.status_text.insert(tk.END, "Loaded file with conflicts\n")
            
        except Exception as e:
            self.status_text.insert(tk.END, f"Error loading file: {str(e)}\n")
            
    def use_local(self):
        content = self.local_text.get('1.0', tk.END)
        self.resolved_text.delete('1.0', tk.END)
        self.resolved_text.insert('1.0', content)
        
    def use_remote(self):
        content = self.remote_text.get('1.0', tk.END)
        self.resolved_text.delete('1.0', tk.END)
        self.resolved_text.insert('1.0', content)
        
    def custom_merge(self):
        # Get differences
        local_lines = self.local_text.get('1.0', tk.END).splitlines()
        remote_lines = self.remote_text.get('1.0', tk.END).splitlines()
        
        differ = difflib.Differ()
        diff = list(differ.compare(local_lines, remote_lines))
        
        # Create merged content
        merged = []
        for line in diff:
            if line.startswith('  '):  # unchanged
                merged.append(line[2:])
            elif line.startswith('+ '):  # added in remote
                merged.append(f">>> {line[2:]}")
            elif line.startswith('- '):  # removed in remote
                merged.append(f"<<< {line[2:]}")
                
        merged_content = '\n'.join(merged)
        self.resolved_text.delete('1.0', tk.END)
        self.resolved_text.insert('1.0', merged_content)
        
    def apply_resolution(self):
        try:
            content = self.resolved_text.get('1.0', tk.END)
            # In a real implementation, this would write to the file
            # and mark the conflict as resolved in git
            self.status_text.insert(tk.END, "Resolution applied successfully\n")
            
        except Exception as e:
            self.status_text.insert(tk.END, f"Error applying resolution: {str(e)}\n")

def main():
    root = tk.Tk()
    app = ConflictResolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
