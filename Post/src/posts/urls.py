from django.conf.urls import url
from posts.views import (post_create,post_delete,post_detail,post_list,post_update)

urlpatterns = [
	url(r'^$',post_list,name='list'),
    url(r'^create/$',post_create,name='create'),
    url(r'^(?P<slug>[\w-]+)/$',post_detail,name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$',post_update,name='update'),
    url(r'^(?P<id>[\w-]+)/delete/$',post_delete),
]