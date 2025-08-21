import os

class Utils:
    def __init__(self):
        pass

    def createDir(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)