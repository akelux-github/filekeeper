import hashlib # will use the md5 utility there

from settings import __verbose

def md5file(file_path, size, blocks = 2L):
    try:
        f = open(file_path, 'rb')
        md5 = hashlib.md5()
        per_block_size = size/blocks
        per_block_size = per_block_size - (per_block_size % 512)
        seek_offset = 0
        if per_block_size > md5.block_size:
            seek_offset = per_block_size - md5.block_size

        if __verbose:    
            print "seek_offset: ", seek_offset
            
        while True:
            data = f.read(md5.block_size)
            if not data:
                break
            else:
                f.seek(seek_offset, 1) # seek is quite slow, even compare to read
            md5.update(data)
        f.close()    
        return md5.digest()
    except IOError as e:
        if __verbose:
            print e
        return None

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
