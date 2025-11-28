# Password Generator (Python Practice Project)

This is a **simple Python password generator** I built as a practice project while learning Python.

It’s nothing fancy or commercial — just a fun way to practice Python concepts like:

* User input and conditionals
* Loops and string manipulation
* Using external modules
* Building a Windows executable with PyInstaller

---

## Features

* Generate passwords of various lengths (Weak, Medium, Strong, or Custom)
* Toggle which characters to include: uppercase, lowercase, numbers, symbols
* Automatically copies the generated password to your clipboard
* Keeps the program open until you press Enter

---

## How to Run

1. Make sure Python is installed: [https://www.python.org/](https://www.python.org/)
2. Install the required module:

```bash
pip install pyperclip
```

3. Run the script in terminal/command prompt:

```bash
python password_generator.py
```

4. Follow the prompts to generate a password.

> Optional: If you want a standalone Windows executable, you can create it using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile password_generator.py
```

The `.exe` will be in the `dist/` folder.

---

## Notes

* This is a **practice project** — no claims of security or commercial use
* Focus was on learning Python and basic scripting skills

---

**Author:** Robert Alvarez
**Year:** 2025
**License:** None / Personal Learning Project
