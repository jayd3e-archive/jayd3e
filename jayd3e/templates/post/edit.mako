<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <form class="horiz-form" method="post">
        <div class="input_group">
            <label for="title">Title</label>
            <div class="inputs">
                <input name="title" class="post_title" value="${post.title}" id="title" type="text" tabindex="1" />
            </div>
        </div>

        <div class="input_group">
            <label for="body">Body</label>
            <div class="inputs">
                <textarea tabindex="2" cols="95" rows="20" name="body" id="body" class="post_body" tabindex="2">${post.body}</textarea>
            </div>
        </div>

        <div class="form_actions">
            <input class="primary" type="submit" value="Submit"></input>
        </div>
    </form>
</%def>
