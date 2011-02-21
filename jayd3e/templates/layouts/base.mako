<%namespace name="header" file="header.mako"/>
<%namespace name="footer" file="footer.mako"/>

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
            ${header.header(here)}
        </div>
        <div class="body">
            ${self.body()}
        </div>
        <div class="footer">
            ${footer.footer()}
        </div>
    </body>
</html>