import os
import shutil
import re

def slugify(text):
    """
    Converts 'Pizza Tower_ Scoutdigo' to 'pizza-tower-scoutdigo'
    """
    # Replace underscores/special chars with hyphens, lowercase everything
    text = text.lower()
    # Remove everything except alphanumeric and spaces/hyphens
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    # Replace spaces and multiple hyphens with a single hyphen
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')

def cleanup_game_folders(path='.'):
    # Get all directories in the path
    items = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    
    for folder in items:
        # Check if the folder needs slugging (has uppercase or spaces)
        if any(char.isupper() for char in folder) or ' ' in folder:
            slugged_name = slugify(folder)
            
            old_path = os.path.join(path, folder)
            new_path = os.path.join(path, slugged_name)
            
            # 1. Handle Duplicates: If the target slugged name already exists
            if os.path.exists(new_path) and old_path.lower() != new_path.lower():
                print(f"Duplicate found: Deleting existing slugged folder '{slugged_name}'")
                try:
                    shutil.rmtree(new_path)
                except Exception as e:
                    print(f"Error deleting {slugged_name}: {e}")
                    continue

            # 2. Rename the 'Good Grammar' folder to the slugged version
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: '{folder}' -> '{slugged_name}'")
            except Exception as e:
                print(f"Error renaming {folder}: {e}")

if __name__ == "__main__":
    # Change this path if the script isn't inside the games folder
    target_dir = os.getcwd() 
    print(f"Starting cleanup in: {target_dir}")
    cleanup_game_folders(target_dir)
    print("Cleanup complete.")