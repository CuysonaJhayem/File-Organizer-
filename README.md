# 🗂️ File Organizer — Python

Automatically sorts all files in your Downloads folder into organized subfolders.

---

## 📁 Folder Structure After Running

```
Downloads/
├── 📁 System_Project   ← .html .php .java .sql .zip
├── 📁 Documents        ← .pdf .docx .xlsx .pptx
├── 📁 Images           ← .jpg .png .gif .svg
├── 📁 Music            ← .mp3 .wav .flac
├── 📁 Videos           ← .mp4 .mkv .avi
├── 📁 Code             ← .py .js .css .json
└── 📁 Other            ← everything else
```

---

## ✅ Requirements

- Python 3.x installed
- No additional libraries needed (uses built-in `os` and `shutil`)

---

## 🚀 Step-by-Step Setup

### Step 1 — Install Python

1. Go to [https://www.python.org/downloads](https://www.python.org/downloads)
2. Click **Download Python 3.x.x**
3. Run the installer
4. ⚠️ **IMPORTANT:** Check the box that says **"Add Python to PATH"** before clicking Install

To verify, open Command Prompt and type:
```
python --version
```
It should show something like `Python 3.12.0`

---

### Step 2 — Install VS Code (Optional but Recommended)

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com)
2. Download and install VS Code
3. Open VS Code → Install the **Python extension** (by Microsoft)

---

### Step 3 — Download the Script

1. Download `File_Organizer.py` from this repository
2. Place it anywhere on your computer (e.g., Desktop)

---

### Step 4 — Find Your Downloads Path

1. Press `Windows + R`
2. Type `%USERPROFILE%\Downloads` and press Enter
3. Look at the address bar — copy your path

Example:
```
C:\Users\Cuysona\Downloads
```

---

### Step 5 — Edit the Script

Open `File_Organizer.py` and change line 4:

```python
# BEFORE
ddir = r"C:\Users\YourName\Downloads"

# AFTER (use your actual username)
ddir = r"C:\Users\Cuysona\Downloads"
```

---

### Step 6 — Run the Script

**Option A — Using VS Code:**
1. Open `File_Organizer.py` in VS Code
2. Press the ▶️ Run button (top right)

**Option B — Using Command Prompt:**
1. Press `Windows + R` → type `cmd` → Enter
2. Navigate to the folder where your script is:
```
cd Desktop
```
3. Run the script:
```
python File_Organizer.py
```

---

### Step 7 — Check the Output

You should see output like this:
```
Created directory: Images
Created directory: Music
Created directory: Videos
Created directory: Documents
Created directory: Code
Created directory: Other
Created directory: System_Project
Moved index.html → System_Project
Moved Main.java → System_Project
Moved style.css → Code
Moved photo.jpg → Images
...
✅ Done! Files organized successfully.
```

---

## ⚠️ Important Notes

- **Backup your files first** before running, just to be safe
- The script only moves **files** — folders are left untouched
- `.DS_Store` files (Mac system files) are automatically skipped
- You can change `ddir` to **any folder** you want to organize, not just Downloads

---

## 🎓 Capstone / System Project Files

These file types automatically go to `System_Project/`:

| Extension | Type |
|-----------|------|
| `.html` `.htm` | HTML |
| `.java` `.class` `.jar` | Java |
| `.php` | PHP |
| `.sql` | Database |
| `.zip` | Zipped Projects |

---

## 📝 Author

Made with Python 🐍
