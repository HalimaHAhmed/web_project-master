# to render html webpages
import random
from django.http import HttpResponse
from articles.models import Article





def home_view(request):
    " take in a request django sends a request  return html response we pick to return a response"

    name = 'halima'  # hard coded
    # api call to some rest api with python and python request
    number = random.randint(10, 1233123)  # pseduo random
    article_obj = Article.objects.get(id=1)

    # from the database
    # article_name
    # article_content
    article_title = article_obj.title
    article_content = article_obj.content

    # django templates
    h1_string = f"""
    <h1 >hello world{article_title}({article_obj.id})!< /h1 >


    """
    p_string = f"""

    <p>hi{article_content}!</p>
    """
    html_string = h1_string + p_string

    return HttpResponse(html_string)
