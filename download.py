import os
from pathlib import Path

import requests
import logging


def _preprocess_output_path(output_path: Path, extension: str) -> Path:
    filename = output_path.stem.lower().replace(" ", "_") + extension
    return output_path.parents[0] / filename


def download_media(source_url: str, output_path: Path, extension: str) -> None:
    output_path = _preprocess_output_path(output_path, extension)
    if os.path.exists(output_path):
        return
    r = requests.get(source_url)
    if r.status_code == 200:
        with open(output_path, "ab") as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
        logging.info("Completed media download.")
