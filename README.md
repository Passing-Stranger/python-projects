# 🖼️ Batch Image Resizer

<pre>
          .?77777777777777$.                  .?77777777$.  
          777..777777777777$+                 777.77777777$  
         .77    7777777777$$$                .77   77777777$  
         .777 .7777777777$$$$                .777  .7777777$  
         .7777777777777$$$$$$               .7777777777777$  
         ..........:77$$$$$$$               ..........:77$$$  
  .77777777777777777$$$$$$$$$.=======.  .77777777777777777$$$$$.==.  
 777777777777777777$$$$$$$$$$.========  777777777777777777$$$$$$$.===  
7777777777777777$$$$$$$$$$$$$.========= 7777777777777777$$$$$$$$$$$.===  
77777777777777$$$$$$$$$$$$$$$.========= 77777777777777$$$$$$$$$$$$$$$.===  
777777777777$$$$$$$$$$$$$$$$ :========+. 777777777777$$$$$$$$$$$$$$$$ :===  
77777777777$$$$$$$$$$$$$$+..=========++~ 77777777777$$$$$$$$$$$$$$+..===+  
777777777$$..~=====================+++++  777777777$$..~=================+++++  
77777777$~.~~~~=~=================+++++.  77777777$~.~~~~=~===============+++++  
777777$$$.~~~===================+++++++.  777777$$$.~~~================+++++++  
77777$$$$.~~==================++++++++:   77777$$$$.~~================+++++++  
 7$$$$$$$.==================++++++++++.   7$$$$$$$.================+++.+++  
 .,$$$$$$.================++++++++++~.    .,$$$$$$.===============++++++++.  
         .=========~.........                .=========~...........   
         .=============++++++               .=============++++++    
         .===========+++..+++               .===========+++..+++   
         .==========+++.  .++               .==========+++.  .++  
          ,=======++++++,,++,               ,=======++++++,,++,  
          ..=====+++++++++=.                ..=====+++++++++=.   
                ..~+=...                        ..~+=...
</pre>

**Batch Image Resizer** is a Python script that allows you to select multiple images, resize them down by 50%, and save them with 100% quality. It also provides a loading bar and deletes the original images after resizing!

## ✨ Features

- Batch resize multiple images by 50%
- 100% image quality preservation
- Progress bar in the CLI to track the resizing process
- Deletes original files after resizing
- Simple file selection via a graphical interface (Tkinter)

## 🚀 How to Use

1. **Install required libraries:**

   You need `PIL` (Pillow) for image processing and `tqdm` for the progress bar. You can install them using `pip`:

   ```bash
   pip install pillow tqdm
   ```

2. **Run the script:**

   Execute the Python script to batch resize your images:

   ```bash
   python batch_resize.py
   ```

   A file dialog will prompt you to select the images you want to resize, and then another dialog will allow you to choose the output folder. After resizing, the original images will be deleted.

## 📂 File Structure

```plaintext
.
├── batch_resize.py      # Main script
└── README.md            # This file
```

## 🛠️ Requirements

- Python 3.x
- Pillow (for image manipulation)
- Tkinter (for file selection)
- Tqdm (for progress bar)

## 🌟 Example

Here's how the progress looks when resizing and deleting images:

```
Resizing images: 100%|████████████████████| 5/5 [00:10<00:00, 2s/image]
Deleting originals: 100%|█████████████████| 5/5 [00:01<00:00, 4files/s]
```

## 🖼️ Output

The resized images will be stored in the selected output folder with the same filenames as the original images.

Enjoy hassle-free image resizing! 🎉

# Python Script Wrapper for PyInstaller

Welcome to the **Python Script Wrapper** project! This tool simplifies the process of converting multiple Python scripts into standalone executables using `PyInstaller`. Perfect for batch processing or automation tasks.

## 🛠️ Features

- **Batch Processing:** Convert multiple Python scripts into executables with a single command.
- **Automated Execution:** Automate the process of calling `PyInstaller` for each script.
- **Custom Configuration:** Easily adjust and configure `PyInstaller` options for your needs.
- **Error Handling:** Provides feedback if scripts do not exist or if there are errors during conversion.

## 🚀 Getting Started

### Prerequisites

- **Python**: Ensure Python is installed on your system.
- **PyInstaller**: Install `PyInstaller` if it's not already installed. You can install it via pip:

  ```bash
  pip install pyinstaller
  ```

## Installation

Clone the Repository

Clone this repository to your local machine:

```bash
Copy code
git clone https://github.com/yourusername/python-script-wrapper.git
cd python-script-wrapper
```

### Configure Scripts

Add the names of the Python scripts you want to convert in the scripts list within wrapper.py.

### Run the Wrapper

Execute the wrapper.py script to convert your Python files:

```bash
python wrapper.py
```

This command will process each script listed in the scripts list and generate corresponding executables.

## 💡 Usage

Edit wrapper.py to include the Python scripts you want to convert. By default, the script includes placeholders for script1.py, script2.py, and script3.py. Modify this list according to your needs.

Here is an example of how to configure wrapper.py:

```python
def main():
    scripts = ["my_script1.py", "my_script2.py", "my_script3.py"]
    for script in scripts:
        if os.path.exists(script):
            convert_to_exe(script)
        else:
            print(f"Script {script} does not exist.")
```

## ⚙️ Customization

You can adjust the convert_to_exe function in wrapper.py to include additional PyInstaller options. For instance, you can change the --onefile flag to include other options such as --noconsole or --icon:

python
Copy code
command = ["pyinstaller", "--onefile", "--noconsole", script_path]

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📄 Contributing

Feel free to open issues or pull requests if you find bugs or want to contribute enhancements. For major changes, please open an issue first to discuss what you would like to change.
