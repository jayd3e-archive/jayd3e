<?xml version="1.0" encoding="utf-8"?>
 
<feed xmlns="http://www.w3.org/2005/Atom">
 
        <title>JayD3e's Feed</title>
        <subtitle>A feed for my blog.</subtitle>
        <link href="http://jayd3e.com/feed" rel="self" />
        <link href="http://jayd3e.com" />
        <id>http://jayd3e.com</id>
        <updated>${updated}</updated>
        <author>
                <name>Joe Dallago</name>
                <email>jd.dallago@gmail.com</email>
        </author>
        % for post in posts: 
            <entry>
                    <title>${post.title}</title>
                    <link href="http://jayd3e.com/post/view/${post.id}" />
                    <id>http://jayd3e.com/post/view/${post.id}</id>
                    <updated>${post.change_time}</updated>
                    <summary></summary>
            </entry>
        % endfor
</feed>
