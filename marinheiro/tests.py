from yapsy.IPlugin import IPlugin

class BasicTest (IPlugin):
    """Basic operations in console"""
    def __init__(self):
        super().__init__()

class WebTest (IPlugin):
    """Operations with webservers"""
    def __init__(self):
        super().__init__()
