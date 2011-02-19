<%inherit file="../base.mako"/>

<%def name="body()">
    % for post in posts:
        ${post.id}
    % endfor
</%def>