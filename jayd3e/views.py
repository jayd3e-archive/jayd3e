import datetime

from pyramid.view import view_config
from jayd3e.models import Post

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


@view_config(route_name='login',
             renderer='auth/login.mako')
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


@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location='/',
                     headers=headers)


@view_config(route_name='archive',
             renderer='archive/index.mako')
def archive(request):
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


@view_config(route_name='archive_month',
             renderer='archive/month.mako')
def archive_month(request):
    matchdict = request.matchdict
    db = request.db

    date = '%s-%s' % (matchdict['month'],
                      matchdict['year'])
    title = 'Archive ' + date

    posts = db.query(Post).all()
    posts.reverse()

    month_posts = []
    for post in posts:
        if post.created.strftime('%B - %Y') == date:
            month_posts.append(post)

    return {'title': title,
            'posts': month_posts}


@view_config(route_name='blog',
             renderer='blog/index.mako')
def blog(request):
    db = request.db

    title = 'Blog Index'

    posts = db.query(Post).order_by(Post.created).all()
    return {'title': title,
            'posts': posts}


@view_config(route_name='hackeyes',
             renderer='blog/hackeyes.mako')
def hackeyes(request):
    return {}


@view_config(route_name='contact',
             renderer='contact/index.mako')
def contact(self):
    title = 'Contact Info'

    return {'title': title}


@view_config(route_name='feed',
             renderer="feed/atom.mako")
def atom(request):
    db = request.db

    posts = db.query(Post).order_by(Post.created).all()

    max_change_time = db.query(func.max(Post.change_time)).first()
    updated = max_change_time[0].strftime("%Y-%m-%dT%H:%M:%SZ")

    return {'posts': posts,
            'updated': updated}


@view_config(route_name='post_add',
             renderer='post/add.mako',
             permission='edit')
def post_add(request):
    db = request.db

    title = 'Post Add'

    if request.POST:
        new_post = Post(title=request.POST['title'],
                        body=request.POST['body'],
                        date=datetime.date.today(),
                        created=datetime.now(),
                        change_time=datetime.now())
        db.add(new_post)
        db.commit()
        return HTTPFound(location='/blog')

    return {'title': title}


@view_config(route_name='post_edit',
             renderer='post/edit.mako',
             permission='edit')
def post_edit(request):
    db = request.db

    title = 'Post Edit'
    _id = request.matchdict['id']

    post = db.query(Post).filter_by(id=_id).first()

    if request.POST:
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.change_time = datetime.now()
        return HTTPFound(location='/blog')

    return {'title': title,
            'post': post}


@view_config(route_name='post_delete',
             permission='edit')
def post_delete(request):
    db = request.db

    _id = request.matchdict['id']

    delete_post = db.query(Post).filter_by(id=_id).first()
    db.delete(delete_post)

    return HTTPFound(location='/blog')


@view_config(renderer='post/view.mako')
def view(request):
    db = request.db

    title = 'Post View'

    _id = request.matchdict['id']
    post = db.query(Post).filter_by(id=_id).first()

    return {'title': title,
            'post': post}
