"""
A simple script to batch remove files unwanted name parts.
"""
import os

def rename_files(text_to_remove):
    current_directory = os.getcwd()
    
    for filename in os.listdir(current_directory):
        if text_to_remove in filename:
            new_filename = filename.replace(text_to_remove, '')
            os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))
            print(f'Renamed file: {filename} to {new_filename}')

if __name__ == "__main__":
    text_to_remove = input("Enter the text to be removed: ")

    if text_to_remove and not text_to_remove.isspace():
        rename_files(text_to_remove)
    else:
        print("Text is empty or null. Exiting.")

    input("Press Enter to exit.")
