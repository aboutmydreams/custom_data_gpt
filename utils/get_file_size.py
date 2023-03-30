import os

def get_file_size(filename):
    if not os.path.exists(filename):
        return None
    filesize = os.stat(filename).st_size
    return round(filesize/1024, 4)