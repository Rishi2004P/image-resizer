import os
from PIL import Image, UnidentifiedImageError

# Paths
input_folder = "/Users/rishibharath/Desktop/VS/Python/project/input_images"
output_folder = "/Users/rishibharath/Desktop/VS/Python/project/output_images"
target_size = (800, 800)
output_format = "JPEG"
output_extension = ".jpg"

# Create output folder if not exist
os.makedirs(output_folder, exist_ok=True)

# Process images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        input_path = os.path.join(input_folder, filename)
        try:
            if os.path.getsize(input_path) == 0:
                print(f"⚠️ Skipping empty file: {filename}")
                continue

            with Image.open(input_path) as img:
                # Resize with optional aspect ratio preservation
                img = img.convert("RGB")  # Convert to RGB to avoid PNG errors
                img.thumbnail(target_size)  # Preserves aspect ratio
                output_path = os.path.join(
                    output_folder, os.path.splitext(filename)[0] + output_extension
                )
                img.save(output_path, output_format)
                print(f"✅ Saved: {output_path}")

        except UnidentifiedImageError:
            print(f"❌ Skipping corrupt or invalid image: {filename}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
