import urllib.request
import os

img_urls = [
    "https://via.placeholder.com/300.jpg",
    "https://via.placeholder.com/400.png"
]

input_folder = "/Users/rishibharath/Desktop/VS/Python/project/input_images"
os.makedirs(input_folder, exist_ok=True)

for idx, url in enumerate(img_urls, 1):
    filename = f"test{idx}.jpg" if url.endswith(".jpg") else f"test{idx}.png"
    path = f"{input_folder}/{filename}"
    urllib.request.urlretrieve(url, path)
    print(f"✅ Downloaded: {path}")
