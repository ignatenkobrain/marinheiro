import os.path

import marinheiro

class CreateFile (marinheiro.tests.BasicTest):
    def run (self):
        path = "/tmp/file.txt"
        if not os.path.isfile(path):
            raise marinheiro.exceptions.FailedTest("{} is not file".format(path))
        if os.path.getsize(path) != 0:
            raise marinheiro.exceptions.FailedTest("{} is not zero byte".format(path))
