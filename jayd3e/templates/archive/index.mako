<%!from markdown import markdown%>
<%inherit file="../layouts/base.mako"/>

<%def name="body()">
	<h1>Archives</h1>
    % for month in months:
        <%
            parts = month.split(" - ")
            m = parts[0]
            y = parts[1]
        %>
        <a href="/archive/${y}/${m}">${month}</a></br>
    % endfor
</%def>
