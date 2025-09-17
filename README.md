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

## Setup and Usage

Follow these steps to set up and run the script.

### 1. Setup

-   **Python 3.x:** Ensure you have Python 3.x installed. You can check by running `python3 --version` or `python --version`.
-   **Clone or Download:** Get the `download_icon.py` script by cloning this repository or downloading it directly.

### 2. Virtual Environment Setup (Recommended)

Using a virtual environment is a best practice to keep project dependencies isolated.

1.  **Navigate to the project directory:**
    ```bash
    cd path/to/your/directory
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment:**

    -   **On Windows (Command Prompt or PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```

    -   **On Linux and macOS:**
        ```bash
        source venv/bin/activate
        ```

    Your terminal prompt should now show `(venv)` at the beginning.

### 3. Running the Script

1.  **Make sure your virtual environment is active.**
2.  **Run the script from the project directory:**
    ```bash
    python3 download_icon.py
    ```

### 4. Downloading an Image

1.  After running the script, you will be prompted to **enter the IconScout URL**.
    ```
    Enter the IconScout URL:
    ```
2.  **Paste the full URL** of the icon's main page and press Enter.

    **Example URLs:**
    -   **3D Icon:** `https://iconscout.com/3d-icon/bloody-axe-3d-icon_13014413`
    -   **Illustration:** `https://iconscout.com/illustration/business-team-of-three-businesswomen-and-two-businessmen-illustration_8041661`

3.  The script will create a new folder named after the icon and save the PNG image inside it.

    **Example Output:**
    ```
    Image downloaded and saved as business-team-of-three-businesswomen-and-two-businessmen-illustration_8041661/business-team-of-three-businesswomen-and-two-businessmen-illustration-svg-download-png-8041661.png
    ```

## How It Works

The script parses the input URL to determine the `icon_type` ("3d-icon" or "illustration"), the `image_name`, and the `image_id`. Based on the `icon_type`, it constructs a CDN URL pointing to the high-quality PNG version of the image. It then downloads the image and saves it locally.