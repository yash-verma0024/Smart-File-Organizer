**1. What problem does this project solve?**
* Organizes messy folders automatically.
* Saves time spent sorting files manually.
* Makes files easier to find.
* Reduces desktop/Downloads clutter.

**2. Who is the user?**

Examples:
* Students
* Developers
* Office workers
* Anyone with messy folders
* Windows/Linux users

**3. What should the program do?**
* Organize files by extension
* Organize by file type
* Organize by creation date
* Organize recursively
* Dry-run mode
* Undo
* Read all files in a selected folder.
* Detect each file's extension.
* Create category folders if needed.
* Move files into the correct folder.
* Log every operation.
* Skip unsupported file types safely.
  
**4. What should the program NOT do?**
* Never delete files
* Never overwrite files
* Never move hidden files
* Never organize system folders
* Modify file contents.
* Move folders (only files).
* Organize files outside the selected folder.
* Overwrite existing files without checking.
* Crash on errors.

**5. What happens if...**
* **Folder doesn't exist? →** Show an error and exit or ask user to create folder (also by giving default name or ask user to enter)
* **Folder is empty? →** Inform the user and exit.
* **Unknown file type? →** Move to an Others folder.
* **Destination folder already exists? →** Reuse it.
* **File with same name already exists? →** Skip or rename * (implement later).
* **Permission denied? →** Log the error and continue.
* **Hidden/system files? →** Skip them (optional for v1).
