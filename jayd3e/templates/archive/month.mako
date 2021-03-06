<%!from markdown import markdown%>
<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    % for post in posts:
        <div class="post">
            <h1>${post.created.strftime('%B %d, %Y') if post.created else 'None'}</h1>
            % if logged_in:
                <div class="operations">
                    <a class="primary" href="/post/edit/${post.id}">Edit</a>
                    <a class="danger" href="/post/delete/${post.id}">Delete</a>
                </div>
            % endif
            <div class="content styled_lists">
                <h2>${post.title}</h2>
                ${markdown(post.body)|n}
            </div>
        </div>
    % endfor
</%def>
