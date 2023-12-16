import zipfile

def extract_archive(archivepaths, dest_dir):
    with zipfile.ZipFile(archivepaths, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("C:\\Users\\Tiziano Pacifico\\Desktop\\Python course\\compressed.zip",
                    "C:\\Users\\Tiziano Pacifico\\Desktop\\Python course")
