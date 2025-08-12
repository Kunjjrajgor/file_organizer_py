import os
import shutil
import sys
import json
from tqdm import tqdm
from datetime import datetime

LOG_FILE = "organizer.log"
UNDO_FILE = "undo.json"

def load_types():
    try:
        with open("file_types.json") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: 'file_types.json' not found!")
        sys.exit()

def get_unique_path(path):
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = f"{base} ({counter}){ext}"
        counter += 1
    return path

def log_action(source, destination):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} | {source} -> {destination}\n")

def save_undo(undo_list):
    with open(UNDO_FILE, "w", encoding="utf-8") as f:
        json.dump(undo_list, f, indent=4)

def load_undo():
    try:
        with open(UNDO_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        print("No undo file found.")
        return []

def organize(folder, types, dry_run=False):
    undo_list = []
    for filename in tqdm(os.listdir(folder), desc="Organizing files"):
        source = os.path.join(folder, filename)
        if os.path.isdir(source):
            continue
        ext = os.path.splitext(filename)[1].lower()

        moved = False
        for category, extensions in types.items():
            if ext in extensions:
                destination_folder = os.path.join(folder, category)
                os.makedirs(destination_folder, exist_ok=True)

                destination = get_unique_path(os.path.join(destination_folder, filename))

                if dry_run:
                    print(f"[DRY RUN] Would move: {source} -> {destination}")
                else:
                    try:
                        shutil.move(source, destination)
                        undo_list.append({"old": source, "new": destination})
                        log_action(source, destination)
                    except PermissionError:
                        print(f"Permission denied: {filename}")
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")
                moved = True
                break

        if not moved and not dry_run:
            others_folder = os.path.join(folder, "others")
            os.makedirs(others_folder, exist_ok=True)
            destination = get_unique_path(os.path.join(others_folder, filename))
            shutil.move(source, destination)
            undo_list.append({"old": source, "new": destination})
            log_action(source, destination)

    if not dry_run:
        save_undo(undo_list)

def undo():
    undo_list = load_undo()
    if not undo_list:
        return
    for entry in tqdm(undo_list, desc="Undoing file moves"):
        try:
            os.makedirs(os.path.dirname(entry["old"]), exist_ok=True)
            shutil.move(entry["new"], entry["old"])
        except Exception as e:
            print(f"Error undoing {entry['new']}: {e}")
    os.remove(UNDO_FILE)
    print("Undo complete.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organizer.py <folder_path> [--dry | --undo]")
        sys.exit()

    if "--undo" in sys.argv:
        undo()
    else:
        folder_path = sys.argv[1]
        dry_mode = "--dry" in sys.argv
        types = load_types()
        organize(folder_path, types, dry_run=dry_mode)
        print("Done!")
