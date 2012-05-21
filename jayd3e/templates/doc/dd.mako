<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <!-- 
    -> "#" need to be the same
    -> The pound symbol in the anchor doesn't stand for a number, it actually means
    the pound symbol.
    
    <div class="collapseable">
        <h2>Title</h2>
        <p>Body</p>
    </div>
    -->
    <h1>Design Document</h1>
    <div class="collapseable">
        <h2>Name</h2>
        <p>This project will be known as the design doc project.</p>
    </div>
    <div class="collapseable">
        <h2>Description</h2>
        <p>This package will be an entirely html and javascript solution to
        creating effective, attractive design documents. As I continue to create
        new projects, I will further perfect this tool, adding a number of
        different features to increase the readability of the document. This
        design document will always be a side project, meant to enhance the rest
        of my work.</p>
    </div>
    <div class="collapseable">
       <h2>Requirements</h2>
       <ul class="styled_list">
           <li>Allow for collapseable/expandable sections.</li>
           <li>A comprehensive table of contents at the top of the page.</li>
       </ul>
    </div>
</%def>