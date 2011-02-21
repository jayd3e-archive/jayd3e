<%inherit file="../layouts/doc_base.mako"/>

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
    <h1>Student Underground</h1>
    <div class="collapseable">
       <h2>Name</h2>
       <p>For the time being, this project will be known as the "Student Underground"
       project.  In actuality, this would be an acceptable name for the finished site;
       however, it will be temporarily used as a handle for the project as a whole,
       until more thought is put into the actual branding of the site.</p>
    </div>
    <div class="collapseable">
       <h2>Description</h2>
       <p>The main purpose of this proposed project is to provide a means for students
       to collaborate on assignments and tests through any means necessary.  The site
       will have a number of networks that will be linked to universities or other 
       educational institutions, which students can enroll themselves in.  These networks
       will be organizaed into classes, which will contain a variety of different 
       class-specific elements(assignments and articles to name a few).  It has yet to
       be decided how these classes will be added to the networks(heavy moderation may be
       necessary).</p>
    </div>
    <div class="collapseable">
       <h2>Requirements</h2>
       <ul>
           <li>Allow students to easily write out the solutions to a variety of complex
           mathematical problems.</li>
           <li>Provide a point system that will allow active users to be rewarded.</li>
       </ul>
    </div>
</%def>