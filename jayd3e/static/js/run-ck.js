$(document).ready(function(){collapseExpandStart();$("code").each(function(a,b){lines=b.innerHTML.split("\n");if(lines[0].indexOf("#")==0){language=lines[0].replace(/#/g,"");$(b).addClass(language)}});hljs.tabReplace="    ";hljs.initHighlightingOnLoad()});