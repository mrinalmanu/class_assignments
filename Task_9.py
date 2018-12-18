import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''
    pass


class FSItem(object):
    ''' Common class for OS items OS: Files and Directories '''

    def __init__(self, path):
        ''' Creates new FSItem instance by given path to file '''
        self.path = path

    def rename(self, newname):
        ''' Renames current item
                raise FileSystemError if item does not exist
                raise FileSystemError if item "newname" already exists '''
        if self.getname() == newname:
            if os.path.exists(os.path.join(os.path.split(self.path)[0], newname)):
                raise FileSystemError("Item {0} already exists".format(newname))
            elif not os.path.exists(self.path):
                raise FileSystemError("Item {0} does not exist".format(self.path))
        else:
            newpath = os.path.join(os.path.split(self.path)[0], newname)
            return os.rename(self.path, newpath)

    def create(self):
        ''' Creates new item in OS
                raise FileSystemError if item with such path already exists '''
        if os.path.exists(self.path):
            raise FileSystemError("Item {0} with such path already exists".format(self.path))
        else:
            open(self.path, 'a').close()

    def getname(self):
        ''' Returns name of current item '''
        return os.path.basename(self.path)

    def isfile(self):
        ''' Returns True if current item exists and current item is file, False otherwise '''
        if os.path.isfile(self.path):
            return True
        else:
            return False

    def isdirectory(self):
        ''' Returns True if current item exists and current item is directory, False otherwise '''
        if os.path.isdir(self.path):
            return True
        else:
            return False


class File(FSItem):
    ''' Class for working with files '''

    def __init__(self, path):
        ''' Creates new File instance by given path to file
                raise FileSystemError if there exists directory with the same path '''
        self.path = path
        if os.path.isdir(self.path):
            raise FyleSystemError("Item {0} is a directory".format(self.path))

    def __len__(self):
        ''' Returns size of file in bytes
                raise FileSystemError if file does not exist '''
        if not os.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.path))
        else:
            os.path.getsize(self.path)

    def getcontent(self):
        ''' Returns list of lines in file (without trailing end-of-line)
                raise FileSystemError if file does not exist '''
        if not os.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.path))
        else:
            open(self.path, 'r').read().split('\n')

    def __iter__(self):
        ''' Returns iterator for lines of this file
                raise FileSystemError if file does not exist '''
        if not os.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.path))
        else:
            return iter(self.getcontent())


class Directory(FSItem):
    ''' Class for working with directories '''

    def __init__(self, path):
        ''' Creates new Directory instance by given path
                raise FileSystemError if there exists file with the same path '''
        self.path = path
        if os.path.isfile(self.path):
            raise FyleSystemError("Item {0} is a file".format(self.path))

    def items(self):
        ''' Yields FSItem instances of items inside of current directory
                raise FileSystemError if current directory does not exists '''
        if os.path.exists(self.path):
            for item in os.listdir(self.path):
                newpath = os.path.join(self.path, item)
                if os.path.isfile(newpath):
                    yield File(newpath)
                elif os.path.isdir(newpath):
                    yield Dir(newpath)
        else:
            raise FileSystemError("Item {0} does not exist".format(self.path))

    def files(self):
        ''' Yields File instances of files inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not os.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.path))
        else:
            yield from filter(lambda f: f.isfile(), self.items())

    def subdirectories(self):
        ''' Yields Directory instances of directories inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not os.path.exists(self.path):
            raise FileSystemError("Subdirectory {0} does not exist".format(self.path))
        else:
            yield from filter(lambda sd: sd.isdir(), self.items())

    def filesrecursive(self):
        ''' Yields File instances of files inside of this directory,
                inside of subdirectories of this directory and so on...
                raise FileSystemError if directory does not exist '''
        if not os.path.exists(path):
            raise FileSystemError("File {0} does not exist".format(self.path))
        else:
            for directories, files in os.walk(self.path):
                for file in files:
                    yield os.path.join(self.path, file)
                for directory in directories:
                    yield os.path.join(self.path, directory)

    def getsubdirectory(self, name):
        ''' Returns Directory instance with subdirectory of current directory with name "name"
                raise FileSystemError if item "name" already exists and item "name" is not directory '''
        if os.path.exists(os.path.join(self.path, name)):
            raise FileSystemError("Item {0} already exists".format(os.path.join(self.path, name)))
        elif not os.path.isdir(os.path.join(self.path, name)):
            raise FileSystemError("Item {0} is not directory".format(os.path.join(self.path, name)))
        else:
            return directory(os.path.join(self.path, name))
        
