import os
from pathlib import Path
from zipfile import ZipFile


HOME_DIR = Path(__file__).resolve().parent


if __name__ == "__main__":
    filename = None

    for _ in range(2021):
        if filename is not None:
            os.remove(filename)
            
        filename = os.path.join(HOME_DIR, list(filter(lambda file: file.endswith(".zip"), os.listdir(HOME_DIR)))[0])

        with ZipFile(filename) as zip_file:
            zip_file.extractall(HOME_DIR)
        