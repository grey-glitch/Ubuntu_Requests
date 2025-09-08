import os
import requests
from urllib.parse import urlparse
import uuid

def download_image():
    # Prompt user for the image URL
    url = input("Enter the image URL: ").strip()

    # Directory for storing fetched images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Send HTTP GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for HTTP codes like 404, 500, etc.

        # Try to extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename is found, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Full path for saving the image
        file_path = os.path.join(save_dir, filename)

        # Save the image in binary mode
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully downloaded and saved as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to download the image. Error: {e}")

if __name__ == "__main__":
    download_image()
