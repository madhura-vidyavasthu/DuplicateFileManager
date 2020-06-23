import os

class FileSystemParser:

    def getListOfFiles(path):
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        return listOfFiles