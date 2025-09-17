import os
import urllib.request
import re
from urllib.parse import urlparse

def get_image_info(url):
    """Extracts the icon type, image name, and ID from the URL."""
    try:
        path_parts = urlparse(url).path.strip('/').split('/')
        icon_type = path_parts[0]
        image_info = path_parts[-1]
        
        match = re.search(r'_(\d+)$', image_info)
        if not match:
            return None, None, None
            
        image_id = match.group(1)
        image_name = image_info[:match.start()]
        return icon_type, image_name, image_id
    except Exception as e:
        print(f"Error parsing URL: {e}")
        return None, None, None

def construct_download_url(icon_type, image_name, image_id):
    """Constructs the download URL."""
    if not all([icon_type, image_name, image_id]):
        return None
    
    image_info_hyphenated = image_name.replace('_', '-')
    
    if icon_type == '3d-icon':
        url = f"https://cdn3d.iconscout.com/3d/premium/thumb/{image_info_hyphenated}-png-download-{image_id}.png"
    else:
        url = f"https://cdni.iconscout.com/illustration/premium/thumb/{image_info_hyphenated}-svg-download-png-{image_id}.png"
        
    return url

def create_filename(icon_type, image_name, image_id):
    """Creates a filename for the downloaded image."""
    if not all([icon_type, image_name, image_id]):
        return None
    
    image_info_hyphenated = image_name.replace('_', '-')
    
    if icon_type == '3d-icon':
        return f"{image_info_hyphenated}-png-download-{image_id}.png"
    else:
        return f"{image_info_hyphenated}-svg-download-png-{image_id}.png"

def download_image(download_url, folder_name, file_name):
    """Downloads and saves the image."""
    if not all([download_url, folder_name, file_name]):
        print("Invalid arguments for downloading image.")
        return

    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    except OSError as e:
        print(f"Error creating directory {folder_name}: {e}")
        return

    file_path = os.path.join(folder_name, file_name)

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0',
            'Cookie': '__cf_bm=vLOGDheL2t6lxMEzQjGRoGpxe15huiEUuCIhEYq.pnQ-1758137275-1.0.1.1-q2UiOMHBqEtUI2LKf8ZKHeyxb5XIFrtZZ.Gyc5q.lrMXkG5dMKpSmvRfNICzhqnlFYf_IN89RJJowbSnlfzlQKJPF35Eerfa_7In7bhHfHQ; XSRF-TOKEN=eyJpdiI6IlVVbFZsMWIzT0tmVmVCVkJaNUUwbnc9PSIsInZhbHVlIjoiZUUwT0hnUThpYnNrSlFzYmpYMWFtcGN4akNWdUlZZHBITVdCS3BoTTBUQlVMMGRkVm1aMUdkcWJjNGVLRzdLY3BMZzhReGp3NURRc1hCZU1pdkJ6Mm1WZ2veFFFWXZ1cXFEdlJFVFNZeHU4aFljdW5ZUE41TjFXTHY3V2dsRjYiLCJtYWMiOiJhZmI2ZTRlNDVmOWMyODg3YTFhYTk5ZjMxYTA2ZDRmNmNjNmQ5MDExMzk2ODUxMWI5ZGY5MjM2MzQxZGM2MzhlIiwidGFnIjoiIn0%3D; iconscout_session=eyJpdiI6IlB2c2pYeXJFQ1VMaHdLbzRxelBabkE9PSIsInZhbHVlIjoiMXZIUTZJdFdnK2lSMTdtMU9BVDFPMFEybjJpcVNpK0xrWnNoZmFhMEV1d1c1dHZocDRNRGJxdU5qdDhTbzQ3clorT2RDdGkrL2Zmd3FXWFljcFlIVnpGZVpkQ3FpcXlrN0N4aXU2U0puRkhhU2ZIMURwUzBHOUZVUzJDRnk0amMiLCJtYWMiOiJlOGE5OTE2MDBmZGIxZjQ2NWM2NGI1NjY1NTU0M2VhOWZlYmExMDQyMjc4MjhmYzUwNGM5NzcyZmU1ZDlmM2Y4IiwidGFnIjoiIn0%3D'
        }
        req = urllib.request.Request(download_url, headers=headers)
        with urllib.request.urlopen(req) as response, open(file_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Image downloaded and saved as {file_path}")
    except urllib.error.URLError as e:
        print(f"Error downloading image: {e}")

def main():
    """Main function to run the script."""
    url = input("Enter the IconScout URL: ").strip()

    icon_type, image_name, image_id = get_image_info(url)

    if not all([icon_type, image_name, image_id]):
        print("Could not extract image information from the URL.")
        return

    download_url = construct_download_url(icon_type, image_name, image_id)
    file_name = create_filename(icon_type, image_name, image_id)
    
    original_image_info = f"{image_name}_{image_id}"
    folder_name = original_image_info

    if download_url and file_name:
        download_image(download_url, folder_name, file_name)
    else:
        print("Failed to construct download URL or filename.")

if __name__ == "__main__":
    main()