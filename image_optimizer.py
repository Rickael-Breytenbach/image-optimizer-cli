import os
from PIL import Image
import zipfile

# === SETTINGS ===
TARGET_SIZE = (2048, 2048)  # Resize dimensions
OUTPUT_FOLDER = "resized_images"
ZIP_NAME = "resized.zip"


def resize_images(input_folder):
    # Create output folder if it doesn’t exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Loop through all files in folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Try to open the file as an image
        try:
            with Image.open(file_path) as img:
                # Convert to RGB (fix issues with PNG/alpha channels)
                img = img.convert("RGB")
                # Resize image
                img = img.resize(TARGET_SIZE)
                # Save to output folder
                output_path = os.path.join(OUTPUT_FOLDER, filename)
                img.save(output_path, "JPEG")
                print(f"Resized and saved: {filename}")
        except Exception as e:
            print(f"Skipping {filename} (not an image). Error: {e}")


def zip_images():
    # Create a zip file with all resized images
    with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
        for filename in os.listdir(OUTPUT_FOLDER):
            file_path = os.path.join(OUTPUT_FOLDER, filename)
            zipf.write(file_path, arcname=filename)
    print(f"\nAll resized images zipped into {ZIP_NAME}")


if __name__ == "__main__":
    # Ask user for the input folder
    folder = input("Enter the path to the folder with your images: ").strip()

    if os.path.isdir(folder):
        resize_images(folder)
        zip_images()
        print("\n✅ Done! Check the 'resized_images' folder and 'resized.zip'.")
    else:
        print("❌ Invalid folder path. Please try again.")