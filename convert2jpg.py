import os
from pdf2image import convert_from_path

# Function to convert PDF to images
def pdf_to_images(pdf_path, output_folder, dpi=300):
    # Convert PDF to list of images
    images = convert_from_path(pdf_path, dpi=dpi)
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Save images as JPG
    image_paths = []
    for i, img in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i+1}.jpg")
        img.save(image_path, "JPEG")
        image_paths.append(image_path)

    return image_paths

# Example usage
pdf_path = "Sources/Testsources/PORCONES.228.35 – 1636.pdf"  # Change this to your PDF file
output_folder = "Sources/file6_images"  # Folder to save images

image_files = pdf_to_images(pdf_path, output_folder)
print("Saved images:", image_files)
