# Password Manager (CLI)

A command-line based password manager built using Python.
This project stores credentials securely using hashed passwords
and provides controlled access to stored data.

## Features
- Add new credentials (service, username, password)
- View stored services (service names only)
- View username after password verification
- Search services (case-insensitive, partial match)
- Delete a credential with confirmation
- Clear entire vault with confirmation
- File-based persistent storage

## Security Notes
- Passwords are NEVER stored in plain text
- Passwords are hashed using MD5 before saving
- Verification is done by hashing input password and comparing hashes
- Passwords are never printed on screen

⚠️ Note: MD5 is used here for learning purposes only.
In real-world applications, stronger hashing algorithms
like bcrypt or SHA-256 with salt should be used.

## Tech Stack
- Python
- File Handling
- Hashing (hashlib)
- CLI-based user interaction

## File Structure
password-manager-cli/
├── password_manager.py
├── vault.txt
├── README.md
└── .gitignore

## How to Run
1. Make sure Python is installed
2. Clone the repository
3. Run the program:
