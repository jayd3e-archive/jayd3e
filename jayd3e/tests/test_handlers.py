import unittest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound
from jayd3e.handlers.auth import AuthHandler 
from jayd3e.handlers.blog import BlogHandler 
from jayd3e.handlers.doc import DocHandler
from jayd3e.handlers.post import PostHandler

class TestAuthHandler(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.str_POST = {}
        self.request.environ['PATH_INFO'] = ''
        self.config.include('pyramid_handlers')
        self.config.add_handler('auth_action', '/auth/{action}', handler=AuthHandler) 

    def testAuthHandlerInit(self):
        self.request.url = 'http://example.com/blog'
        handler = AuthHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertIs(handler.came_from, 'http://example.com/blog')
        self.assertIs(handler.here, '')

    def testAuthHandlerInitRedirect(self):
        self.request.url = 'http://example.com/auth/login'
        handler = AuthHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertIs(handler.came_from, '/')
        self.assertIs(handler.here, '')

    def testAuthLoginSuccess(self):
        self.request.str_POST = {'username':'test',
                                 'password':'testpass',
                                 'submit':''}
        handler = AuthHandler(self.request)
        response = handler.login()
        self.assertIsInstance(response, HTTPFound)

    def testAuthLoginFailed(self):
        self.request.str_POST = {'username':'test',
                                 'password':'wrongpass',
                                 'submit':''}
        handler = AuthHandler(self.request)
        response = handler.login()
        self.assertIn('message', response)
        self.assertEqual(response['message'], 'Failed login')

    def testAuthLogin(self):
        handler = AuthHandler(self.request)
        response = handler.login()
        self.assertIn('came_from', response)
        self.assertIn('title', response)
        self.assertIn('here', response)
        self.assertIn('url', response)
        self.assertIn('username', response)
        self.assertIn('password', response)
        self.assertIn('message', response)

    def testAuthLogout(self):
        handler = AuthHandler(self.request)
        response = handler.logout()
        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(response.location, '/')

    def tearDown(self):
        testing.tearDown()

class TestBlogHandler(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.environ['PATH_INFO'] = '/blog'

    def testBlogHandlerInit(self):
        handler = BlogHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/blog')
        self.assertEqual(handler.logged_in, None)

    def testBlogHandlerIndex(self):
        handler = BlogHandler(self.request)
        response = handler.index()
        self.assertIn('here', response)
        self.assertIn('title', response)
        self.assertIn('logged_in', response)
        self.assertIn('posts', response)

    def testBlogHandlerHackeyes(self):
        handler = BlogHandler(self.request)
        response = handler.hackeyes()
        self.assertEqual(response, {})

    def tearDown(self):
        testing.tearDown()

class TestDocHandler(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.environ['PATH_INFO'] = '/blog'

    def testDocHandlerInit(self):
        handler = DocHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/blog')
        self.assertEqual(handler.logged_in, None)

    def testDocHandlerIndex(self):
        handler = DocHandler(self.request)
        response = handler.index()
        self.assertEqual(response['here'], '/blog')
        self.assertEqual(response['logged_in'], None)
        self.assertEqual(response['title'], 'Design Documents')

    def testDocHandlerStug(self):
        handler = DocHandler(self.request)
        response = handler.stug()
        self.assertEqual(response['here'], '/blog')
        self.assertEqual(response['logged_in'], None)
        self.assertEqual(response['title'], 'Student Underground - Design Document')
    
    def testDocHandlerDd(self):
        handler = DocHandler(self.request)
        response = handler.dd()
        self.assertEqual(response['here'], '/blog')
        self.assertEqual(response['logged_in'], None)
        self.assertEqual(response['title'], 'Design Documentor - Design Document')
    
    def tearDown(self):
        testing.tearDown()

class testPostHandler(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.environ['PATH_INFO'] = '/post/add'

    def testPostHandlerInit(self):
        handler = PostHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/post/add')
        self.assertEqual(handler.logged_in, None)
