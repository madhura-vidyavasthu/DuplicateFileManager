from DuplicateFinder import *
from utils.ConsoleWrite import *
import sys

if __name__ == '__main__':

    dupObj = DuplicateFinder()
    duplicates = dupObj.find(sys.argv[1])
    ConsoleWrite.showDuplicates(duplicates)
