import unittest
from jayd3e import main

class TestMain(unittest.TestCase):
    def testMain(self):
        app = main(self)
        self.assertIsNot(app.registry, None)
