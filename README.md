
# 📂 File Organizer Pro

A powerful Python utility to automatically organize files in any folder by type.  
Features dry-run mode, undo functionality, duplicate file handling, logging, and a progress bar for a professional touch.



## 🚀 Features
- **Automatic Categorization** – Moves files into folders like `Videos`, `Documents`, `Photos`, etc. based on their extensions.
- **Custom Config** – Define your own categories and extensions in `file_types.json`.
- **Dry Run Mode** – Preview what will happen before actually moving files.
- **Duplicate Handling** – Automatically renames files if the same name already exists.
- **Undo Functionality** – Restore files to their original locations after a run.
- **Logging** – Keeps a record of all moves in `organizer.log`.
- **Progress Bar** – See the file processing progress in real-time.



## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/file-organizer-pro.git
   cd file-organizer-pro
````

2. **Install dependencies**

   ```bash
   pip install tqdm
   ```

3. **Edit file types (optional)**
   Modify `file_types.json` to suit your needs.



## 🖥️ Usage

### **1️⃣ Dry Run (Safe Mode)**

Preview what would happen without moving files:

```bash
python organizer.py "C:\Users\DELL\Downloads" --dry
```

### **2️⃣ Organize Files**

Move files into categorized folders:

```bash
python organizer.py "C:\Users\DELL\Downloads"
```

### **3️⃣ Undo Last Operation**

Restore files to original locations:

```bash
python organizer.py --undo
```



## 📂 Example Folder Structure

Before:

```
Downloads/
    photo1.jpg
    movie.mp4
    report.pdf
```

After running:

```
Downloads/
    photos/photo1.jpg
    videos/movie.mp4
    documents/report.pdf
```



## ⚙️ Configuration

Edit `file_types.json` to add/remove categories and file extensions:

```json
{
    "videos": [".mp4", ".mov", ".avi"],
    "photos": [".jpg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt"]
}
```



## 📝 Logging

All moves are saved in:

```
organizer.log
```

Example:

```
2025-08-10 14:32:12 | C:\Downloads\photo.jpg -> C:\Downloads\photos\photo.jpg
```

---

## 💡 Ideas for Future Improvements

* GUI interface using Tkinter or PyQt
* Scheduling with Task Scheduler / Cron jobs
* Integration with cloud storage



Feel free to ⭐ the repo if you found this useful!



