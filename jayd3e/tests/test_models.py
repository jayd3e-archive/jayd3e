import unittest
from pyramid import testing


class TestSiteModel(unittest.TestCase):
    def setUp(self):
        self.request = testing.DummyRequest

    def testSiteModelInit(self):
        model = SiteModel(self.request)
        self.assertIsNot(model, None)

    def testPostModel(self):
        post = PostModel()
        self.assertTrue(str(post).startswith('<Post'))
