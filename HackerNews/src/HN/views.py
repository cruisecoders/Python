# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from HN.utils import getting_data, getting_sentiments
from HN.models import Hnews
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from HN.models import Hnews
from HN.serializers import HnewsSerializer

# Create your views here.
# @csrf_exempt
def hn_list(request):
    if request.is_ajax():
        x = 2
        while True:
            data = getting_data(x)
            emotions = getting_sentiments(data.get('title'))
            instance = Hnews(hn_id = data.get('id'),
                            username = data.get('author'),
                            title = data.get('title'),
                            url = data.get('url'),
                            score = data.get('points'),
                            hn_type = data.get('type'),
                            sentiments = emotions.get('polarity_confidence'))
            instance.save()
            x += 1
    snip = Hnews.objects.all()
    context = {
            "data": snip
            }
    return render(request, "hn_list.html",context)
