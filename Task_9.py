import os

class FileSystemError(BaseException):
    pass

class FSItem(object):
    module = os.path

    def __len__(self):
        # Return the size of the file in bytes
        # FSError if the file doesn't exist
        return os.stat(self).st_size

    __len__: property(
        __len__, None, None,
        # Size of the file, in bytes.
    )

    def __init__(self, path):
        # Creates new File instance by given path to file
        # Raise FileSystemError if the file is already present
        # Behaves like the "touch" command of BASH shell
        if self.isfile(path):
            raise FileSystemError("Can't create file: {0} already exist".format(self.getname()))
        fd = os.open(self, os.O_WRONLY | os.O_CREAT, 0o666)
        os.close(fd)
        os.utime(self, None)
        return self


    def rename(self, new):
        # Renames current FSItem
        if not self.isfile(path):
            raise FileSystemError("Can't create file: {0}, is not a file".format(self.getname()))
        os.rename(self, new)
        return self._next_class(new)

    def create(self, path):
        # Creates new item in OS, here a directory
        if not self.isdir(path):
            raise FileSystemError("Can't create dir: {0} already exist".format(self.getname()))
        os.mkdir(self, path, 0o777)

    def getname(self):
        # Return the name of the current item
        return self._next_class(self.module.basename(self))

    def isfile(self):
        # Check if the given file exists
        return os.path.isfile(self.path)

    def isdir(self):
        # Check if the current item exists and the current item
        # is in directory
        os.path.isdir(self.path)

class File(FSItem):

    # Child class of FSItem

    def make(self):
        # Creates new item in OS, here a file
        if self.isfile(path):
            raise FileSystemError("Can't create file: {0} already exist".format(self.getname()))
        fd = os.open(self, os.O_WRONLY | os.O_CREAT, 0o666)
        os.close(fd)
        os.utime(self, None)
        return self


    def getcontent(self):
        # Count the number of lines in a file
        return len(self.text(encoding, errors).splitlines(retain))

    def __iter__(self):
        # Return an iterator of lines in the given file
        # Raises FileSystemError if file does not exist
        # Reuse method getcontent here.
        for __iter__ in iter(lambda: f.read(size) or None, None):
            yield line

class Directory(FSItem):
    # Class for working with directories
    # Child of FSItem
    def __init__(self, path):
        # Creates new Directory
        if self.__init__(path):
            raise FileSystemError("Can't create Directory: {0}, already exists".format(self.getname()))
        os.mkdir(self, path)

    def items(self, *args, **kwargs):
        # Yields FSItem instances of items inside of current directory.
        return (
            item
            for item in self.walk(*args, **kwargs)
            if item.isdir()
        )

    def files(self, *args, **kwargs):
        # List of the files in this directory
        return [p for p in self.listdir(*args, **kwargs) if p.isfile()]

    def subdirectories(self, *args, **kwargs):
        # Yields Directory instances of directories inside of current directory.
        return [p for p in self.listdir(*args, **kwargs) if p.isdir()]

    def filesrecursive(self, *args, **kwargs):
        # Yields File instances of files inside of this
        # directory, inside of subdirectories of this directory and so on
        return (
            item
            for item in self.walk(*args, **kwargs)
            if item.isfile()
        )

    def getsubdirectory(self, match=None, errors='strict'):
        # Returns Directory instance with subdirectory
        # of current directory with name "name"
        class Handlers:
            def strict(msg):
                raise

            def warn(msg):
                warnings.warn(msg, TreeWalkWarning)

            def ignore(msg):
                pass

        if not callable(errors) and errors not in vars(Handlers):
            raise ValueError("invalid errors parameter")
        errors = vars(Handlers).get(errors, errors)

        match = matchers.load(match)

        try:
            childList = self.listdir()
        except Exception:
            exc = sys.exc_info()[1]
            tmpl = "Unable to list directory '%(self)s': %(exc)s"
            msg = tmpl % locals()
            errors(msg)
            return

        for child in childList:
            if match(child):
                yield child
            try:
                isdir = child.isdir()
            except Exception:
                exc = sys.exc_info()[1]
                tmpl = "Unable to access '%(child)s': %(exc)s"
                msg = tmpl % locals()
                errors(msg)
                isdir = False

            if isdir:
                for item in child.walk(errors=errors, match=match):
                    yield item

def main():

    Directory.create("dir", "C:\\Users\\LENOVO\\PycharmProjects\\untitled")
    os.chdir("C:\\Users\\LENOVO\\PycharmProjects\\untitled\\dir")
    File.make("new1.txt")
    File.make("new2.txt")


main()
