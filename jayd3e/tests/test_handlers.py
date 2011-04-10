import unittest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound
from jayd3e.handlers.auth import AuthHandler 

class TestHandlers(unittest.TestCase):
    def setUp(self):
        self.request = testing.DummyRequest()
        self.config = testing.setUp(request=self.request)
        self.config.include('pyramid_handlers')
        self.config.add_handler('auth_action', '/auth/{action}', handler=AuthHandler) 

    def testAuthHandlerInit(self):
        handler = AuthHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertIsNot(handler.came_from, None)
        self.assertIsNot(handler.here, None)

    def testAuthLogin(self):
        handler = AuthHandler(self.request)
        response = handler.login()
        self.assertIn(response, 'came_from')
        self.assertIn(response, 'title')
        self.assertIn(response, 'here')
        self.assertIn(response, 'url')
        self.assertIn(response, 'username')
        self.assertIn(response, 'password')
        self.assertIn(response, 'message')

    def testAuthLogout(self):
        handler = AuthHandler(self.request)
        response = handler.logout()
        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(response.location, '/')

    def tearDown(self):
        testing.tearDown()
