from jayd3e.models.model import Session

class Handler(object):
    def __init__(self, request):
        self.session = Session()
        self.request = request
        self.setup()

    def __del__(self):
        self.session.close()
