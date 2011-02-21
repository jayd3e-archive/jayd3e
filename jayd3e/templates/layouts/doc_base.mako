<!-- doc_base.mako --> 
<DOCTYPE html>
<%namespace name="header" file="header.mako"/>
<%namespace name="footer" file="footer.mako"/>

<html>
    <head>
        <title>${title}</title>
        <head>
        <title>Design Doc</title>
        <script language="javascript" type="text/javascript" src="/static/js/jquery.js"></script>
        <script language="javascript" type="text/javascript" src="/static/js/run.js"></script>
        <script language="javascript" type="text/javascript" src="/static/js/collapseExpand.js"></script>
        <link rel="stylesheet" type="text/css" href="/static/css/reset.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/doc_style.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/doc_type.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/type.css" />
    </head>
    <body>
        <div class="header">
            ${header.header(here)}
        </div>
        <div class="doc_body">
            ${self.body()}
        </div>
        <div class="footer">
            ${footer.footer()}
        </div>
    </body>
</html>