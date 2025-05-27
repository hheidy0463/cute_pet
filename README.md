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

## Configuration

If `cute_pet` supports custom settings (e.g., reminder intervals, pet styles), you can adjust these in the `config.json` file or via command-line flags:

```bash
python cute_pet.py --reminders --interval 60
```

*(Update this section with any specific flags or config options.)*

## Usage Tips

* Right-click (or Ctrl-click) on the pet for a context menu with actions.
* Use the `--help` flag to see available options:

  ```bash
  python cute_pet.py --help
  ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   ```

git checkout -b feature/YourFeature

````
3. Commit your changes:
   ```bash
git commit -m "Add some feature"
````

4. Push to the branch:

   ```bash
   ```

git push origin feature/YourFeature

````
5. Open a Pull Request.

Please ensure your code follows the [PEP 8 style guide](https://peps.python.org/pep-0008/) and includes tests where applicable.

## License

This project is licensed under the MIT License. To verify:

1. Check the `LICENSE` file in the repo root. It should start with `MIT License` and include the full text.
2. Ensure the file is named `LICENSE` (no extension).
3. Run:
   ```bash
grep -R "MIT License" LICENSE
````

4. On GitHub, the repo page should display "MIT License" next to the project title.
