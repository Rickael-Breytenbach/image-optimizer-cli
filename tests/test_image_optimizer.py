import os
import shutil
from image_optimizer import resize_images, OUTPUT_FOLDER, zip_images, ZIP_NAME

SAMPLE_FOLDER = "sample_images"
TEST_OUTPUT = OUTPUT_FOLDER
TEST_ZIP = ZIP_NAME

def test_resize_images():
    # Ensure a clean start
    if os.path.exists(TEST_OUTPUT):
        shutil.rmtree(TEST_OUTPUT)
    if os.path.exists(TEST_ZIP):
        os.remove(TEST_ZIP)

    # Run the resize function
    resize_images(SAMPLE_FOLDER)

    # Check that output folder exists
    assert os.path.exists(TEST_OUTPUT), "Output folder was not created"

    # Check that at least one file exists in the output folder
    files = os.listdir(TEST_OUTPUT)
    assert len(files) > 0, "No images were resized and saved"

    # Test zip function
    zip_images()
    assert os.path.exists(TEST_ZIP), "ZIP file was not created"

    # Cleanup after test
    shutil.rmtree(TEST_OUTPUT)
    os.remove(TEST_ZIP)
