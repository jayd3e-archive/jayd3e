import unittest
from pyramid import testing
from jayd3e.models.site import SiteModel
from jayd3e.models.post import PostModel

class TestSiteModel(unittest.TestCase):
    def setUp(self):
        self.request = testing.DummyRequest

    def testSiteModelInit(self):
        model = SiteModel(self.request)
        self.assertIsNot(model, None)

    def testPostModel(self):
        post = PostModel()
        self.assertTrue(str(post).startswith('<Post'))
