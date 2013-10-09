import hashlib # will use the md5 utility there

"""
# compute the md5 of a regular file (existing)
def md5file(file_path, block_size=4*2**10):
    try:
        f = open(file_path, 'rb')
        md5 = hashlib.md5()
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
        f.close()    
        return md5.digest()
    except IOError as e:
        if __verbose:
            print e
        return None
"""

def md5file(file_path, size, blocks = 2L):
    try:
        f = open(file_path, 'rb')
        md5 = hashlib.md5()
        seek_offset = size/blocks - md5.block_size
        while True:
            data = f.read(md5.block_size)
            if not data:
                break
            else:
                f.seek(seek_offset, 1)
            md5.update(data)
        f.close()    
        return md5.digest()
    except IOError as e:
        if __verbose:
            print e
        return None

