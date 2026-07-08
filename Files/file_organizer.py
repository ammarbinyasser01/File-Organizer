import os
import shutil
import logging
from pathlib import Path

# =====================================================
# CONFIGURATION
# =====================================================

# Change this to the folder you want to organize.
# Example:
# DIRECTORY = r"C:\Users\YourName\Downloads"

DIRECTORY = r"D:\File Organizer\test_downloads"

# =====================================================
# LOGGING CONFIGURATION
# =====================================================

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =====================================================
# FILE TYPE MAPPING
# =====================================================

FILE_TYPES = {
    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp"
    ],

    "Documents": [
        ".pdf",
        ".docx",
        ".doc",
        ".txt",
        ".xlsx",
        ".xls",
        ".pptx",
        ".ppt"
    ],

    "Videos": [
        ".mp4",
        ".avi",
        ".mov",
        ".mkv",
        ".wmv"
    ]
}

# =====================================================
# CREATE REQUIRED FOLDERS
# =====================================================

def create_folders(base_directory):
    """
    Create category folders if they do not already exist.
    """

    folders = list(FILE_TYPES.keys())
    folders.append("Others")

    for folder in folders:
        folder_path = os.path.join(base_directory, folder)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.info(f"Created folder: {folder_path}")


# =====================================================
# DETERMINE FILE CATEGORY
# =====================================================

def get_category(extension):
    """
    Return the folder name based on file extension.
    """

    extension = extension.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


# =====================================================
# MOVE FILE
# =====================================================

def move_file(source_path, destination_folder):
    """
    Move a file safely into its destination folder.
    """

    filename = os.path.basename(source_path)

    destination_path = os.path.join(destination_folder, filename)

    try:
        shutil.move(source_path, destination_path)

        print(f"Moved: {filename} -> {os.path.basename(destination_folder)}")

        logging.info(
            f"Moved '{filename}' to '{destination_folder}'"
        )

    except Exception as error:

        print(f"Error moving {filename}")

        logging.error(
            f"Could not move '{filename}'. Error: {error}"
        )

# =====================================================
# ORGANIZE FILES
# =====================================================

def organize_files(base_directory):
    """
    Organize files in the specified directory.
    """

    # Check if directory exists
    if not os.path.exists(base_directory):
        print("Error: Directory does not exist.")
        logging.error(f"Directory not found: {base_directory}")
        return

    # Create category folders
    create_folders(base_directory)

    # Scan all items in the directory
    for item in os.listdir(base_directory):

        item_path = os.path.join(base_directory, item)

        # Skip directories (Images, Documents, etc.)
        if os.path.isdir(item_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(item)

        # Determine destination category
        category = get_category(extension)

        destination_folder = os.path.join(base_directory, category)

        # Move the file
        move_file(item_path, destination_folder)

    print("\nFile organization completed successfully!")
    logging.info("File organization completed successfully.")

# =====================================================
# MAIN FUNCTION
# =====================================================

def main():
    """
    Main entry point of the program.
    """

    print("=" * 50)
    print("        FILE ORGANIZER")
    print("=" * 50)
    print(f"\nDirectory to organize:\n{DIRECTORY}\n")

    logging.info("=" * 50)
    logging.info("File Organizer Started")

    organize_files(DIRECTORY)

    logging.info("File Organizer Finished")
    logging.info("=" * 50)


# =====================================================
# RUN PROGRAM
# =====================================================

if __name__ == "__main__":
    main()