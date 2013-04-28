import unittest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound
from jayd3e.handlers.auth import AuthHandler
from jayd3e.handlers.blog import BlogHandler
from jayd3e.handlers.doc import DocHandler
from jayd3e.handlers.post import PostHandler
from jayd3e.handlers.site import SiteHandler
from jayd3e.handlers.feed import FeedHandler
from jayd3e.models.post import PostModel
from jayd3e.models.model import initializeDb
from jayd3e.models.model import engine
from jayd3e.models.model import Session
from jayd3e.db.config import TestConfig
from datetime import date
from datetime import datetime


class TestAuthHandler(unittest.TestCase):
    def setUp(self):
        initializeDb(engine(TestConfig))
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
        self.request.str_POST = {'username': 'test',
                                 'password': 'testpass',
                                 'submit': ''}
        handler = AuthHandler(self.request)
        response = handler.login()
        self.assertIsInstance(response, HTTPFound)

    def testAuthLoginFailed(self):
        self.request.str_POST = {'username': 'test',
                                 'password': 'wrongpass',
                                 'submit': ''}
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
        Session().close()


class TestBlogHandler(unittest.TestCase):
    def setUp(self):
        initializeDb(engine(TestConfig))
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
        Session().close()


class TestDocHandler(unittest.TestCase):
    def setUp(self):
        initializeDb(engine(TestConfig))
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
        Session().close()


class TestPostHandler(unittest.TestCase):
    def setUp(self):
        initializeDb(engine(TestConfig))
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.str_POST = {}
        self.request.environ['PATH_INFO'] = '/post'

    def testPostHandlerInit(self):
        handler = PostHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/post')
        self.assertEqual(handler.logged_in, None)

    def testPostHandlerAdd(self):
        self.request.environ['PATH_INFO'] += '/add'
        handler = PostHandler(self.request)
        response = handler.add()
        self.assertEqual(response['here'], '/post/add')
        self.assertEqual(response['logged_in'], None)
        self.assertEqual(response['title'], 'Post Add')

    def testPostHandlerAddSuccess(self):
        self.request.environ['PATH_INFO'] += '/add'
        self.request.str_POST = {'title':'Test Title',
                                 'body':'Test body.'}
        handler = PostHandler(self.request)
        response = handler.add()

        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(response.location, '/blog')

    def testPostHandlerEdit(self):
        session = Session()

        post = PostModel(title='Test Title',
                         body='Test body.',
                         date=date.today(),
                         created=datetime.now(),
                         change_time=datetime.now())
        session.add(post)
        session.flush()

        self.request.matchdict = {'id':post.id}
        self.request.environ['PATH_INFO'] += '/edit'

        handler = PostHandler(self.request)
        response = handler.edit()

        self.assertEqual(response['here'], '/post/edit')
        self.assertEqual(response['logged_in'], None)
        self.assertEqual(response['title'], 'Post Edit')
        self.assertIsNot(response['post'], None)

    def testPostHandlerEditSuccess(self):
        session = Session()
        #Create post in database
        post = PostModel(title='Test Title',
                         body='Test body.',
                         date=date.today(),
                         created=datetime.now(),
                         change_time=datetime.now())
        session.add(post)
        session.commit()
        id = post.id

        #Setup variables that are passed into the handler
        self.request.str_POST = {'title':'Test Title Changed',
                                 'body':'Test body changed.'}
        self.request.matchdict = {'id':id}
        self.request.environ['PATH_INFO'] += '/edit'

        #Call action and capture responsea
        handler = PostHandler(self.request)
        response = handler.edit()

        #Retrieve edited post
        session.refresh(post)

        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(response.location, '/blog')
        self.assertEqual(post.title, 'Test Title Changed')
        self.assertEqual(post.body, 'Test body changed.')

    def testPostHandlerDelete(self):
        session = Session()
        #Create post in database
        post = PostModel(title='Test Title',
                         body='Test body.',
                         date=date.today(),
                         created=datetime.now(),
                         change_time=datetime.now())
        session.add(post)
        session.commit()
        id = post.id

        #Setup variables that are passed into the handler
        self.request.matchdict = {'id':id}
        self.request.environ['PATH_INFO'] += '/delete'

        #Call action and capture responsea
        handler = PostHandler(self.request)
        response = handler.delete()

        #Retrieve edited post
        post = session.query(PostModel).filter_by(id=id).first()

        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(response.location, '/blog')
        self.assertEqual(post, None)

    def testPostHandlerView(self):
        session = Session()
        post = PostModel(title='Test Title',
                         body='Test body.',
                         date=date.today(),
                         created=datetime.now(),
                         change_time=datetime.now())
        session.add(post)
        session.commit()

        #Setup variables that are passed into the handler
        self.request.matchdict = {'id': post.id}
        self.request.environ['PATH_INFO'] += '/view'

        #Call action and capture responsea
        handler = PostHandler(self.request)
        response = handler.view()

        self.assertEqual(response['here'], '/post/view')
        self.assertEqual(response['logged_in'], None)
        self.assertEqual(response['title'], 'Post View')
        self.assertIsNot(response['post'], None)

    def tearDown(self):
        testing.tearDown()
        Session().close()


class TestSiteHandler(unittest.TestCase):
    def setUp(self):
        initializeDb(engine(TestConfig))
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.str_POST = {}
        self.request.environ['PATH_INFO'] = '/'

    def testSiteHandlerIndex(self):
        handler = SiteHandler(self.request)
        response = handler.index()

        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(response.location, '/blog')

    def tearDown(self):
        testing.tearDown()
        Session().close()


class TestFeedHandler(unittest.TestCase):
    def setUp(self):
        initializeDb(engine(TestConfig))
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.str_POST = {}
        self.request.environ['PATH_INFO'] = '/'

    def testFeedHandlerAtom(self):
        session = Session()

        for i in range(0, 10):
            post = PostModel(title='Test Title',
                             body='Test body.',
                             date=date.today(),
                             created=datetime.now(),
                             change_time=datetime.now())
            session.add(post)
        session.commit()

        handler = FeedHandler(self.request)
        response = handler.atom()

        correct_time = post.change_time.strftime("%Y-%m-%dT%H:%M:%SZ")

        self.assertIsNot(response['posts'], None)
        self.assertEqual(len(response['posts']), 5)
        self.assertEqual(response['updated'], correct_time)

    def testDown(self):
        testing.tearDown()
        Session().close()
