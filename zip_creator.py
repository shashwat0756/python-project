import zipfile
import pathlib


def make_achive(filepaths,dest_dir):
    dest_path = pathlib.Path(dest_dir,"processed.zip")
    with zipfile.ZipFile(dest_path,"w") as file:
       for filepath in filepaths:
           filepath = pathlib.Path(filepath)
           file.write(filepath,arcname=filepath.name)


if __name__ == "__main__":
    make_achive(filepaths=["bonus15.py","bonus16.py"], dest_dir="filesss")

