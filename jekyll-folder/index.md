---
layout: page 
title: Bellisimon's Database course
description: CSCI-UA 60 Database Design and Web Implementation (Fall 2017)
---
{% for post in site.posts limit: 15 %}
<div class="logo">
	<a href="/~ms9144"><img src="{{  site.baseurl  }}/img/logo.png"></a>
</div>
<div>
	<a href=".{{  post.url  }}"><h1 class="postTitle">{{  post.title  }}</h1></a>
</div>
<div class="postDescription">
	<i>{{post.date | date_to_long_string}}</i>
</div>
<div class="describe">{{post.description}}</div> {{post.content | truncatewords: 30}}
<a href=".{{post.url}}">Read More<a>
<hr class="pbreak" />
{% endfor %}


