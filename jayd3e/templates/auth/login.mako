<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <form method="post" action="${url}" class="basic">
        <p>${message if message else ""}</p>
        <label for="username">Username</label>
        <input name="username" id="username" type="text" tabindex="1"></input>
        <label for="password">Password</label>
        <input name="password" id="password" type="password" tabindex="2"></input>
        <input type="submit" value="Submit" name="submit"></input>
    </form>
</%def>
