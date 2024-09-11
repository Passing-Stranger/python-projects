````markdown
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
````

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
