<%!from markdown import markdown%>
<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    % for post in posts:
        <div class="post">    
            <div class="title">
                <h1>${post.created.strftime('%B %d, %Y') if post.created else 'None'}</h1>
                % if logged_in:
                    <div class="operations">
                        <a href="/post/edit/${post.id}">Edit</a>
                        <a href="/post/delete/${post.id}">Delete</a>
                    </div>
                % endif
            </div>
            <div class="content">
                <h2>${post.title}</h2>
                ${markdown(post.body)|n}
            </div>
        </div>
    % endfor
</%def>
