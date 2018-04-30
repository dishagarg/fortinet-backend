from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings

import urllib.request, json


def get_table(request):
    """GET request for data with pagination."""
    json = get_json()
    page = request.GET.get('page')
    paginator = Paginator(json, 4)
    json = paginator.get_page(page)
    print(json)

    return render(request, 'view.html', {'json': json})


def get_json():
    """GET request for JSON data list."""
    response = urllib.request.urlopen(settings.JSON_URL)
    json_data = json.loads(response.read().decode('utf-8'))
    return json_data
