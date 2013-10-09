# data structure of file db:
#   a dictionary indexed by file size, with file character vector [file_path, ctime, md5]

# a file vector is a list has the following coordinates
FILE_NAME = 0
FILE_CTIME = 1
FILE_MD5 = 2 # raw md5 value
FILE_MD5_2 = 3 # true md5 value

#
def update_directory(curdb, path):
    """
    add a directory to scan
    """
    pass

#
def merge_db(db1, db2):
    """
    merge two db1 scanned separately
    Output:
        db_merged, db_duplicated
    """
    pass

