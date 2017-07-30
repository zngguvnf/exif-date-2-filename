import os
import shutil
import exifread


def convert_timestamp(ExifTime):
    # converts Exif Timestamp '2015:12:27 09:43:44'
    # To ISO like Timestamp   '2015-12-27T09-43-44'
    # attrs = dir(ExifTime)
    values = getattr(ExifTime, 'values')
    # values = '2015:12:27 09:43:44'
    timestamp = values.replace(' ', 'T')
    timestamp = timestamp.replace(':', '-')
    return timestamp


# def rename_pictures(source='testfiles/source',
#                     destination='testfiles/destination'):
def rename_pictures(source='testfiles/source'):
    destination=source

    for file in os.listdir(source):
        if file != '.DS_Store':

            filename = os.path.splitext(file)[0] 
            extension = os.path.splitext(file)[1]

            f = open(source+'/'+file, 'rb')
            tags = exifread.process_file(f)

            if 'EXIF DateTimeOriginal' in tags.keys():
                ExifTime = tags['EXIF DateTimeOriginal']
                timestamp = convert_timestamp(ExifTime)

                shutil.copy(source + '/'
                            + file, destination
                            + '/' + timestamp
                            + '--' + filename
                            + extension)
            else:
                print('no EXIF Data found for %s' % file)
                shutil.copy(source + '/'
                            + file, destination
                            + '/' + filename
                            + '__' + 'noexif'
                            + extension)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--source', metavar='path', required=True,
                        help='path to source folder')
    # parser.add_argument('--destination', metavar='path', required=True,
    #                     help='path to destination folder')
    args = parser.parse_args()
    # rename_pictures(source=args.source, destination=args.destination)
    rename_pictures(source=args.source)
