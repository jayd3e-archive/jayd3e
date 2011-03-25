<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <form method="post" class="std_form">
        <label for="title">Title</label>
        <input name="title" id="title" type="text" tabindex="1"></input>
        <label for="body">Body</label>
        <textarea tabindex="2" cols="95" rows="20" name="body" id="body" tabindex="2"></textarea>
        <input type="submit" value="Submit"></input>
    </form>
</%def>
