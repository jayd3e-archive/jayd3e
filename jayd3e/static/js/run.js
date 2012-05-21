$(document).ready(function() {
    collapseExpandStart();

    $('code').each(function(index, code) {
        lines = code.innerHTML.split("\n");

        if(lines[0].indexOf("#") == 0) {
            language = lines[0].replace(/#/g, "");
            $(code).addClass(language);
        }
    });

    hljs.tabReplace = '    ';
    hljs.initHighlightingOnLoad();
});
