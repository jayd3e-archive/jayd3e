<%!from markdown import markdown%>
<%inherit file="../layouts/base.mako"/>

<%def name="body()">
	<h1>Archives</h1>
    % for month in months:
        <a href="/archive/${month}">${month}</a>
    % endfor
</%def>
