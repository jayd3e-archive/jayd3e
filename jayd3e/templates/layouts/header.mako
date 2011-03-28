<%def name="header(here)">
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
        ${'<a href="/auth/logout">Logout</a>' if logged_in else '<a href="/auth/login">Login</a>'}
    </div>
</%def>
