from jayd3e.models.model import Session

class Handler(object):
    session = Session()

    def __init__(self):
        pass

    def __del__(self):
        self.session.close()
