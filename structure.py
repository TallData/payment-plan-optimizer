import os

# Define the folder structure in a dictionary
folder_structure = {
    'payment-plan-optimizer': {
        'app': ['static/css', 'static/js', 'static/img', 'templates'],
        'data': ['raw', 'processed'],
        'models': [],
        'notebooks': [],
        'tests': [],
        'utils': [],
    }
}

def create_folders(base_path, structure):
    """Recursively create folder structure."""
    for folder, subfolders in structure.items():
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        if isinstance(subfolders, list):  # Base case: a list of subfolders
            for subfolder in subfolders:
                os.makedirs(os.path.join(path, subfolder), exist_ok=True)
        elif isinstance(subfolders, dict):  # Recursive case: a dict of more folders
            create_folders(path, subfolders)

# The base path where to create the folder structure
base_path = '.'  # Current directory as base path

# Create the folder structure
create_folders(base_path, folder_structure)

print("Folder structure created successfully!")