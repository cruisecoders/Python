from django.conf.urls import url
from HN.views import hn_list

urlpatterns = [
    url(r'^hn/$',hn_list),
]
