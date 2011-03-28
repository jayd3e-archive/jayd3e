<%!from markdown import markdown%>
<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    % for post in posts:
        <div class="post">
            <h1>${post.date.strftime('%B %d, %Y') if post.date else 'None'}</h1>
            <h2>${post.title}</h2>
            <p>${markdown(post.body)}</p>
        </div>
    % endfor
</%def>
