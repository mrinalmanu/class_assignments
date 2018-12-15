import os

class FileSystemError(Exception):
    pass


class FSItem(object):

    def __init__(self, path):
        ''' Initialize current file item '''
        self.path = os.path.normpath(path)

    def rename(self, new):
        ''' Returns a new name '''
        if os._exists(self):
            raise FileSystemError("No can do, {0}, already exists".format(self.path))
        else:
            self.path = os.path.split(self.path)[0] + '\\' + new

    def create(selfs):
        ''' Make new item in OS '''
        if os.path.exists(self.path):
            raise FileSystemError("No can do, {0}, already exists".format(self.path))
        else:
            open(self.path, 'a').close()


    def getname(self):
        ''' Name of current item '''
        return os.path.split(self.path)[1]

    def isfile(self):
        ''' True/ False for file '''
        return os.path.isfile(self.path)

    def isdirectory(self):
        ''' True/ False for dir '''
        return os.path.isdir(self.path)

class File(FSItem):

    def __init__(self, path):
        ''' Makes new file in OS '''
        try:
            if os.path.exists(self.path):
                raise FileSystemError("No can do, {0}, already exists".format(self.path))
        except:
            super(File, self).__init__(path)

    def __len__(self):
        ''' Tells length of the file '''
        if os.path.exists(self.path):
            os.path.getsize(self.path)
        else:
            raise FileSystemError("No can do, {0}, doesn't exists".format(self.path))

    def getcontent(self):
        ''' Return list of lines in the file '''
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return list(map(lambda x: x.strip(), f.readlines()))
        else:
            raise FileSystemError("No can do, {0}, already exists".format(self.path))

    def __iter__(self):
        ''' Return iterator for line '''
        if os.path.exists(self.path):
            with open(self.path) as f:
                self.all_lines = f.readlines()
            self.iterate = 0
            return self
        else:
            raise FileSystemError('{0}, dose not exist'.format(self.path))

    def __next__(self):
        if self.iterate < len(self.all_lines):
            x = self.all_lines[self.iterate].strip()
            self.iterate += 1
            return self
        else:
            raise FileSystemError("{0}, does not exist".format(self.path))


class Directory(FSItem):

    def __init__(self, path):
        ''' Makes a new dir '''
        if os.path.exists(self.path):
            raise FileSystemError('No can do, {0}, already exists'.format(self.path))
        else:
            os.mkdir(self.path, mode=0o777)

    def items(self):
        ''' leads items inside current dir'''
        if os.path.exists(self.path):
            for name in os.listdir(self.path):
                yield FSItem(self.path + '\\' + name)
        else:
            raise FileSystemError("{0}, does not exist".format(self.path))

    def files(self):
        ''' lists all files inside current dir '''
        if os.path.exists(self.path):
            for name in os.listdir(self.path):
                if os.path.isfile(self.path + '\\' + name):
                    yield File(self.path + '\\' + name)
        else:
            raise FileSystemError("{0} directory not exists".
                                  format(self.path))

    def getsubdirectory(self, match=None, errors='strict'):
        ''' Returns Directory instance with subdirectory
        of current directory with name "name" '''
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

    def filesrecursive(self, *args, **kwargs):
        ''' Yields File instances of files inside of this
        directory, inside of subdirectories of this directory and so on '''
        return (
            item
            for item in self.walk(*args, **kwargs)
            if item.isfile()
        )
    
