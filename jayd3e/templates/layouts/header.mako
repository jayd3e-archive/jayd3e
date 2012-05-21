<%def name="header(here)">
	    <a class="logo" href="/"></a>
	    <ul class="nav">
	        <li>
	            <a
	            ${' class="active" ' if '/blog' in here else '' | n}
	            href="/blog">
	                <span>Recent</span> 
	            </a>
	        </li>
	        <li>
	            <a
	            ${'class="active"' if '/archive' in here else '' | n}
	            href="/archive">
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
	            ${'class="active"' if '/contact' in here else '' | n}
	            href="/contact">
	                <span>Contact</span>
	            </a>
	        </li>
	    </ul>
	    <ul class="account">
	    	% if logged_in:
	            <li>
	            	<a href="/auth/logout">Logout</a>
	            </li>
	            <li>
		        	<span>-</span>
		        </li>
	        	<li>      
	            	<a href="/post/add">New Post</a>
	            </li>
	        % else:
	            <li>
	            	<a href="/auth/login">Login</a>
	            </li>
	        % endif
	        <li>
	        	<span>-</span>
	        </li>
	        <li>
	        	<span>${logged_in if logged_in else 'Guest'}</span>
	        </li>
	    </ul>
</%def>
