function collapseExpand(e) {
    if (!e) var e = window.event;
    div = e.target.parentNode;
    children = div.children;
    for ( var i = 0; i < children.length; i++) {
        collapseOrExpand(children[i]);
    }
}

function collapseExpandStart(){
    var divs=document.getElementsByTagName('div'); 
    for(var i=0; i<divs.length; i++){
        if(divs[i].className == "collapseable"){
            children = divs[i].children;
            for(var j=0; j < children.length; j++) {
                if(children[j].tagName == 'H2'){
                    children[j].onclick = collapseExpand;
                }
                else if(children[j].tagName in {'P':'','UL':'','OL':''}){
                    children[j].style.display = 'block';
                }
            }
        }
    }
}

function collapseOrExpand(child) {
    if ((child.tagName in {
        'P' : '',
        'UL' : '',
        'OL' : ''
    }) && (child.style.display == 'none')) {
        child.style.display = "block";
    } else if ((child.tagName in {
        'P' : '',
        'UL' : '',
        'OL' : ''
    }) && (child.style.display == 'block')) {
        child.style.display = "none";
    }
}