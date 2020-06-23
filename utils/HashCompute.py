import hashlib

class HashCompute:

    def __init__(self):
        self.md5hashObj = hashlib.md5()

    def md5hash(self, string):
        return hashlib.md5(string).hexdigest()
