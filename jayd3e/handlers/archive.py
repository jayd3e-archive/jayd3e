from pyramid_handlers import action
from pyramid.security import authenticated_userid
from jayd3e.models.post import PostModel
from jayd3e.models.model import Session

class ArchiveHandler(object):
    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']
        self.logged_in = authenticated_userid(request)

    @action(renderer='archive/index.mako')
    def index(self):
        title = 'Archive Index'
        session = Session()
        posts = session.query(PostModel).order_by(PostModel.created).all()
        posts.reverse()
        
        months = []
        for post in posts:
            if post.created.strftime('%B - %Y') not in months:
                months.append(post.created.strftime('%B - %Y'))

        session.close()
        return {'here':self.here,
                'title':title,
                'logged_in':self.logged_in,
                'months':months}

    @action(renderer='archive/month.mako')
    def month(self):
        matchdict = self.request.matchdict
        date = matchdict['month'] + ' - ' + matchdict['year']
        title = 'Archive ' + date
        session = Session()
        
        posts = session.query(PostModel).all()
        posts.reverse()
        
        month_posts = []
        for post in posts:
            if post.created.strftime('%B - %Y') == date:
                month_posts.append(post)
            
        return {'here':self.here,
                'title':title,
                'logged_in':self.logged_in,
                'posts':month_posts} 
        