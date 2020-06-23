from utils.HashCompute import HashCompute
from FileSystemParser import *
from collections import defaultdict
import os

class DuplicateFinder:

    def __init__(self):
        self.filesize_grp    = defaultdict(list)
        self.firstMb_grp     = defaultdict(list)
        self.filecontent_grp = defaultdict(list)

    def find(self, path):
        self.groupByFilesize(FileSystemParser.getListOfFiles(path))
        self.groupByFirstMb()
        self.groupByFileContent()
        return self.filecontent_grp

    def groupByFilesize(self, listofFiles):
        for file in listofFiles:
            try:
                file = os.path.realpath(file)
                file_size = os.path.getsize(file)
            except (OSError,):
                continue
            self.filesize_grp[file_size].append(file)

    def groupByFirstMb(self):
        for _, files in self.filesize_grp.items():
            for file in files:
                firstMbHash = self.firstMbHashCompute(file)
                self.firstMb_grp[firstMbHash].append(file)

    def groupByFileContent(self):
        for _, files in self.firstMb_grp.items():
            for file in files:
                hashObj = HashCompute()
                with open(file, 'rb') as fileHandler:
                    chunk = fileHandler.read(1024)
                    while chunk:
                        hashObj.md5hashObj.update(chunk)
                        chunk = fileHandler.read(1024)
                chunkHash = hashObj.md5hashObj.digest()
                fileHandler.close()
                self.filecontent_grp[chunkHash].append(file)

    def firstMbHashCompute(self, file):
        with open(file, 'rb') as fileHandler:
            firstMbHash = HashCompute().md5hash(fileHandler.read(1024))
        fileHandler.close()
        return firstMbHash
