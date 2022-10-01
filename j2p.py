# from pathlib import Path
from PIL import Image


def JPG_to_PNG_converter(source_folder_path, dest_folder_path):
    # check if source folder is present and is, in fact, a folder
    if not source_folder_path.exists():
        raise FileNotFoundError(f"Source folder {source_folder_path}/ not found")
    if not source_folder_path.is_dir():
        raise TypeError(f"{source_folder_path} is a file, expected folder")
    else:
        image_paths = [file for file in source_folder_path.glob("*.jpg")]

    # check if destination folder exists, if not create it
    if len(image_paths) == 0:
        print("No .jpg files found to process")
        return
    dest_folder_path.mkdir(exist_ok=True)

    # loop through source folder and convert jpg to png, then save them to the destination folder
    for image_path in image_paths:
        im = Image.open(image_path)
        im.save(f"{image_path.parent.parent / dest_folder_path / image_path.stem}.png")
