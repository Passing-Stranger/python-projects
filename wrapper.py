import subprocess
import os


def convert_to_exe(script_path):
    # Ensure PyInstaller is available
    try:
        subprocess.run(["pyinstaller", "--version"], check=True)
    except FileNotFoundError:
        print("PyInstaller is not installed or not in PATH.")
        return

    # Define command to run PyInstaller
    command = ["pyinstaller", "--onefile", script_path]

    # Run the command
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created executable for {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create executable for {script_path}: {e}")


def main():
    # List of Python scripts to convert
    scripts = ["script1.py", "script2.py", "script3.py"]

    # Convert each script
    for script in scripts:
        if os.path.exists(script):
            convert_to_exe(script)
        else:
            print(f"Script {script} does not exist.")


if __name__ == "__main__":
    main()
# This is a wrapper for pyinstaller
