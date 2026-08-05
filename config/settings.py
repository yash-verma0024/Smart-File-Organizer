from pathlib import Path

PROJECT_NAME = "Smart File Organizer"
VERSION = "0.1.0"
DATABASE_PATH = Path("database") / "file_index.db"
LOG_DIR = Path("logs/")
LOG_FILE = Path("logs") / "app.log"
DEFAULT_FOLDER = "Others"