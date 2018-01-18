# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	#fields to display
	list_display=["title","updated","timestamp"]
	#on which we can open the post
	list_display_links=["updated"]
	#filter the content
	list_filter=["updated","timestamp"]
	#which field is searchable
	search_fields=["title","content"]
	#field which can be edited
	list_editable=["title"]
	class Meta:
		model=Post #model class name where we want to make changes

admin.site.register(Post,PostModelAdmin)