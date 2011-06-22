<%def name="header(here)">
	<div class="top">
		<div class="shoutbox">
			<p>"Say 'Hi' To Your Mother for Me."</p>
		</div>
		<div class="header_graphic"></div>
	</div>
	<div class="bot">
	    <a href="/">
	        <div class="logo"></div>
	    </a>
	    <ul class="main">
	        <li>
	            <a
	            ${' class="active" ' if '/blog' in here else '' | n}
	            href="/blog">
	                <span>Recent</span> 
	            </a>
	        </li>
	        <li>
	            <a
	            ${'class="active"' if '/blog/archive' in here else '' | n}
	            href="/blog/archive">
	                <span>Archives</span>
	            </a>
	        </li>
	        <li>
	            <a
	            ${'class="active"' if '/doc' in here else '' | n}
	            href="/doc">            
	                <span>Docs</span>
	            </a>
	        </li>
	        <li>
	            <a
	            ${'class="active"' if '/blog/contact' in here else '' | n}
	            href="/blog/contact">
	                <span>Contact</span>
	            </a>
	        </li>
	    </ul>
	    <div class="auth_span">
	        ${logged_in if logged_in else 'Guest'} - 
	        % if logged_in:            
	            <a href="/post/add">New Post</a> -
	            <a href="/auth/logout">Logout</a> 
	        % else:
	            <a href="/auth/login">Login</a>
	        % endif
	    </div>
	</div>
</%def>
