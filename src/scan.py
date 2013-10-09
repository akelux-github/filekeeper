import os # use utitlies in os.path
from filedb import FILE_MD5
from md5file import md5file
from settings import __verbose

#use a queue data structure instead of list
class _Node(object):
    """
    Class for linked list node.
    """
    __slots__ = ['_data', '_next'] # data field and next field of an node
    def __init__(self, value, link):
        self._data = value
        self._next = link

class Queue(object):
    """
    A linked list based implementation of FIFO queue.
    This ensures constant time for "enque" (put an value
    into the queue ) and "deque" (get a value out of queue).
    """
    __slots__ = ['_head', '_tail'] # head and tail node of the queue
    def __init__(self):
        self._head=None
        self._tail=None

    """
    def empty(self):
        return self._head==None
    """

    def not_empty(self):
        """
        Test non emptiness of the queue.
        """
        return self._head!=None

    # get the first element of a non-empty queue
    def deque(self):
        """
        Pop the first element out of the queue.
        Return the value and remove the first element from the queue.
        """
        if self._head == None: # an exception will be raised if trying of deque a empty queue
            raise Exception("trying to pop an empty queue")

        data = self._head._data
        t = self._head
        self._head = self._head._next
        del t
        if self._head == None: # reset _tail if resulting an empty queue
            self._tail = None

        return data

    def enque(self, data):
        """
        Add an element to the the end of queue.

        """
        if self._tail == None:
            self._head=self._tail=_Node(data, None)
        else:
            self._tail._next = _Node(data, None)
            self._tail = self._tail._next

    def cat(self, other): # other might not hold valid reference to a queue
        """
        Concatente two queues to be one.
        Appending all elements in other to the end of the queue
        """
        if self._tail == None:
            self._head = other._head
            self._tail = other.tail
        else:
            self._tail._next = other._head
            self._tail = other._tail

# do breath first search of the directory tree
def scan(dir_init, db_init = None):
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
            # if name == '/Users/Rong/ProjectLocker/testsrc
            if __verbose:
                print "Scanning ", name
            
            if os.path.islink(name): # skip symbolic links
                pass
            elif os.path.isdir(name):
                queue.enque(name)
            elif os.path.isfile(name):
                size = os.path.getsize(name)
                ctime= os.path.getctime(name)
                md5 = md5file(name, size)
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