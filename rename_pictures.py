import os
import shutil
import exifread


def convert_timestamp(ExifTime):
    # converts Exif Timestamp '2015:12:27 09:43:44'
    # To ISO like Timestamp   '2015-12-27T09-43-44'
    #attrs = dir(ExifTime)
    values = getattr(ExifTime, 'values')
    # values = '2015:12:27 09:43:44'
    timestamp = values.replace(' ', 'T')
    timestamp = timestamp.replace(':', '-')
    return timestamp


def rename_pictures(source='htc-desire',
                    destination='htc-desire_out'):

    for filename in os.listdir(source):
        if filename != '.DS_Store':
            extension = os.path.splitext(filename)[1]

            f = open(source+'/'+filename, 'rb')
            tags = exifread.process_file(f)

            if 'EXIF DateTimeOriginal' in tags.keys():
                ExifTime = tags['EXIF DateTimeOriginal']
                timestamp = convert_timestamp(ExifTime)

                shutil.copy(source + '/'
                            + filename, destination
                            + '/' + timestamp + extension)
            else:
                print('no EXIF Data found for %s' % filename)

if __name__ == "__main__":
    rename_pictures()
