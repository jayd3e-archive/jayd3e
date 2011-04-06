from pyramid_handlers import action
from pyramid.security import authenticated_userid
from jayd3e.models.post import PostModel
from jayd3e.handlers.handler import Handler
from pyramid.httpexceptions import HTTPFound
from datetime import date
from datetime import datetime

class PostHandler(Handler):
    def setup(self):
        self.here = self.request.environ['PATH_INFO']
        self.POST = self.request.str_POST
        self.logged_in = authenticated_userid(self.request)

    @action(renderer='post/add.mako', permission='edit')
    def add(self):
        self.title = 'Post Add'
        if self.POST:
            new_post = PostModel(title=self.POST['title'],
                                 body=self.POST['body'],
                                 date=date.today(),
                                 created=datetime.now(),
                                 change_time=datetime.now())
            self.session.add(new_post)
            self.session.commit()
            return HTTPFound(location='/blog')
        return {'here':self.here,
                'logged_in':self.logged_in,
                'title':self.title}

    @action(renderer='post/edit.mako', permission='edit')
    def edit(self):
        self.title = 'Post Edit'
        id = self.request.matchdict['id']
        self.post = self.session.query(PostModel).filter_by(id=id).first()
        if self.POST:
            self.post.title = self.POST['title']
            self.post.body = self.POST['body']
            self.session.commit()
            return HTTPFound(location='/blog')
        return {'here':self.here,
                'logged_in':self.logged_in,
                'title':self.title,
                'post':self.post}

    @action(permission='edit')
    def delete(self):
        id = self.request.matchdict['id']
        delete_post = self.session.query(PostModel).filter_by(id=id).first()
        self.session.delete(delete_post)
        self.session.commit()
        return HTTPFound(location='/blog')

    @action(renderer='post/view.mako')
    def view(self):
        self.title = 'Post View'
        id = self.request.matchdict['id']
        self.post = self.session.query(PostModel).filter_by(id=id).first()
        return {'here':self.here,
                'title':self.title,
                'logged_in':self.logged_in,
                'post':self.post}
