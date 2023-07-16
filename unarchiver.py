import zipfile

def unzip_file(archive_path, extract_path):
    try:
        with zipfile.ZipFile(archive_path, 'r') as archive:
            archive.extractall(extract_path)
            print("Extraction successful!")
    except zipfile.BadZipFile:
        print("Error: Invalid ZIP file.")

# Usage example
archive_path = 'path/to/archive.zip'  # Replace with the path to your ZIP archive
extract_path = 'path/to/extract'  # Replace with the path where you want to extract the files

unzip_file(archive_path, extract_path)
