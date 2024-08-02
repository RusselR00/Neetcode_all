import os
import re

def clean_folder_name(name):
    # Remove special characters and replace spaces with underscores
    return re.sub(r'[^a-zA-Z0-9_]', '', name.replace(' ', '_'))

def create_folders(base_path, folder_names):
    for folder in folder_names:
        cleaned_name = clean_folder_name(folder)
        folder_path = os.path.join(base_path, cleaned_name)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"Folder '{cleaned_name}' created successfully.")
        except OSError as error:
            print(f"Error creating folder '{cleaned_name}': {error}")
def create_folders_with_index(base_path, folder_names):
    for index, folder in enumerate(folder_names, start=1):
        cleaned_name = f"{index:02d}_{clean_folder_name(folder)}"
        folder_path = os.path.join(base_path, cleaned_name)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"Folder '{cleaned_name}' created successfully.")
        except OSError as error:
            print(f"Error creating folder '{cleaned_name}': {error}")


# List of main categories
roadmap_topics = [
    "Arrays & Hashing",
    "Two Pointers",
    "Stack",
    "Binary Search",
    "Sliding Window",
    "Linked List",
    "Trees",
    "Tries",
    "Backtracking",
    "Heap / Priority Queue",
    "Graphs",
    "1-D Dynamic Programming",
    "Intervals",
    "Greedy",
    "Advanced Graphs",
    "2-D Dynamic Programming",
    "Bit Manipulation",
    "Math & Geometry"
]

# Base directory
base_dir = r"D:\neetcode\Neetcode_all"

# Create the base directory if it doesn't exist
os.makedirs(base_dir, exist_ok=True)

# Create folders with index
create_folders_with_index(base_dir, roadmap_topics)