<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <form method="post">
        <label for="title">Title</label>
        <input name="title" value="${post.title}" class="post_title" id="title" type="text" tabindex="1"></input>

        <label for="body">Body</label>
        <textarea tabindex="2" cols="95" rows="20" name="body" id="body" class="post_body" tabindex="2">${post.body}</textarea>
        
        <input type="submit" value="Submit"></input>
    </form>
</%def>
