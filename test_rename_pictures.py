import os
from rename_pictures import rename_pictures


def test_move_files():
    source = 'testfiles/source'
    destination = 'testfiles/destination'

    num_files_source = len([name for name in os.listdir(source)
                            if name != '.DS_Store'])
    
    rename_pictures(source, destination)

    num_files_destination = len([name for name in os.listdir(destination)
                                 if name != '.DS_Store'])

    assert num_files_source == num_files_destination
