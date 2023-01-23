# to render html webpages
from django.http import HttpResponse
html_string = "<h1>hello halimah</h1>"


def home(request):
    " take in a request django sends a request  return html response we pick to return a response"

# hel
    return HttpResponse(html_string)
