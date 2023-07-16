import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import zipfile
import threading

def unzip_file():
    archive_path = filedialog.askopenfilename(title="Select Archive", filetypes=[("ZIP files", "*.zip")])
    if archive_path:
        extract_path = filedialog.askdirectory(title="Select Destination Folder")
        if extract_path:
            progress_bar["value"] = 0
            status_label.config(text="Extracting...")
            status_label.update()
            threading.Thread(target=extract_files, args=(archive_path, extract_path)).start()

def extract_files(archive_path, extract_path):
    try:
        with zipfile.ZipFile(archive_path, 'r') as archive:
            file_count = len(archive.infolist())
            extracted_count = 0
            for file in archive.infolist():
                archive.extract(file, extract_path)
                extracted_count += 1
                progress = int((extracted_count / file_count) * 100)
                progress_bar["value"] = progress
                status_label.config(text=f"Extracting {extracted_count}/{file_count} files...")
                status_label.update()
            status_label.config(text="Extraction successful!")
    except zipfile.BadZipFile:
        status_label.config(text="Error: Invalid ZIP file.")

# Create the main window
window = tk.Tk()
window.title("Unarchiving Tool")
window.geometry("400x200")

# Create a style for the ttk widgets
style = ttk.Style()
style.configure("TButton", padding=6)
style.configure("TLabel", padding=6)

# Create a frame for the content
content_frame = ttk.Frame(window, padding=10)
content_frame.pack(fill=tk.BOTH, expand=True)

# Create a button for selecting the archive file
select_button = ttk.Button(content_frame, text="Select Archive", command=unzip_file)
select_button.pack(pady=10)

# Create a progress bar
progress_bar = ttk.Progressbar(content_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress_bar.pack()

# Create a label for displaying the status
status_label = ttk.Label(content_frame, text="")
status_label.pack()

# Run the main event loop
window.mainloop()
