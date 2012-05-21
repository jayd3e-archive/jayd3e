from pyramid_handlers import action
from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from jayd3e.models.post import PostModel
from jayd3e.models.model import Session
from datetime import date
from datetime import datetime

class PostHandler(object):
    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']
        self.logged_in = authenticated_userid(request)

    @action(renderer='post/add.mako', permission='edit')
    def add(self):
        title = 'Post Add'
        session = Session()
        if self.request.POST:
            new_post = PostModel(title=self.request.POST['title'],
                                 body=self.request.POST['body'],
                                 date=date.today(),
                                 created=datetime.now(),
                                 change_time=datetime.now())
            session.add(new_post)
            session.commit()
            return HTTPFound(location='/blog')
        session.close()
        return {'here':self.here,
                'logged_in':self.logged_in,
                'title':title}

    @action(renderer='post/edit.mako', permission='edit')
    def edit(self):
        session = Session()
        title = 'Post Edit'
        id = self.request.matchdict['id']
        post = session.query(PostModel).filter_by(id=id).first()
        if self.request.POST:
            post.title = self.request.POST['title']
            post.body = self.request.POST['body']
            post.change_time = datetime.now()
            session.commit()
            return HTTPFound(location='/blog')

        session.close()
        return {'here':self.here,
                'logged_in':self.logged_in,
                'title':title,
                'post':post}

    @action(permission='edit')
    def delete(self):
        session = Session()
        id = self.request.matchdict['id']
        delete_post = session.query(PostModel).filter_by(id=id).first()
        session.delete(delete_post)
        session.commit()
        session.close()
        return HTTPFound(location='/blog')

    @action(renderer='post/view.mako')
    def view(self):
        session = Session()
        title = 'Post View'
        id = self.request.matchdict['id']
        post = session.query(PostModel).filter_by(id=id).first()
        session.close()
        return {'here':self.here,
                'title':title,
                'logged_in':self.logged_in,
                'post':post}
