import unittest
from pyramid import testing
from jayd3e.models.site import SiteModel

class TestSiteModel(unittest.TestCase):
    def setUp(self):
        self.request = testing.DummyRequest
    
    def testSiteModelInit(self):
        model = SiteModel(self.request)
        self.assertIsNot(model, None)
