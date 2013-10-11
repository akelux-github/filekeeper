'''
Created on Oct 10, 2013

@author: Rong
'''
# import os,string

class DICT(object):
    """
    Data structure for keeping search dirs.
    """
    __slots__ = ('_links_hash') # ('_name', '_links_hash')
    def __init__(self):
        # self._name = name # root
        # self._dir_set = set([])
        self._links_hash = None

class _DirTree(object):
    __slots__ = ('_root', '_root_added')
    def __init__(self):
        self._root = DICT()
        self._root_added = False

    def checked(self, dirname): # return true if already in; else false and add
        """
        Add a dirname to the tree; if already there, return False, otherwise return True.

        Assume the dirname has is in abstract form
        """
        if self._root_added == True:
            return False

        splitted = dirname.split('/') # for windows, we shall use '\'?
        cur_node = self._root
        new_node = None
        for d in splitted:
            if not d: # skip empty names
                continue

            if cur_node._links_hash == None:
                new_node = DICT()
                cur_node._links_hash = {d:new_node}
                cur_node = new_node
            elif cur_node._links_hash.has_key(d):
                cur_node = cur_node._links_hash[d]
                if cur_node._links_hash == None:
                    return False
            else:
                new_node = DICT()
                cur_node._links_hash[d]=new_node
                cur_node = new_node


        if new_node == None:
            cur_node._links_hash=None
            if cur_node == self._root:
                self._root_added = True

        return True

    def add_dir(self, dirname): # return true if already in; else false and add
        """
        Add a dirname to the tree; if already there, return False, otherwise return True.

        Assume the dirname has is in abstract form
        """
        if self._root_added == True:
            return False

        splitted = dirname.split('/') # for windows, we shall use '\'?
        cur_node = self._root
        new_node = None
        for d in splitted:
            if not d: # skip empty names
                continue

            if cur_node._links_hash == None:
                new_node = DICT()
                cur_node._links_hash = {d:new_node}
                cur_node = new_node
            elif cur_node._links_hash.has_key(d):
                cur_node = cur_node._links_hash[d]
                if cur_node._links_hash == None:
                    return False
            else:
                new_node = DICT()
                cur_node._links_hash[d]=new_node
                cur_node = new_node


        if new_node == None:
            cur_node._links_hash=None
            if cur_node == self._root:
                self._root_added = True

        return True



class ScanCache(object):
    __slots__=('_searched', '_filedb', '_duplicated', '_queue', '_searched_lock', '_filedb_lock', '_duplicated_lock', '_searced_lock')
    '''
    Thread safe class for caching processing data
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._searched = _DirTree()


    def dir_checked(self, dirname):
        """
        If a dir's parent is in the searched cache, it is regarded as checked (or scheduled to be checked).
        """
        pass

    def add_dir(self, dirname):
        """
        Add dirname to the queue to be scanned and searched cache.
        """
        if self._searched.add_dir(dirname):
            self._queue.add(dirname)

    def remove_file(self,file_vec,*morefiles):
        """
        Remove a file from file system and update cache (filedb and duplicated) accordingly.
        """
        #keep latest?
        pass

    def db_append(self, size, *others):
        pass

    def dup_append(self, name, ctime, md5, size):
        pass

