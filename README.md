# cute\_pet

An adorable animated desktop pet written in Python. `cute_pet` is packaged into a standalone application using PyInstaller, so it can run on Windows, macOS, and Linux without requiring a separate Python installation.

## Features

* A small, animated pet that roams around your desktop
* Interactive behaviors such as following the cursor or responding to clicks
* Optional reminder functionality for quick prompts throughout the day
* Cross-platform support (Windows, macOS, Linux)

## Prerequisites

* Python 3.7 or higher (only required if running from source)
* `pip` for installing dependencies

## Installation (from source)

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/cute_pet.git
   cd cute_pet
   ```
2. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\\Scripts\\activate    # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:

   ```bash
   python cute_pet.py
   ```

## Packaging with PyInstaller

To generate a standalone executable:

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```
2. Build the executable:

   ```bash
   pyinstaller --onefile --windowed cute_pet.py
   ```
3. After the build completes, find the packaged application in the `dist/` directory:

   * **Windows**: `dist\\cute_pet.exe`
   * **macOS**: `dist/cute_pet.app`
   * **Linux**: `dist/cute_pet`

You can distribute the contents of the `dist/` folder. Users do not need Python installed to run the pet.
