<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    % for post in posts:
        <div class="post">
            <h1>${post.date}</h1>
            <h2>${post.title}</h2>
            <p>${post.body}</p>
        </div>
    % endfor
</%def>