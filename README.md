# IconScout Image Downloader

This Python script downloads images from IconScout, supporting both "3d-icon" and "illustration" types. It takes a base URL from IconScout, constructs the appropriate download URL for the PNG version of the image, and saves it into a directory named after the icon.

## Features

-   Downloads images from IconScout URLs.
-   Supports both `3d-icon` and `illustration` image types.
-   Automatically constructs the correct CDN download URL.
-   Ensures the downloaded image is in PNG format.
-   Creates a dedicated directory for each downloaded image.
-   Cross-platform compatibility (Windows, macOS, and Linux).

## Requirements

-   Python 3.x

The script uses only Python's standard libraries (`os`, `urllib.request`, `re`, `urllib.parse`), so no external packages are required.

## Usage

1.  **Run the script from your terminal:**
    ```bash
    python3 download_icon.py
    ```

2.  **Enter the IconScout URL** when prompted. The URL should be the main page for the icon, not the direct image link.

    **Example URLs:**
    -   **3D Icon:** `https://iconscout.com/3d-icon/bloody-axe-3d-icon_13014413`
    -   **Illustration:** `https://iconscout.com/illustration/business-team-of-three-businesswomen-and-two-businessmen-illustration_8041661`

3.  The script will then download the image and save it in a newly created directory in the same location as the script.

    **Example Output:**
    ```
    Image downloaded and saved as business-team-of-three-businesswomen-and-two-businessmen-illustration_8041661/business-team-of-three-businesswomen-and-two-businessmen-illustration-svg-download-png-8041661.png
    ```

## How It Works

The script parses the input URL to determine the `icon_type` ("3d-icon" or "illustration"), the `image_name`, and the `image_id`. Based on the `icon_type`, it constructs a CDN URL pointing to the high-quality PNG version of the image. It then downloads the image and saves it locally.