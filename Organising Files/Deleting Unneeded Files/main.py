import os

def find_large_files(folder):
    folder = os.path.abspath(folder)
    size_limit = 100 * 1024 * 1024

    for folder_name, subfolders, file_names in os.walk(folder):
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)

            try:
                file_size = os.path.getsize(file_path)
            except OSError:
                continue

            if file_size > size_limit:
                print(f"{file_path} ---> {file_size / (1024*1024):.2f} MB")
