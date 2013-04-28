from pyramid.view import view_config
from jayd3e.models.post import Post

from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember
from pyramid.security import forget
from jayd3e.security import USERS


def get_came_from(request, default_route_name='index'):
    # figure out where we came from
    ignore_urls = [
        request.route_url('login')
    ]
    referrer = request.params.get('came_from', request.url)

    if referrer in ignore_urls:
        referrer = request.route_url(default_route_name) # never use the login form itself as came_from

    return referrer


@view_config(renderer='auth/login.mako')
def login(request):
    title = 'Login Page'

    came_from = get_came_from(request)

    if 'submit' in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        if USERS.get(username) == password:
            headers = remember(request, username)
            return HTTPFound(location=came_from,
                             headers=headers)

        message = 'Failed login'

    return {'came_from': came_from,
            'title': title,
            'username': username,
            'message': message}


@view_config()
def logout(request):
    headers = forget(request)
    return HTTPFound(location='/',
                     headers=headers)


@view_config(renderer='archive/index.mako')
def index(request):
    db = request.db

    title = 'Archive Index'

    posts = db.query(Post).order_by(Post.created).all()
    posts.reverse()

    months = []
    for post in posts:
        if post.created.strftime('%B - %Y') not in months:
            months.append(post.created.strftime('%B - %Y'))

    return {'title': title,
            'months': months}


@view_config(renderer='archive/month.mako')
def month(request):
    matchdict = request.matchdict
    db = request.db

    date = matchdict['month'] + ' - ' + matchdict['year']
    title = 'Archive ' + date

    posts = db.query(Post).all()
    posts.reverse()

    month_posts = []
    for post in posts:
        if post.created.strftime('%B - %Y') == date:
            month_posts.append(post)

    return {'title': title,
            'posts': month_posts}


@view_config(renderer='blog/index.mako')
def index(self):
    title = 'Blog Index'
    session = Session()
    posts = session.query(PostModel).order_by(PostModel.created).all()
    #Sort descending by created date
    posts.reverse()
    #Grab the five most recent posts
    posts = posts[0:5]
    session.close()
    return {'here': self.here,
            'title': title,
            'logged_in': self.logged_in,
            'posts': posts}


@view_config(renderer='blog/hackeyes.mako')
def hackeyes(self):
    return {}


@view_config(renderer='contact/index.mako')
def index(self):
    title = 'Contact Info'

    return {'here': self.here,
            'title': title,
            'logged_in': self.logged_in}


@view_config(renderer="feed/atom.mako")
def atom(self):
    session = Session()

    posts = session.query(PostModel).order_by(PostModel.created).all()
    posts.reverse()
    posts = posts[0:5]

    max_change_time = session.query(func.max(PostModel.change_time)).first()
    updated = max_change_time[0].strftime("%Y-%m-%dT%H:%M:%SZ")

    session.close()
    return {'posts': posts,
            'updated': updated}


@view_config(renderer='post/add.mako', permission='edit')
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
    return {'here': self.here,
            'logged_in': self.logged_in,
            'title': title}


@view_config(renderer='post/edit.mako', permission='edit')
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
    return {'here': self.here,
            'logged_in': self.logged_in,
            'title': title,
            'post': post}


@view_config(permission='edit')
def delete(self):
    session = Session()
    id = self.request.matchdict['id']
    delete_post = session.query(PostModel).filter_by(id=id).first()
    session.delete(delete_post)
    session.commit()
    session.close()
    return HTTPFound(location='/blog')


@view_config(renderer='post/view.mako')
def view(self):
    session = Session()
    title = 'Post View'
    id = self.request.matchdict['id']
    post = session.query(PostModel).filter_by(id=id).first()
    session.close()
    return {'here': self.here,
            'title': title,
            'logged_in': self.logged_in,
            'post': post}
