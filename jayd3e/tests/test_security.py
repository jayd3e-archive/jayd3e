import unittest
from pyramid import testing
from jayd3e.security import groupfinder


class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.request = testing.DummyRequest()

    def testGroupFinder(self):
        groups = groupfinder('test', self.request)
        self.assertEqual(groups, ['group:admins'])
