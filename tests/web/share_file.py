import requests

import marinheiro

class FileTxt (marinheiro.tests.WebTest):
    def run (self):
        try:
            res = requests.get("http://localhost/file.txt")
        except requests.ConnectionError as err:
            raise marinheiro.exceptions.FailedTest(repr(err))
        if not res.ok:
            raise marinheiro.exceptions.FailedTest(res.status_code)
        if res.text != "sQaq8XXm":
            raise marinheiro.exceptions.FailedTest("Wrong text")
