import unittest
from pyramid import testing


class TestExceptions(unittest.TestCase):
    def testNotFound(self):
        from jayd3e.exceptions import notFound
        request = testing.DummyRequest()
        self.assertIn('title', notFound(request))

    def testForbidden(self):
        from jayd3e.exceptions import forbidden
        from pyramid.httpexceptions import HTTPFound
        request = testing.DummyRequest()
        self.assertIsInstance(forbidden(request), HTTPFound)
        self.assertEqual(forbidden(request).location, '/auth/login')
