import os
import shutil

def collect_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(destination_dir, filename)

        if os.path.isfile(source_path):
            shutil.copy2(source_path, dest_path)

    print(f"Files copied to: {destination_dir}")

if __name__ == "__main__":
    collect_files("files_to_encrypt", "collected_files")
