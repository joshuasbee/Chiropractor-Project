# Run this to update the tkinter app
# python -m PyInstaller --name=ServerControlApp --onefile --noconsole server_control.py

import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import signal
import sys

class ServerControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Server Control")

        self.server_process = None

        self.status_label = tk.Label(root, text="Server Status: Not Running", padx=20, pady=20)
        self.status_label.pack()

        self.start_button = tk.Button(root, text="Start Server", command=self.start_server, padx=20, pady=10)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Server", command=self.stop_server, padx=20, pady=10)
        self.stop_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_server(self):
        if self.server_process is None:
            try:
                self.server_process = subprocess.Popen(
                    [sys.executable, 'myapp.py'],
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                self.status_label.config(text="Server Status: Running")
                messagebox.showinfo("Server Control", "Server started successfully!")
            except Exception as e:
                messagebox.showerror("Server Control", f"Error starting server: {e}")
        else:
            messagebox.showwarning("Server Control", "Server is already running!")

    def stop_server(self):
        if self.server_process is not None:
            try:
                os.kill(self.server_process.pid, signal.SIGTERM)
                self.server_process = None
                self.status_label.config(text="Server Status: Not Running")
                messagebox.showinfo("Server Control", "Server stopped successfully!")
            except Exception as e:
                messagebox.showerror("Server Control", f"Error stopping server: {e}")
        else:
            messagebox.showwarning("Server Control", "Server is not running!")

    def on_closing(self):
        self.stop_server()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerControlApp(root)
    root.mainloop()
