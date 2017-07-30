import os
import shutil


def rename_pictures(source='testfiles/source',
                    destination='testfiles/destination'):

    for filename in os.listdir(source):
        shutil.copy(source + '/' + filename, destination)


if __name__ == "__main__":
    rename_pictures()
