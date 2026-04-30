import os
import shutil

# ── Change this to your folder path ─────────────
ddir = r"C:\Users\YourName\Downloads"
# ────────────────────────────────────────────────

# ── CREATE FOLDERS ──────────────────────────────
folders = [
    "/Images", "/Music", "/Videos", "/Documents",
    "/Code", "/Other", "/System_Project"
]
for folder in folders:
    if not os.path.exists(ddir + folder):
        os.makedirs(ddir + folder)
        print(f"Created directory: {folder[1:]}")

# ── FILE EXTENSIONS ──────────────────────────────
image_extensions  = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"]
music_extensions  = [".mp3", ".wav", ".aiff", ".flac", ".ogg"]
video_extensions  = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
doc_extensions    = [".txt", ".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".csv"]
code_extensions   = [".py", ".js", ".ts", ".css", ".json", ".xml", ".sh"]

# HTML, Java, PHP → System_Project (Capstone)
system_extensions = [
    ".html", ".htm",          # HTML
    ".java", ".class", ".jar",# Java
    ".php",                   # PHP
    ".sql",                   # Database
    ".zip",                   # Zipped projects
]

# ── MOVE FILES ──────────────────────────────────
for file in os.listdir(ddir):
    if os.path.isdir(ddir + "/" + file):
        continue
    if file == ".DS_Store":
        continue

    extension = os.path.splitext(file)[1].lower()

    if extension in system_extensions:
        shutil.move(ddir + "/" + file, ddir + "/System_Project")
        print(f"[CAPSTONE] Moved {file} → System_Project")
    elif extension in image_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Images")
        print(f"Moved {file} → Images")
    elif extension in music_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Music")
        print(f"Moved {file} → Music")
    elif extension in video_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Videos")
        print(f"Moved {file} → Videos")
    elif extension in doc_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Documents")
        print(f"Moved {file} → Documents")
    elif extension in code_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Code")
        print(f"Moved {file} → Code")
    else:
        shutil.move(ddir + "/" + file, ddir + "/Other")
        print(f"Moved {file} → Other")

print("\n✅ Done! Files organized successfully.")
