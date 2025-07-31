from pathlib import Path
import requests


def download_data_from_url(url: str, url_path: Path):
    """
    Download data from a given URL and save it to the specified destination.
    Args:
        url (str): The URL to download the data from.
        url_path (Path): The destination path.
    """

    if not url_path.exists():
        response = requests.get(url)
        response.raise_for_status()
        with open(url_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded data from {url} to {url_path}")
    else:
        print(f"File already exists at {url_path}, skipping download.")
