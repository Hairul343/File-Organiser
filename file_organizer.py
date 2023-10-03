import os
import shutil
import json

def load_config():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    return config

def organize_files(source_dir, dest_dir, config):
    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        if os.path.isfile(src_path):
            file_extension = filename.split(".")[-1]
            file_extension = file_extension.lower()

            if file_extension in config:
                category = config[file_extension]
                category_dir = os.path.join(dest_dir, category)

                if not os.path.exists(category_dir):
                    os.makedirs(category_dir)

                dest_path = os.path.join(category_dir, filename)

                if not os.path.exists(dest_path):
                    shutil.move(src_path, dest_path)
                    print(f"Moved {filename} to {category}")
                else:
                    print(f"{filename} already exists in {category}")

def main():
    config = load_config()
    source_dir = config["source_directory"]
    dest_dir = config["destination_directory"]

    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    organize_files(source_dir, dest_dir, config)
    print("File organization complete.")

if __name__ == "__main__":
    main()
