import os # use utitlies in os.path
from filedb import *
from md5file import md5file

#use a queue data structure instead of list
class _Node(object):
    __slots__ = ['_data', '_next']
    def __init__(self, value, link):
        self._data = value
        self._next = link

class Queue(object):
    __slots__ = ['_head', '_tail']
    def __init__(self):
        self._head=None
        self._tail=None

    """
    def empty(self):
        return self._head==None
    """

    def not_empty(self):
        return self._head!=None
    
    # get the first element of a non-empty queue
    def deque(self):
        if self._head == None:
            raise Exception("trying to pop an empty queue")

        data = self._head._data
        t = self._head
        self._head = self._head._next
        del t
        if self._head == None: # reset _tail if resulting an empty queue
            self._tail = None
        
        return data

    def enque(self, data):
        if self._tail == None:
            self._head=self._tail=_Node(data, None)
        else:
            self._tail._next = _Node(data, None)
            self._tail = self._tail._next

# do breath first search of the directory tree
def scan(dir_init, db_init=None)
    duplicated = [] # list of duplicated files
    filedb = {}
    if type(db_init) == dict:
        filedb = db_init
    queue = Queue()
    if os.path.exists(dir_init):
        queue.enque(dir_init)

    while queue.not_empty():
         top = queue.deque()
         dir_listing = os.listdir(top)
         for name in dir_listing:
            name = os.path.join(top, name)
            if os.path.isdir(name):
                queue.enque(name)
            elif os.path.isfile(name):
                size = os.path.getsize(name)
                ctime= os.path.getctime(name)
                md5 = md5file(name)
                if filedb.has_key(size):
                    # if size<64:
                    for file_vec in filedb[size]:
                        if md5 == file_vec[FILE_MD5]:
                            duplicated.append([name, ctime, md5, size])
                        else:
                            filedb[size].append([name, ctime, md5])
                else:
                    filedb[size]=[[name, ctime, md5]]
    return filedb, duplicated
