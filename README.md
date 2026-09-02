<img width="489" height="510" alt="image" src="https://github.com/user-attachments/assets/59d7470b-b2cd-486e-81b9-181171687692" />
# 📁 Smart-File-Organizer

> A powerful Python-based tool that automatically organizes files into categorized folders by type. Built with clean architecture, comprehensive database tracking, and beautiful visualizations to solve real-world file management challenges.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com)

## 🎯 Overview

**Smart-File-Organizer** is an intelligent file management system that transforms cluttered folders into well-organized directory structures. It's designed for students, developers, office workers, and anyone struggling with file management on Windows or Linux systems.

### Key Features

✨ **Core Features:**
- 🔄 **Automatic File Organization** - Intelligently sorts files by type, extension, or date
- 📊 **Database Tracking** - SQLite database stores metadata for all organized files
- 📈 **Visual Analytics** - Beautiful charts showing file distribution and storage usage
- 🔍 **Smart Search** - Find files by ID, name, extension, or custom queries
- ⚠️ **Safe Operations** - Never deletes files, validates all operations
- 🔐 **Error Handling** - Graceful error management with comprehensive logging
- 🔁 **Recursive Organization** - Organize nested folder structures
- 🏃 **Dry-Run Mode** - Preview changes before applying them

---

## 📋 Problem It Solves

- ❌ **Messy Downloads/Desktop folders**
- ❌ Manual file sorting is time-consuming
- ❌ Difficulty finding files across mixed folders
- ❌ No history of where files were moved
- ❌ Risk of accidental file deletion or overwriting

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/Smart-File-Organizer.git
cd Smart-File-Organizer
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python main.py
```

---

## 📖 Usage Guide

### Main Menu Options

When you run the program, you'll see three main options:

```
1. Organize files in folder
2. Check Database
3. View Graphs
```

### Option 1: Organize Files

```python
python main.py
# Select option: 1
# Enter the path you want to organize
```

**What happens:**
- Scans all files in the specified folder
- Classifies files by type (Images, Documents, Audio, etc.)
- Creates category folders automatically
- Moves files to appropriate folders
- Stores metadata in the database

**Supported Categories:**
- 📷 **Images:** jpg, png, jpeg, gif
- 📄 **Documents:** doc, docx, pdf, txt, xlsx, xls
- 🎵 **Audio:** mp3, wav, m4a
- 🎬 **Videos:** mp4, m4v, mkv
- 📦 **Archives:** zip, rar, 7z, tar
- 🐍 **Programming:** py, js, html, css, cpp, ipynb

### Option 2: Database Operations

```
1. See all records
2. Search for specific files
   - By ID
   - By name
   - By extension
3. Update file path
```

**View all files:**
Shows complete metadata including:
- File ID
- File name
- Extension
- Full path
- File size
- File hash
- MIME type
- Creation & modification dates

**Search features:**
- Quick lookup by ID
- Find all files with specific extension
- Search by file name

### Option 3: View Graphs & Analytics

```
1. Files vs Extension graph
2. Storage usage by extension
3. Files with maximum size
```

Generates beautiful visualizations showing:
- Distribution of files across extensions
- Storage consumption analysis
- Largest files in your organized folder

---

## 📁 Project Structure

```
Smart-File-Organizer/
├── main.py                 # Entry point of the application
├── requirements.txt       # Python dependencies
├── requirements.md        # Project requirements document
├── README.md           
│
├── config/               # Configuration module
│   ├── __init__.py
│   ├── file_types.py     # File extension to category mapping
│   ├── options.py        # Menu options and strings
│   └── settings.py       # Global settings
│
├── database/             # Database management module
│   ├── __init__.py
│   ├── connection.py     # SQLite connection handler
│   ├── schema.py         # Database table definitions
│   ├── file_index.py     # File metadata operations
│   ├── analytics.py      # Data analysis functions
│   └── delete.py         # File deletion handlers
│
├── organizer/            # Core organization logic
│   ├── __init__.py
│   ├── organizer.py      # Main orchestration logic
│   ├── scanner.py        # Folder scanning
│   ├── classifier.py     # File type classification
│   ├── mover.py          # File movement operations
│   ├── validator.py      # Input/file validation
│   ├── metadata.py       # Extract file metadata
│   ├── hasher.py         # File hashing
│   └── path_manager.py   # Path handling utilities
│
├── visualisation/        # Data visualization module
    ├── __init__.py
    └── charts.py         # Graph generation

```

---

## 🔧 Core Modules

### 1. **config/** - Configuration
Defines file categories, user options, and global settings.

### 2. **database/** - Database Management
- **connection.py:** SQLite database connections
- **schema.py:** Table definitions
- **file_index.py:** CRUD operations for file metadata
- **analytics.py:** Statistical analysis

### 3. **organizer/** - File Organization Engine
- **scanner.py:** Recursively scans folders
- **classifier.py:** Determines file category
- **mover.py:** Handles safe file movement
- **metadata.py:** Extracts file information
- **validator.py:** Validates operations

### 4. **visualisation/** - Analytics & Charts
Generates matplotlib/seaborn visualizations for data analysis.

---

## 📊 Database Schema

```sql
CREATE TABLE files(
    id INTEGER PRIMARY KEY,
    file_name TEXT NOT NULL,
    extension TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    file_hash TEXT NOT NULL,
    mime_type TEXT,
    created_at TEXT,
    modified_at TEXT
)
```

---

## 🛡️ Safety Features

✅ **Never deletes files** - Files are only moved, not removed
✅ **Prevents overwrites** - Renames conflicts instead of replacing
✅ **Validates all operations** - Checks paths and permissions
✅ **Skips system files** - Protects hidden and system files
✅ **Error logging** - All errors logged for debugging
✅ **Graceful failure** - One file error doesn't stop the entire process

---

## 📦 Dependencies

```
pandas       - Data manipulation and analysis
matplotlib   - Visualization and plotting
seaborn      - Enhanced statistical graphics
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🎯 Use Cases

### Student Organization
Organize Downloads folder with multiple document types, images, and programming assignments.

### Developer Environment
Auto-organize project files, screenshots, and code snippets by type.

### Office Work
Manage business documents, reports, spreadsheets, and presentations.

### General Users
Keep Desktop and Downloads folders clean automatically.

---

## 🔍 Example Workflow

```python
# Step 1: Run the application
python main.py

# Step 2: Choose option 1 (Organize files)
Enter the path: C:\Users\YourName\Downloads

# Step 3: Program organizes files
✓ Scanned 245 files
✓ Created 8 category folders
✓ Moved 240 files
✓ 5 files skipped (unsupported types)
✓ Files saved to database

# Step 4: View results in database
python main.py → Option 2 → See all records

# Step 5: Analyze with graphs
python main.py → Option 3 → View analytics
```

---

## 📈 Analytics Examples

**Files by Extension Distribution:**
```
Images:      120 files (35%)
Documents:   85 files (25%)
Videos:      60 files (18%)
Audio:       45 files (13%)
Archives:    30 files (9%)
```

**Storage Usage:**
```
Videos:      2.5 GB (highest)
Images:      1.2 GB
Documents:   450 MB
Audio:       380 MB
Archives:    290 MB
```

---

## 🚫 What This Tool Does NOT Do

- ❌ Delete files permanently
- ❌ Overwrite existing files without warning
- ❌ Move hidden or system files
- ❌ Modify file contents
- ❌ Move folders (only individual files)
- ❌ Organize files outside the selected folder
- ❌ Crash on errors (graceful error handling)

---

## 🐛 Error Handling

The application handles various edge cases:

| Scenario | Behavior |
|----------|----------|
| Folder doesn't exist | Show error and exit |
| Folder is empty | Inform user and exit |
| Unknown file type | Move to "Others" folder |
| Destination exists | Reuse existing folder |
| Same filename exists | Rename file (v2 feature) |
| Permission denied | Log error and continue |
| Hidden/system files | Skip them safely |

---

## 📸 Screenshots / Visualization

The application generates charts showing:
- **File Distribution Chart** - Shows count of files per extension
- **Storage Usage Chart** - Displays size consumption by file type
- **Top Files Chart** - Identifies largest files in your folder

![alt text](image.png)

*Analytics visualization generated by charts.py*

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution:
- 🎨 New file categories
- 🔍 Enhanced search capabilities
- 📊 More visualization options
- 🔄 Undo/rollback functionality
- 🌐 GUI interface (Tkinter/PyQt)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Smart-File-Organizer**
- Built as a learning project for clean code architecture
- Focuses on real-world file management
- Emphasizes safety and reliability

---

## 🎓 Learning Goals

This project demonstrates:
- ✅ Clean project architecture
- ✅ File handling and I/O operations
- ✅ Database design and SQL
- ✅ Object-oriented programming
- ✅ Error handling and logging
- ✅ Data visualization
- ✅ Git workflows
- ✅ Documentation best practices

---

## 📞 Support

For issues, questions, or suggestions:
1. Open an issue on GitHub
2. Check existing documentation
3. Review the requirements.md file

---

## 🚀 Future Enhancements

- [ ] GUI interface with Tkinter
- [ ] Undo/rollback functionality
- [ ] Schedule automatic organization
- [ ] Custom category profiles
- [ ] Cloud storage support
- [ ] Duplicate file detection
- [ ] Web-based dashboard
- [ ] REST API

---

## ✨ Key Achievements

🎯 **Architecture:** Modular, extensible design
📊 **Database:** Comprehensive file tracking
📈 **Analytics:** Beautiful visualizations
🔐 **Safety:** Non-destructive operations
🧪 **Testing:** Unit test coverage
📚 **Documentation:** Complete and clear

---

**⭐ If you find this project helpful, please star it on GitHub!**

Last Updated: 2026
Version: 1.0.0
