# to render html webpages
import random
from django.http import HttpResponse


def home_view(request):
    " take in a request django sends a request  return html response we pick to return a response"


name = 'halima'  # hard coded
# api call to some rest api with python and python request
number = random.randint(10, 1233123)  # pseduo random

# from the database


# django templates
h1_string = f"""
<h1 >hello {name} - {number}!< /h1 >


"""
p_string = f"""

<p>hi {name} - {number}!</p>
"""
html_string = h1_string + p_string

# return HttpResponse(html_string)
