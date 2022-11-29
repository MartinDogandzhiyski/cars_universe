from django.http import HttpResponse

from django.template import loader

from rest_framework import serializers, response, status


def handler500(request, *args, **argv):
    template = loader.get_template('error-500.html')
    response.status_code = 500
    return HttpResponse(template.render({}, request))


def handler404(request, *args, **argv):
    template = loader.get_template('error-404.html')
    response.status_code = 404
    return HttpResponse(template.render({}, request))
