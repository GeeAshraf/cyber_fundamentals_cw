import os
import shutil

def collect_files(source_dir, destination_dir, extensions):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, _, files in os.walk(source_dir):
        for filename in files:
            if filename.lower().endswith(extensions):
                source_path = os.path.join(root, filename)
                dest_path = os.path.join(destination_dir, filename)
                shutil.copy2(source_path, dest_path)

    print(f"files with (extensions) copied to: {destination_dir}")

def main():
    source_dir = input("Enter the source directory (where files are located): ");
    destination_dir = "collected_files"
    extensions_input = input("Enter file extensions to collect (comma separated, e.g., .txt,.docx,.jpg): ");
    extensions = tuple(ext.strip().lower() for ext in extensions_input.split(","))

    collect_files(source_dir, destination_dir, extensions)

if __name__ == "__main__":
    main()
