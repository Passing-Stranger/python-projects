import os
from PIL import Image
from tkinter import Tk, filedialog
from tqdm import tqdm


def resize_image(image_path, output_folder):
    with Image.open(image_path) as img:
        # Get current size
        width, height = img.size
        # Resize to 50% of original size
        img_resized = img.resize((width // 2, height // 2))
        # Save the resized image with 100% quality
        img_name = os.path.basename(image_path)
        img_resized.save(os.path.join(output_folder, img_name), quality=100)


def batch_resize_images():
    # Open file dialog to select multiple images
    Tk().withdraw()  # Hide the root window
    image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[
                                              ("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])

    # Open file dialog to select output folder
    output_folder = filedialog.askdirectory(title="Select Output Folder")

    if image_paths and output_folder:
        # Using tqdm for progress bar
        for image_path in tqdm(image_paths, desc="Resizing images", unit="image"):
            resize_image(image_path, output_folder)
        print(
            f"\nResized {len(image_paths)} images and saved to {output_folder}")
    else:
        print("No images selected and/or output folder not chosen \nPlease try again.")


if __name__ == "__main__":
    batch_resize_images()
