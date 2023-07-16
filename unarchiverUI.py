import tkinter as tk
from tkinter import filedialog
import zipfile

def unzip_file():
    archive_path = filedialog.askopenfilename(title="Select Archive", filetypes=[("ZIP files", "*.zip")])
    if archive_path:
        extract_path = filedialog.askdirectory(title="Select Destination Folder")
        if extract_path:
            try:
                with zipfile.ZipFile(archive_path, 'r') as archive:
                    archive.extractall(extract_path)
                    status_label.config(text="Extraction successful!")
            except zipfile.BadZipFile:
                status_label.config(text="Error: Invalid ZIP file.")

# Create the main window
window = tk.Tk()
window.title("Unarchiving Tool")

# Create a button for selecting the archive file
select_button = tk.Button(window, text="Select Archive", command=unzip_file)
select_button.pack(pady=10)

# Create a label for displaying the status
status_label = tk.Label(window, text="")
status_label.pack()

# Run the main event loop
window.mainloop()
