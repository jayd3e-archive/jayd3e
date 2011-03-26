<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <form method="post" action="${url}" class="std_auth_form">
        <label for="username">Username</label>
        <input name="username" class="auth_username" id="username" type="text" tabindex="1"></input>
        <label for="password">Password</label>
        <input name="password" class="auth_password" id="password" type="password" tabindex="2"></input>
        <input type="submit" value="Submit" name="submit"></input>
    </form>
</%def>
