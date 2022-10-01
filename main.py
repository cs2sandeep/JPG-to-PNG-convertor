import sys
from pathlib import Path
from j2p import JPG_to_PNG_converter


def main():
    # grab first and second argument i.e. source and dest folder names
    no_of_folders = len(sys.argv) - 1
    if no_of_folders != 2:
        raise Exception(f"Expected 2 arguments, received {no_of_folders} arguments")

    source_path = Path(sys.argv[1])
    dest_path = Path(sys.argv[2])

    try:
        JPG_to_PNG_converter(source_path, dest_path)
    except FileNotFoundError as err:
        print(err)
    except TypeError as err:
        print(err)


if __name__ == "__main__":
    main()
