import os

def collect_files(directory, extensions=None, log_file='files.log'):
    if extensions is None:
        extensions = ['.txt', '.docx', '.jpg']

    collected_files = []

    # Recursively walk through directories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                collected_files.append(file_path)

    # Save to log file
    with open(log_file, 'w') as f:
        for path in collected_files:
            f.write(path + '\n')

    print(f"[+] Collected {len(collected_files)} files.")
    return collected_files

# Example usage
if __name__ == "__main__":
    import sys

    target_dir = input("Enter the directory to search: ").strip()
    if not os.path.isdir(target_dir):
        print("[-] Invalid directory.")
        sys.exit(1)

    collect_files(target_dir)
