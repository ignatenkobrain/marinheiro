class FailedTest (Exception):
    def __init__(self, msg=None):
        super().__init__()
        self.msg = msg
