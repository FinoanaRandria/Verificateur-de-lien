import requests
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def check_url_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.exceptions.RequestException as e:
        return False, str(e)

def scan_urls(file_path, result_display):
    with open(file_path, 'r') as file:
        urls = file.readlines()

    result_display.delete(1.0, tk.END)
    for url in urls:
        url = url.strip()
        if url:
            is_valid, status = check_url_status(url)
            status_text = f"OK ({status})" if is_valid else f"Broken ({status})"
            result_display.insert(tk.END, f"{url}: {status_text}\n")

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select URL file", 
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def start_scan():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showwarning("File not selected", "Please select a file.")
        return
    scan_urls(file_path, result_display)

# Tkinter 
root = tk.Tk()
root.title("URL Scanner")
root.geometry("600x400")


file_frame = tk.Frame(root)
file_frame.pack(pady=20)

file_label = tk.Label(file_frame, text="Select file:")
file_label.pack(side=tk.LEFT, padx=5)

file_entry = tk.Entry(file_frame, width=40)
file_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(file_frame, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT, padx=5)

scan_button = tk.Button(root, text="Scan URLs", command=start_scan)
scan_button.pack(pady=10)

result_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
result_display.pack(pady=10)

root.mainloop()
