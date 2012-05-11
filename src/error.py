class IdentiError(AttributeError):
    """Generic Error class for Identier"""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
