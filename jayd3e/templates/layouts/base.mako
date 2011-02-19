<!-- base.mako --> 
<DOCTYPE html>
<html>
    <head>
        <title>${title}</title>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/type.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/reset.css" />
    </head>
    <body>
        <div class="header">
            ${self.header()}
        </div>
        ${self.body()}
        <div class="footer">
            ${self.footer()}
        </div>
    </body>
</html>

<%def name="header()">
    <a href="/">
        <div class="logo"></div>
    </a>
    <ul class="main">
        <li>
            <a class="active" href="/blog">
               <span>Recent</span> 
            </a>
        </li>
        <li>
            <a href="/blog/archive">
               <span>Archives</span>
            </a>
        </li>
        <li>
            <a href="/doc">	           
                <span>Docs</span>
            </a>
        </li>
        <li>
            <a href="/blog/contact">
               <span>Contact</span>
            </a>
        </li>
    </ul>
</%def>

<%def name="footer()">
</%def>