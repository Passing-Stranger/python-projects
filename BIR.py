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
        print(f"Resizing {len(image_paths)} images...")
        # First, resize all images
        for image_path in tqdm(image_paths, desc="Resizing images", unit="image"):
            resize_image(image_path, output_folder)

        print(f"\nDeleting original files...")
        # Then, delete the original images after resizing
        for image_path in tqdm(image_paths, desc="Deleting originals", unit="file"):
            os.remove(image_path)  # Delete the original image

        print(
            f"\nSuccessfully resized and deleted {len(image_paths)} original images. Resized files saved to {output_folder}")
    else:
        print("No images selected or output folder not chosen")


if __name__ == "__main__":
    batch_resize_images()

# note i added line 30 to delete the og image after all, and i changed the ratio from 50% to 10%.
